# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import subprocess

import pytest

# Testing "workers" command

# Sub command:
#   {dockerfile,list,logs,show,test}
#                         Sub command
#     dockerfile          LAVA worker Dockerfile
#     list                List workers
#     logs                Worker logs
#     show                Worker details
#     test                Test connection to server

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def workers_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "dockerfile" subcommand
def test_dockerfile_noid(workers_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "dockerfile"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam workers dockerfile: error:" in call_result.stderr


def test_dockerfile_valid(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1111/dockerfile"
    ).respond_with_data("DOCKERFILE_CONTENT", content_type="text/plain", status=200)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "dockerfile", "1111"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "DOCKERFILE_CONTENT" in call_result.stdout


def test_dockerfile_notexisting(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1112/dockerfile"
    ).respond_with_data("Not Found", content_type="text/plain", status=404)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "dockerfile", "1112"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "Unable to call the appliance API" in call_result.stderr
    assert "404" in call_result.stderr


# Testing "list" subcommand
def test_list_invalid(workers_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "list", "AAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_list_valid(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request("/api/v1/workers").respond_with_json(
        {
            "items": [
                {
                    "id": 1113,
                    "name": "laa-0000X",
                    "server_url": "https://staging.validation.linaro.org/",
                },
                {
                    "id": 1115,
                    "name": "laa-0000Y",
                    "server_url": "https://iotil.validation.linaro.org/",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Workers:" in call_result.stdout
    assert (
        "1113: laa-0000X - https://staging.validation.linaro.org/" in call_result.stdout
    )
    assert (
        "1115: laa-0000Y - https://iotil.validation.linaro.org/" in call_result.stdout
    )


def test_list_json(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request("/api/v1/workers").respond_with_json(
        {
            "items": [
                {
                    "id": 1113,
                    "name": "laa-0000X",
                    "server_url": "https://staging.validation.linaro.org/",
                },
                {
                    "id": 1115,
                    "name": "laa-0000Y",
                    "server_url": "https://iotil.validation.linaro.org/",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "list", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "id": 1113,
            "name": "laa-0000X",
            "server_url": "https://staging.validation.linaro.org/",
        },
        {
            "id": 1115,
            "name": "laa-0000Y",
            "server_url": "https://iotil.validation.linaro.org/",
        },
    ]


# Testing "logs" subcommand
def test_logs_invalid(workers_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "logs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam workers logs: error:" in call_result.stderr


def test_logs_notexisting(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1112/logs"
    ).respond_with_data("Not Found", content_type="text/plain", status=404)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "logs", "1112"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "Unable to call the appliance API" in call_result.stderr
    assert "404" in call_result.stderr


def test_logs(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1116/logs"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-13T11:08:32.032Z",
                "dt_iso": "2025-08-13T11:08:32+00:00",
                "message": "WARNING => Image not available",
                "priority": 4,
            },
            {
                "dt": "2025-08-13T11:08:37.032Z",
                "dt_iso": "2025-08-13T11:08:37+00:00",
                "message": "   INFO Get server version",
                "priority": 6,
            },
            {
                "dt": "2025-08-13T11:08:37.417Z",
                "dt_iso": "2025-08-13T11:08:37+00:00",
                "message": "   INFO => 2025.06.dev0098",
                "priority": 6,
            },
        ]
    )

    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "logs", "1116"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert (
        "2025-08-13T11:08:32+00:00 \x1b[1;31mWARNING => Image not available\x1b[0m"
        in call_result.stdout
    )
    assert "2025-08-13T11:08:37+00:00    INFO Get server version" in call_result.stdout
    assert "2025-08-13T11:08:37+00:00    INFO => 2025.06.dev0098" in call_result.stdout


def test_logs_json(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1118/logs"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-13T11:12:03.511Z",
                "dt_iso": "2025-08-13T11:12:03+00:00",
                "message": 'WARNING Error response from daemon: Get "https://hub.lavasoftware.org/v2/": dial tcp: lookup hub.lavasoftware.org on 8.8.8.8:53: no such host',
                "priority": 4,
            },
            {
                "dt": "2025-08-13T11:12:03.512Z",
                "dt_iso": "2025-08-13T11:12:03+00:00",
                "message": "WARNING => Image not available",
                "priority": 4,
            },
        ]
    )

    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "logs", "1118", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "dt": "2025-08-13T11:12:03.511Z",
            "dt_iso": "2025-08-13T11:12:03+00:00",
            "message": 'WARNING Error response from daemon: Get "https://hub.lavasoftware.org/v2/": dial tcp: lookup hub.lavasoftware.org on 8.8.8.8:53: no such host',
            "priority": 4,
        },
        {
            "dt": "2025-08-13T11:12:03.512Z",
            "dt_iso": "2025-08-13T11:12:03+00:00",
            "message": "WARNING => Image not available",
            "priority": 4,
        },
    ]


# Testing "show" subcommand
def test_show_invalid(workers_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "show"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam workers show: error:" in call_result.stderr


def test_show_notexisting(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1112"
    ).respond_with_data("Not Found", content_type="text/plain", status=404)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "show", "1112"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "Unable to call the appliance API" in call_result.stderr
    assert "404" in call_result.stderr


def test_show(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1120"
    ).respond_with_json(
        {
            "running": True,
            "id": 1120,
            "name": "laa-0000Z",
            "server_url": "https://staging.validation.linaro.org/",
            "token": "XYZXYZ",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "show", "1120"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "id        : 1120" in call_result.stdout
    assert "name      : laa-0000Z" in call_result.stdout
    assert "running   : True" in call_result.stdout
    assert "server url: https://staging.validation.linaro.org/" in call_result.stdout
    assert "token     : XYZXYZ" in call_result.stdout


def test_show_json(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1121"
    ).respond_with_json(
        {
            "running": True,
            "id": 1121,
            "name": "laa-0000U",
            "server_url": "https://iotl.validation.linaro.org/",
            "token": "UUUUUU",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "show", "1121", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "running": True,
        "id": 1121,
        "name": "laa-0000U",
        "server_url": "https://iotl.validation.linaro.org/",
        "token": "UUUUUU",
    }


# Testing "test" subcommand
def test_test_invalid(workers_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "test"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam workers test: error:" in call_result.stderr


def test_test_notexisting(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1121/test"
    ).respond_with_data("Not Found", content_type="text/plain", status=404)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "test", "1121"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "Unable to call the appliance API" in call_result.stderr
    assert "404" in call_result.stderr


def test_test(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1121/test"
    ).respond_with_json(
        {"connected": True, "error": "Missing 'version'", "status_code": 400}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "test", "1121"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert call_result.stderr == ""
    assert call_result.stdout == ""


def test_test_json(workers_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/workers/1124/test"
    ).respond_with_json(
        {"connected": True, "error": "Missing 'version'", "status_code": 400}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "workers", "test", "1124", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "connected": True,
        "error": "Missing 'version'",
        "status_code": 400,
    }
