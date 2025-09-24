# Copyright (c) 2021 Julien Floret
# Copyright (c) 2021 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
import logging
import os
from typing import Callable

from aiohttp import web

from .util import BaseView, TarResponse


LOG = logging.getLogger(__name__)


# --------------------------------------------------------------------------------------
class FormatDirView(BaseView):
    @classmethod
    def urls(cls):
        yield "/branches/{branch}/{tag}/{job}/{format}/"
        yield "/~{user}/branches/{branch}/{tag}/{job}/{format}/"
        yield "/products/{product}/{variant}/{product_branch}/{version}/{format}/"
        yield "/~{user}/products/{product}/{variant}/{product_branch}/{version}/{format}/"

    async def head(self):
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        if fmt.is_dirty():
            raise web.HTTPNotFound()
        if fmt.url() != self.request.path:
            raise web.HTTPFound(fmt.url())
        return web.Response()

    async def get(self):
        """
        Get the list of files of a job for the specified format.
        """
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        if fmt.url() != self.request.path:
            raise web.HTTPFound(fmt.url())
        if "html" in self.request.headers.get("Accept", "json"):
            return await self.autoindex(fmt, "")
        data = {
            "artifact_format": {
                "name": fmt.name,
                "internal": fmt.is_internal(),
                "dirty": fmt.is_dirty(),
                "files": list(fmt.get_digests().keys()),
            },
        }
        return web.json_response(data)

    async def patch(self):
        """
        Remove the dirty flag from a format.
        """
        version = self.request.match_info.get(
            "tag", self.request.match_info.get("version")
        )
        if "product" in self.request.match_info or version in (
            "latest",
            "stable",
            "oldstable",
        ):
            raise web.HTTPMethodNotAllowed("PATCH", ["GET"])
        fmt = _get_format(self.repo(), self.request.match_info)
        try:
            await fmt.post_process()
            fmt.set_dirty(False)
        except OSError as e:
            LOG.error("post process failed: %s", e)
            raise web.HTTPInternalServerError(reason="post process failed") from e
        return web.Response()

    async def delete(self):
        """
        Delete a format.
        """
        loop = asyncio.get_running_loop()
        try:
            fmt = _get_format(self.repo(), self.request.match_info, delete=True)
            await loop.run_in_executor(None, fmt.delete)
            self.repo().schedule_cleanup_orphans()
        except FileNotFoundError as e:
            raise web.HTTPNotFound() from e
        except OSError as e:
            raise web.HTTPBadRequest(reason=str(e)) from e
        return web.Response()


# --------------------------------------------------------------------------------------
class FormatArchiveView(BaseView):
    @classmethod
    def urls(cls):
        yield "/branches/{branch}/{tag}/{job}/{format}.tar"
        yield "/~{user}/branches/{branch}/{tag}/{job}/{format}.tar"
        yield "/products/{product}/{variant}/{product_branch}/{version}/{format}.tar"
        yield "/~{user}/products/{product}/{variant}/{product_branch}/{version}/{format}.tar"

    async def head(self):
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        if fmt.is_dirty():
            raise web.HTTPNotFound()
        url = fmt.url().rstrip("/") + ".tar"
        if url != self.request.path:
            raise web.HTTPFound(url)
        return web.Response()

    async def get(self):
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        url = fmt.url().rstrip("/") + ".tar"
        if url != self.request.path:
            raise web.HTTPFound(url)

        return TarResponse(
            fmt.get_digests(), fmt.path(), fmt.archive_name(), fmt.timestamp()
        )


# --------------------------------------------------------------------------------------
class FormatDigestsView(BaseView):
    @classmethod
    def urls(cls):
        yield "/branches/{branch}/{tag}/{job}/{format}.sha256"
        yield "/~{user}/branches/{branch}/{tag}/{job}/{format}.sha256"
        yield "/products/{product}/{variant}/{product_branch}/{version}/{format}.sha256"
        yield "/~{user}/products/{product}/{variant}/{product_branch}/{version}/{format}.sha256"

    async def get(self):
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        url = fmt.url().rstrip("/") + ".sha256"
        if url != self.request.path:
            raise web.HTTPFound(url)
        sha256sums = []
        for artifact, digest in sorted(fmt.get_digests().items()):
            algo, digest = digest.split(":")
            if algo == "sha256":
                sha256sums.append(f"{digest}  {artifact}\n")
        return web.Response(text="".join(sha256sums))


# --------------------------------------------------------------------------------------
class FormatFileView(BaseView):
    @classmethod
    def urls(cls):
        yield "/branches/{branch}/{tag}/{job}/{format}"
        yield "/~{user}/branches/{branch}/{tag}/{job}/{format}"
        yield "/products/{product}/{variant}/{product_branch}/{version}/{format}"
        yield "/~{user}/products/{product}/{variant}/{product_branch}/{version}/{format}"

    async def head(self):
        return await self.get()

    async def get(self):
        """
        If only one file in $format:
            redirect to /branches/$branch/$tag/$job/$format/$file
        else:
            redirect to /branches/$branch/$tag/$job/$format/
        """
        fmt = _get_format(self.repo(), self.request.match_info, self.access_granted)
        if fmt.is_dirty():
            raise web.HTTPNotFound()
        files = list(fmt.get_digests().keys())
        if len(files) == 1 and files[0] != "index.html":
            return web.HTTPFound(
                fmt.url() + files[0],
                headers={
                    "Content-Disposition": f"attachment; filename={os.path.basename(files[0])}"
                },
            )
        return web.HTTPFound(fmt.url())


# --------------------------------------------------------------------------------------
def _get_format(
    repo, match_info, access_cb: Callable[[str], bool] = None, delete=False
):
    try:
        if "product" in match_info:
            if delete:
                raise web.HTTPBadRequest(
                    reason="Deleting product formats is not supported"
                )
            fmt = (
                repo.get_product(match_info["product"])
                .get_variant(match_info["variant"])
                .get_branch(match_info["product_branch"])
                .get_version(match_info["version"], access_cb)
                .get_format(match_info["format"])
            )
        else:
            job = (
                repo.get_branch(match_info["branch"])
                .get_tag(match_info["tag"], access_cb)
                .get_job(match_info["job"])
            )
            fmt = job.get_format(match_info["format"])
            if delete and job.is_locked() and not fmt.is_internal():
                raise web.HTTPBadRequest(reason="Cannot delete format: job is locked")
    except FileNotFoundError as e:
        raise web.HTTPNotFound() from e
    if not fmt.exists():
        raise web.HTTPNotFound()
    return fmt
