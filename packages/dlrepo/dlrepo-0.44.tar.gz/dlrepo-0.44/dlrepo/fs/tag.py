# Copyright (c) 2021 Julien Floret
# Copyright (c) 2021 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
import json
import logging
import os
from pathlib import Path
import socket
from typing import Iterator, Optional

import aiohttp

from .fmt import ArtifactFormat
from .job import Job
from .util import SubDir


LOG = logging.getLogger(__name__)


# --------------------------------------------------------------------------------------
class Tag(SubDir):
    """
    TODO
    """

    def create(self):
        super().create()
        stamp = self._path / ".stamp"
        if not stamp.exists():
            stamp.touch()

    @classmethod
    def creation_date(cls, t):
        stamp = t.path() / ".stamp"
        if stamp.is_file():
            # prefer mtime over ctime
            # on UNIX, ctime is "the time of most recent metadata change" whereas
            # mtime is "most recent content modification"
            return stamp.stat().st_mtime
        return 0

    @property
    def timestamp(self) -> int:
        return Tag.creation_date(self)

    def get_jobs(self) -> Iterator[Job]:
        yield from Job.all(self)

    def get_job(self, name: str) -> Job:
        return Job(self, name)

    def _publish_status_path(self) -> Path:
        return self._path / ".publish-status"

    def publish_status(self) -> Optional[str]:
        try:
            return self._publish_status_path().read_text().strip()
        except FileNotFoundError:
            return None

    def _released_path(self) -> Path:
        return self._path / ".released"

    def is_released(self) -> bool:
        return self._released_path().is_file()

    def set_released(self, released: bool, semaphore: asyncio.Semaphore):
        if not self.PUBLISH_URL:
            raise ValueError("DLREPO_PUBLISH_URL is undefined")
        if not self.PUBLISH_AUTH:
            raise ValueError("DLREPO_PUBLISH_AUTH is undefined")
        if not self._path.is_dir():
            raise FileNotFoundError()
        loop = asyncio.get_running_loop()
        task = loop.create_task(self.do_release(released, semaphore))
        task.add_done_callback(self.done_cb)

    def _stable_path(self) -> Path:
        return self._path / ".stable"

    def is_stable(self) -> bool:
        return self._stable_path().is_file()

    def set_stable(self, stable: bool):
        if not self._path.is_dir():
            raise FileNotFoundError()
        path = self._stable_path()
        if stable:
            path.touch()
        elif path.is_file():
            path.unlink()

    def _description_path(self) -> Path:
        return self._path / ".description"

    def description(self) -> Optional[str]:
        try:
            return self._description_path().read_text().strip()
        except FileNotFoundError:
            return None

    def set_description(self, description: str):
        description = description.strip()
        if description:
            self._description_path().write_text(f"{description}\n")
        elif self._description_path().is_file():
            self._description_path().unlink()

    def done_cb(self, task):
        if task.cancelled():
            return
        exc = task.exception()
        if exc:
            LOG.error("while changing released flag on tag %s", self.name, exc_info=exc)
            self._publish_status_path().write_text(f"error: {exc}\n")

    PUBLISH_URL = os.getenv("DLREPO_PUBLISH_URL")
    PUBLISH_AUTH = os.getenv("DLREPO_PUBLISH_AUTH")
    PUBLISH_FILTER_CMD = os.getenv("DLREPO_PUBLISH_FILTER_CMD")
    PUBLISH_TIMEOUT = int(os.getenv("DLREPO_PUBLISH_TIMEOUT", "300"))
    USER_AGENT = f"dlrepo-server/{socket.gethostname()}"

    def _publish_session(self, url) -> aiohttp.ClientSession:
        with open(self.PUBLISH_AUTH, "r", encoding="utf-8") as f:
            buf = f.read().strip()
        if ":" not in buf:
            raise ValueError("invalid DLREPO_PUBLISH_AUTH file")
        login, password = buf.split(":", 1)
        auth = aiohttp.BasicAuth(login, password, "utf-8")
        timeout = aiohttp.ClientTimeout(total=self.PUBLISH_TIMEOUT)
        return aiohttp.ClientSession(
            url,
            auth=auth,
            timeout=timeout,
            raise_for_status=True,
            headers={"User-Agent": self.USER_AGENT},
        )

    async def _publish_filter(self, url):
        proc = await asyncio.create_subprocess_exec(
            self.PUBLISH_FILTER_CMD, url, cwd=self._path
        )
        ret = await proc.wait()
        return ret == 0

    async def do_release(self, released: bool, semaphore: asyncio.Semaphore):
        published_jobs = []
        self._publish_status_path().write_text("in progress\n")
        for publish_url in self.PUBLISH_URL.split(","):
            if self.PUBLISH_FILTER_CMD and not await self._publish_filter(publish_url):
                continue
            async with self._publish_session(publish_url) as sess:
                if released:
                    LOG.info(
                        "publishing tag %s/%s to %s",
                        self.parent.name,
                        self.name,
                        publish_url,
                    )
                    await self._publish(sess, publish_url, semaphore)
                    async with semaphore:
                        try:
                            resp = await sess.get(self.url())
                            data = await resp.read()
                            data = json.loads(data.decode("utf-8"))
                            published_jobs = data["tag"]["jobs"]
                        except aiohttp.client_exceptions.ClientResponseError as e:
                            if e.status != 404:
                                raise
                else:
                    LOG.info(
                        "deleting tag %s/%s from %s",
                        self.parent.name,
                        self.name,
                        publish_url,
                    )
                    async with semaphore:
                        try:
                            await sess.delete(self.url())
                        except aiohttp.client_exceptions.ClientResponseError as e:
                            if e.status != 404:
                                raise
        released_path = self._released_path()
        if released and published_jobs:
            released_path.touch()
            self._publish_status_path().write_text(f"published to {self.PUBLISH_URL}\n")
        else:
            if released_path.is_file():
                released_path.unlink()
            for job in self.get_jobs():
                job.set_released(False)
            status_path = self._publish_status_path()
            if status_path.is_file():
                status_path.unlink()

    async def _publish(
        self,
        sess: aiohttp.ClientSession,
        publish_url: str,
        semaphore: asyncio.Semaphore,
    ):
        loop = asyncio.get_running_loop()
        for job in self.get_jobs():
            job_url = job.url()
            if not job.is_locked():
                LOG.debug(
                    "job %s is not locked, skipping release",
                    job_url,
                )
                continue
            if job.is_internal():
                # in case job was already published, delete it from the public server
                async with semaphore:
                    await sess.delete(job_url, raise_for_status=False)
                job.set_released(False)
                continue
            async with semaphore:
                resp = await sess.get(job_url, raise_for_status=False)
            if resp and resp.status == 200:
                data = await resp.read()
                data = data.decode("utf-8")
                data = json.loads(data)
                if data.get("job", {}).get("digest") == job.get_digest():
                    LOG.debug(
                        "job %s already up to date on public server, skipping release",
                        job_url,
                    )
                    continue
                # delete the job previously released before re-uploading it
                async with semaphore:
                    await sess.delete(job_url, raise_for_status=False)
                job.set_released(False)
            self._publish_status_path().write_text(
                f"uploading {job.name} to {publish_url}\n"
            )
            tasks = []
            for fmt in job.get_formats(exclude_internal=True):
                tasks.append(loop.create_task(self._publish_fmt(fmt, sess, semaphore)))
            await asyncio.gather(*tasks)
            metadata = job.get_metadata(dynamic=False)
            LOG.debug("publishing job metadata %s", job_url)
            async with semaphore:
                await sess.patch(job_url, json={"job": metadata})
            job.set_released(True)
            LOG.debug("locking job %s", job_url)
            async with semaphore:
                await sess.put(job_url, json={"job": {"locked": True}})

    async def _publish_fmt(
        self,
        fmt: ArtifactFormat,
        sess: aiohttp.ClientSession,
        semaphore: asyncio.Semaphore,
    ):
        fmt_url = fmt.url()
        loop = asyncio.get_running_loop()

        async def _publish_file(file, digest):
            file_url = fmt_url + file
            headers = {"Digest": digest}

            async with semaphore:
                resp = await sess.head(
                    file_url, headers=headers, raise_for_status=False
                )
            if resp.status == 200:
                LOG.debug("publishing file %s (deduplicated)", file_url)
                # file digest already present on the server, do not upload
                # the data again
                headers["X-Dlrepo-Link"] = digest
                async with semaphore:
                    await sess.put(file_url, data=None, headers=headers)

            else:
                LOG.debug("publishing file %s", file_url)
                # file digest not on server, proceed with upload
                async with semaphore:
                    with open(fmt.path() / file, "rb") as f:
                        await sess.put(file_url, data=f, headers=headers)

        tasks = []
        for file, digest in fmt.get_digests().items():
            tasks.append(loop.create_task(_publish_file(file, digest)))
        await asyncio.gather(*tasks)

        # clear the dirty flag
        async with semaphore:
            await sess.patch(fmt_url)

    def _locked_path(self) -> Path:
        return self._path / ".locked"

    def is_locked(self) -> bool:
        return self._locked_path().is_file()

    def set_locked(self, locked: bool):
        path = self._locked_path()
        if locked:
            path.touch()
        elif path.is_file():
            path.unlink()

    def delete(self):
        if not self.exists():
            raise FileNotFoundError()
        if self.is_locked():
            raise OSError(f"Tag {self.name} is locked")
        if self.is_released():
            raise OSError(f"Tag {self.name} is released, unrelease it first")
        for j in self.get_jobs():
            j.delete()
        self.root().rmtree(self._path)
