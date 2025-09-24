# Copyright (c) 2022 Julien Floret
# Copyright (c) 2022 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import hashlib

import aiohttp
import pytest


pytestmark = pytest.mark.asyncio


async def test_no_headers(dlrepo_server):
    url, _ = dlrepo_server
    async with aiohttp.ClientSession(url) as sess:
        for u in ("/", "/not-found", "/cli"):
            resp = await sess.get(u)
            assert resp.status == 401
        resp = await sess.get("/static/logo.svg")
        assert resp.status == 200


async def test_no_groups(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "x-dlrepo-login": "foo",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        for u in ("/", "/not-found", "/cli"):
            resp = await sess.get(u)
            assert resp.status == 401
        resp = await sess.get("/static/logo.svg")
        assert resp.status == 200


async def test_valid_headers(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "x-dlrepo-login": "foo",
        "x-dlrepo-groups": "group1,baz",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        resp = await sess.get("/")
        assert resp.status == 200
        resp = await sess.get("/not-found")
        assert resp.status == 404
        resp = await sess.get("/cli")
        assert resp.status == 200
        text = await resp.text()
        with open("dlrepo-cli", "r", encoding="utf-8") as f:
            assert text == f.read()
        resp = await sess.get("/static/logo.svg")
        assert resp.status == 200


async def test_write_denied(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "x-dlrepo-login": "foo",
        "x-dlrepo-groups": "group1,baz",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        resp = await sess.put("/branches/main/tag/job/format/file.txt")
        assert resp.status == 401


@pytest.mark.dependency()
async def test_write_allowed(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "x-dlrepo-login": "bar",
        "x-dlrepo-groups": "group2,bleh",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        data = b"content"
        digest = hashlib.sha256(data).hexdigest()
        resp = await sess.put(
            "/branches/main/tag/job/format/file.txt",
            data=data,
            headers={"Digest": f"sha256:{digest}"},
        )
        assert resp.status == 201
        resp = await sess.put(
            "/branches/main/tag/job/format/file2.txt",
            data=data + b"corrupt",
            headers={"Digest": f"sha256:{digest}"},
        )
        assert resp.status == 422


@pytest.mark.dependency(depends=["test_write_allowed"])
async def test_read_allowed(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "X-Dlrepo-login": "foo",
        "X-Dlrepo-groups": "group1,baz",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        resp = await sess.get("/branches/main/tag/job/format/file.txt")
        assert resp.status == 200
        data = await resp.read()
        assert data == b"content"


async def test_read_denied(dlrepo_server):
    url, _ = dlrepo_server
    async with aiohttp.ClientSession(url) as sess:
        resp = await sess.get("/branches/main/tag/job/format/file.txt")
        assert resp.status == 401
    headers = {
        "x-DLREPO-login": "coin",
        "x-dlrepo-groups": "group3",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        resp = await sess.get("/branches/main/tag/job/format/file.txt")
        assert resp.status == 401


async def test_acl_regexp(dlrepo_server):
    url, _ = dlrepo_server
    headers = {
        "x-dlrepo-LOGIn": "coin",
        "x-dlrepo-GROUps": "group3",
    }
    async with aiohttp.ClientSession(url, headers=headers) as sess:
        data = b"content"
        digest = hashlib.sha256(data).hexdigest()
        resp = await sess.put(
            "/branches/main/tag2/job/format/file2.txt",
            data=data,
            headers={"Digest": f"sha256:{digest}"},
        )
        assert resp.status == 201
        resp = await sess.get("/branches/main/tag2/job/format/file2.txt")
        assert resp.status == 200
        data = await resp.read()
        assert data == b"content"
