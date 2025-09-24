# Copyright (c) 2021 Julien Floret
# Copyright (c) 2021 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import pathlib
import shutil
import socket
import subprocess
import sys
import time

import pytest


def get_free_tcp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 0))
        _, portnum = sock.getsockname()
        return portnum


@pytest.fixture(scope="module")
def start_dlrepo_server(request, tmp_path_factory):
    dlrepo_servers = []

    def _start_dlrepo_server():
        tmp_path = tmp_path_factory.mktemp("pytest_dlrepo")
        data_dir = pathlib.Path(request.fspath).parent / request.module.__name__
        for d in ("branches", "products", "users"):
            folder = data_dir / d
            if folder.is_dir():
                shutil.copytree(folder, tmp_path / d)
        portnum = get_free_tcp_port()
        env = {
            "DLREPO_ROOT_DIR": str(tmp_path),
            "DLREPO_LISTEN_ADDRESS": "127.0.0.1",
            "DLREPO_LISTEN_PORT": str(portnum),
            "DLREPO_TEMPLATES_DIR": str(data_dir / "templates"),
            "DLREPO_STATIC_DIR": str(data_dir / "static"),
            "DLREPO_LOG_OUTPUT": "console",
            "DLREPO_LOG_LEVEL": "DEBUG",
        }
        acls = data_dir / "acls"
        if acls.is_dir():
            env["DLREPO_ACLS_DIR"] = str(acls)
        auth = data_dir / "auth"
        if auth.is_file():
            env["DLREPO_AUTH_FILE"] = str(auth)
        else:
            headers = data_dir / "headers"
            if headers.is_dir():
                for h in headers.iterdir():
                    env[h.name] = h.read_text("utf-8").strip()
            else:
                env["DLREPO_AUTH_DISABLED"] = "1"
        settings = data_dir / "settings"
        if settings.is_dir():
            for s in settings.iterdir():
                env[s.name] = s.read_text("utf-8").strip()
        post_process = data_dir / "post-process.sh"
        if post_process.is_file():
            env["DLREPO_POST_PROCESS_CMD"] = str(post_process)
        proc = subprocess.Popen(  # pylint: disable=consider-using-with
            [sys.executable, "-m", "dlrepo"], env=env
        )
        dlrepo_servers.append(proc)
        while proc.poll() is None:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(("127.0.0.1", portnum))
                break
            except socket.error:
                time.sleep(0.1)
        assert proc.poll() is None
        return f"http://127.0.0.1:{portnum}", tmp_path

    def stop_dlrepo_server():
        for proc in dlrepo_servers:
            proc.terminate()

    request.addfinalizer(stop_dlrepo_server)
    return _start_dlrepo_server


@pytest.fixture(scope="module")
def dlrepo_server(start_dlrepo_server):  # pylint: disable=redefined-outer-name
    """
    Use the same instance for all tests except publication ones.
    """
    yield start_dlrepo_server()


@pytest.fixture(
    scope="module",
    params=[
        {
            "max_requests": "1",
            "quantity": 1,
        },
    ],
)
def dlrepo_publish_servers(
    request, tmp_path_factory, start_dlrepo_server
):  # pylint: disable=redefined-outer-name
    reference = pathlib.Path(__file__).parent / "publish_reference"
    tmp_path = tmp_path_factory.mktemp("pytest_dlrepo_publish")
    shutil.copytree(reference / "branches", tmp_path / "branches")
    shutil.copytree(reference / "products", tmp_path / "products", symlinks=True)
    auth = tmp_path / "publish.auth"
    auth.write_text("foo:bar")  # use garbage credentials, auth is disabled anyway
    public_urls = [start_dlrepo_server()[0] for _ in range(request.param["quantity"])]

    portnum = get_free_tcp_port()

    env = {
        "DLREPO_ROOT_DIR": str(tmp_path),
        "DLREPO_LISTEN_ADDRESS": "127.0.0.1",
        "DLREPO_LISTEN_PORT": str(portnum),
        "DLREPO_LOG_OUTPUT": "console",
        "DLREPO_LOG_LEVEL": "DEBUG",
        "DLREPO_AUTH_DISABLED": "1",
        "DLREPO_PUBLISH_URL": ",".join(public_urls),
        "DLREPO_PUBLISH_AUTH": auth,
        "DLREPO_PUBLISH_MAX_REQUESTS": request.param["max_requests"],
    }
    with subprocess.Popen([sys.executable, "-m", "dlrepo"], env=env) as proc:
        while proc.poll() is None:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(("127.0.0.1", portnum))
                break
            except socket.error:
                time.sleep(0.1)
        assert proc.poll() is None
        try:
            yield f"http://127.0.0.1:{portnum}", public_urls
        finally:
            proc.terminate()
