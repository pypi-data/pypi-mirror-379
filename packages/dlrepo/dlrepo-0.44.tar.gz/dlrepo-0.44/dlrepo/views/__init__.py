# Copyright (c) 2021 Julien Floret
# Copyright (c) 2021 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
from datetime import datetime, timezone
import os
import pathlib
import re

from aiohttp import web
import aiohttp_jinja2
import jinja2

from ..fs.util import human_readable
from .artifact import ArtifactView
from .branch import BranchesView, BranchView
from .container import (
    BlobsUploadsView,
    BlobsView,
    CatalogView,
    ManifestReadOnlyView,
    ManifestView,
    NewBlobUploadView,
    RootView,
    TagsListView,
)
from .fmt import FormatArchiveView, FormatDigestsView, FormatDirView, FormatFileView
from .job import JobArchiveView, JobView
from .product import (
    ProductBranchView,
    ProductsView,
    ProductVariantView,
    ProductView,
    VersionArchiveView,
    VersionView,
)
from .tag import TagView
from .util import BaseView


# --------------------------------------------------------------------------------------
class HomeView(BaseView):
    LATEST_RELEASES = os.getenv("DLREPO_LATEST_RELEASES", "1") != "0"
    LATEST_RELEASES_USER = os.getenv("DLREPO_LATEST_RELEASES_USER", "1") != "0"

    @classmethod
    def urls(cls):
        yield "/"
        yield "/~{user}"
        yield "/~{user}/"

    def _get_version_dirs(self, repo):
        stamps = list(repo.path().glob("products/*/*/*/*/.stamp"))
        # prefer mtime over ctime
        # on UNIX, ctime is "the time of most recent metadata change" whereas
        # mtime is "most recent content modification"
        stamps.sort(key=lambda s: s.stat().st_mtime, reverse=True)
        versions = []
        for s in stamps:
            versions.append(s.parent)
        return versions

    async def get_latest_releases(self, repo, num=10):
        loop = asyncio.get_running_loop()
        version_dirs = await loop.run_in_executor(None, self._get_version_dirs, repo)
        versions = []
        for v in version_dirs:
            version = (
                repo.get_product(v.parent.parent.parent.name)
                .get_variant(v.parent.parent.name)
                .get_branch(v.parent.name)
                .get_version(v.name)
            )
            if self.access_granted(version.url()):
                versions.append(version)
                if len(versions) == num:
                    break
        return versions

    @aiohttp_jinja2.template("home.html")
    async def get(self):
        repo = self.repo()
        user = self.request.match_info.get("user")
        if user:
            if not repo.path().exists():
                raise web.HTTPNotFound()
            if not self.request.path.endswith("/"):
                raise web.HTTPFound(self.request.path + "/")
            data = {
                "disk_usage": repo.disk_usage,
                "quota": repo.QUOTA,
                "human_readable": human_readable,
                "access": {
                    "branches": self.access_granted(repo.url() + "branches/"),
                    "products": self.access_granted(repo.url() + "products/"),
                },
            }
            if self.LATEST_RELEASES_USER:
                data["latest_releases"] = await self.get_latest_releases(repo)
            return data
        users = []
        for r in repo.get_user_repos():
            if self.access_granted(r.url()):
                users.append(r.user)
        data = {
            "users": users,
            "access": {
                "branches": self.access_granted("/branches/"),
                "products": self.access_granted("/products/"),
            },
        }
        if self.LATEST_RELEASES:
            data["latest_releases"] = await self.get_latest_releases(repo)
        return data


# --------------------------------------------------------------------------------------
class StaticView(BaseView):
    ROOT = pathlib.Path(__file__).parent.parent.parent
    PUBLIC_URL = os.getenv("DLREPO_PUBLIC_URL")
    CLI = b""
    for root in (ROOT, pathlib.Path("/usr/local/bin"), pathlib.Path("/usr/bin")):
        cli = root / "dlrepo-cli"
        if cli.is_file():
            CLI = cli.read_text(encoding="utf-8")
            if PUBLIC_URL:
                CLI = CLI.replace("http://127.0.0.1:1337", PUBLIC_URL)
            CLI = CLI.encode("utf-8")
            break
    CLI_HEADERS = {
        "Content-Type": "text/plain; charset=utf-8",
        "Content-Length": str(len(CLI)),
    }
    STATIC_DIRS = []
    if os.getenv("DLREPO_STATIC_DIR"):
        STATIC_DIRS.append(pathlib.Path(os.getenv("DLREPO_STATIC_DIR")))
    STATIC_DIRS.append(ROOT / "dlrepo/static")

    @classmethod
    def urls(cls):
        yield "/cli"
        yield "/static/{file}"

    def resolve_filepath(self):
        relpath = self.request.match_info["file"]
        if relpath.startswith("/") or any(x in (".", "..") for x in relpath.split("/")):
            raise web.HTTPNotFound()
        for static_dir in self.STATIC_DIRS:
            path = static_dir / relpath
            if path.is_file():
                return path
        raise web.HTTPNotFound()

    async def get(self):
        if self.request.path == "/cli":
            return web.Response(body=self.CLI, headers=self.CLI_HEADERS)
        # Do not use self.file_response to avoid X-Sendfile.
        # The static roots are dynamic and it makes complex reverse proxy configs.
        # The static files are small anyway.
        return web.FileResponse(self.resolve_filepath())

    async def head(self):
        if self.request.path == "/cli":
            return web.Response(headers=self.CLI_HEADERS)
        return await self.get()


# --------------------------------------------------------------------------------------
async def template_vars(request):
    return {
        "year": datetime.now().strftime("%Y"),
        "request": request,
        **request.match_info,
    }


# --------------------------------------------------------------------------------------
def pretty_time(timestamp: int, fmt: str = "%Y %b %d, %H:%M:%S UTC") -> str:
    if not timestamp:
        return "n/a"
    utc_time = datetime.fromtimestamp(timestamp, timezone.utc)
    return utc_time.strftime(fmt)


# --------------------------------------------------------------------------------------
def semantic_sort(value, reverse=False, case_sensitive=False, attribute=None):
    """Sort a list of strings using semantic/natural version ordering."""
    if not isinstance(value, list):
        return value

    def _version_key(value, case_sensitive=False, attribute=None):
        if attribute:
            value = getattr(value, attribute, value[attribute])

        key = []
        for part in re.split(r"[\.\-_]", value):
            # Add int/str identifier to prevent mixed comparison issues when values are not
            # formatted identically, e.g. "my-branch-1.9" "my-maintenance-branch-1.7"
            if part.isdigit():
                key.append((0, int(part)))
            elif case_sensitive:
                key.append((1, part))
            else:
                key.append((1, part.lower()))
        return key

    return sorted(
        value,
        key=lambda item: _version_key(item, case_sensitive, attribute),
        reverse=reverse,
    )


# --------------------------------------------------------------------------------------
def add_routes(app):
    template_dirs = []
    if os.getenv("DLREPO_TEMPLATES_DIR"):
        template_dirs.append(os.getenv("DLREPO_TEMPLATES_DIR"))
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dirs += [
        os.path.join(base_dir, "templates"),
        # add the parent path of the default templates dir to allow overriding
        # builtin templates in DLREPO_TEMPLATES_DIR
        # Inspired from https://github.com/ipython/ipython/commit/905835ea53d3a
        base_dir,
    ]
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(template_dirs),
        context_processors=[template_vars],
        extensions=["jinja2.ext.do"],
        trim_blocks=True,
        lstrip_blocks=True,
        filters={
            "pretty_time": pretty_time,
            "semantic_sort": semantic_sort,
        },
    )
    for route in (
        HomeView,
        StaticView,
        # artifacts
        BranchesView,
        BranchView,
        TagView,
        JobArchiveView,
        JobView,
        FormatArchiveView,
        FormatDigestsView,
        FormatFileView,
        FormatDirView,
        ArtifactView,
        ProductsView,
        ProductView,
        ProductVariantView,
        ProductBranchView,
        VersionArchiveView,
        VersionView,
        # docker
        RootView,
        CatalogView,
        ManifestView,
        TagsListView,
        NewBlobUploadView,
        BlobsUploadsView,
        BlobsView,
        TagsListView,
        ManifestReadOnlyView,
    ):
        for url in route.urls():
            app.add_routes([web.view(url, route)])
