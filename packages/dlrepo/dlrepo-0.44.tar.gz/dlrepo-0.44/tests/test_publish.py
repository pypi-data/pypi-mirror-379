# Copyright (c) 2022 Julien Floret
# Copyright (c) 2022 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import asyncio

import aiohttp
import pytest


pytestmark = pytest.mark.asyncio


_PUBLISH_TEST_CASES = {
    "single-server-single-request": {
        "max_requests": "1",
        "quantity": 1,
    },
    "single-server-many-requests": {
        "max_requests": "10",
        "quantity": 1,
    },
    "many-servers-single-request": {
        "max_requests": "1",
        "quantity": 2,
    },
    "many-servers-many-requests": {
        "max_requests": "10",
        "quantity": 2,
    },
}


@pytest.mark.parametrize(
    "dlrepo_publish_servers",
    _PUBLISH_TEST_CASES.values(),
    indirect=True,
    ids=_PUBLISH_TEST_CASES.keys(),
)
async def test_publish(dlrepo_publish_servers):
    url, public_urls = dlrepo_publish_servers
    async with aiohttp.ClientSession(url) as sess:
        resp = await sess.post(
            "/branches/branch/tag/",
            json={"tag": {"released": True}},
        )
        assert resp.status == 200
        await asyncio.sleep(1)
        resp = await sess.get("/branches/branch/tag/")
        assert resp.status == 200
        data = await resp.json()
        assert data["tag"]["publish_status"] == f"published to {','.join(public_urls)}"

        for public_url in public_urls:
            async with aiohttp.ClientSession(public_url) as pub_sess:
                for job in "job1", "job2":
                    for fmt in "fmt1", "fmt2":
                        sha_url = f"/branches/branch/tag/{job}/{fmt}.sha256"
                        resp = await sess.get(sha_url)
                        assert resp.status == 200
                        data = await resp.text()
                        resp = await pub_sess.get(sha_url)
                        assert resp.status == 200
                        data_pub = await resp.text()
                        assert data_pub == data
                sha_url = "/branches/branch/tag/internal_job/fmt1.sha256"
                resp = await sess.get(sha_url)
                assert resp.status == 200
                resp = await pub_sess.get(sha_url)
                assert resp.status == 404
