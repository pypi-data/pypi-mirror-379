# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import re
import signal
import subprocess
import time

import pytest

from tests.mock_appliance_ws import MockApplianceWs

# Testing "serials" command

# Sub command:
#   {list,connect,show}  Sub command
#     list               List serials
#     connect            Connect to serial
#     show               Serial details


# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def serials_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


@pytest.fixture
def ws_appliance():
    return MockApplianceWs()


@pytest.fixture
def ws_config(serials_config, ws_appliance):
    subprocess.run(
        ["laam", "identities", "update", "idtest", "--uri", ws_appliance.base_url]
    )
    return serials_config


# Testing "list" subcommand
def test_list(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "LEGACY-ttyUSB1",
                    "port": 2001,
                    "path": "/dev/ttyUSB1",
                    "speed": "115200n81",
                },
                {
                    "name": "ttyACM0",
                    "port": 2020,
                    "path": "/dev/ttyACM0",
                    "speed": "115200n81",
                },
                {
                    "name": "ttyACM0-1_5M",
                    "port": 2220,
                    "path": "/dev/ttyACM0",
                    "speed": "1500000n81",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "LEGACY-ttyUSB1" in call_result.stdout
    assert "2001" in call_result.stdout
    assert "/dev/ttyUSB1" in call_result.stdout
    assert "ttyACM0-1_5M" in call_result.stdout
    assert "2220" in call_result.stdout
    assert "/dev/ttyACM0" in call_result.stdout
    assert "115200n81" in call_result.stdout


def test_list_json_1(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "LEGACY-ttyUSB1",
                    "port": 2001,
                    "path": "/dev/ttyUSB1",
                    "speed": "115200n81",
                },
                {
                    "name": "ttyACM0",
                    "port": 2020,
                    "path": "/dev/ttyACM0",
                    "speed": "115200n81",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "list", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "name": "LEGACY-ttyUSB1",
            "port": 2001,
            "path": "/dev/ttyUSB1",
            "speed": "115200n81",
        },
        {"name": "ttyACM0", "port": 2020, "path": "/dev/ttyACM0", "speed": "115200n81"},
    ]


def test_list_json_2(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "ttymxc3-3M",
                    "port": 2300,
                    "path": "/dev/ttymxc3",
                    "speed": "3000000n81",
                },
                {
                    "name": "ttymxc3-9600",
                    "port": 2100,
                    "path": "/dev/ttymxc3",
                    "speed": "9600n81",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "list", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "name": "ttymxc3-3M",
            "port": 2300,
            "path": "/dev/ttymxc3",
            "speed": "3000000n81",
        },
        {
            "name": "ttymxc3-9600",
            "port": 2100,
            "path": "/dev/ttymxc3",
            "speed": "9600n81",
        },
    ]


def test_list_filter_ok(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "LEGACY-ttyUSB1",
                    "port": 2001,
                    "path": "/dev/ttyUSB1",
                    "speed": "115200n81",
                },
                {
                    "name": "ttyACM0",
                    "port": 2020,
                    "path": "/dev/ttyACM0",
                    "speed": "115200n81",
                },
            ]
        }
    )
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "serials",
            "list",
            "--filter",
            "/dev/ttyACM0",
            "--json",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {"name": "ttyACM0", "port": 2020, "path": "/dev/ttyACM0", "speed": "115200n81"}
    ]


def test_list_filter_empty(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "LEGACY-ttyUSB1",
                    "port": 2001,
                    "path": "/dev/ttyUSB1",
                    "speed": "115200n81",
                },
                {
                    "name": "ttyACM0",
                    "port": 2020,
                    "path": "/dev/ttyACM0",
                    "speed": "115200n81",
                },
            ]
        }
    )
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "serials",
            "list",
            "--filter",
            "/dev/ttyNOTEXISTING",
            "--json",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == []


# Testing "show" subcommand
def test_show_noname(serials_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "show"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam serials show: error:" in call_result.stderr


def test_show_1(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials/ttyUSB1-9600"
    ).respond_with_json(
        {
            "name": "ttyUSB1-9600",
            "port": 2111,
            "path": "/dev/ttyUSB1",
            "speed": "9600n81",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "show", "ttyUSB1-9600"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "name : ttyUSB1-9600" in call_result.stdout
    assert "path : /dev/ttyUSB1" in call_result.stdout
    assert "port : 2111" in call_result.stdout
    assert "speed:9600n81" in call_result.stdout


def test_show_2(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials/ttymxc3-1_5M"
    ).respond_with_json(
        {
            "name": "ttymxc3-1_5M",
            "port": 2200,
            "path": "/dev/ttymxc3",
            "speed": "1500000n81",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "show", "ttymxc3-1_5M"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "name : ttymxc3-1_5M" in call_result.stdout
    assert "path : /dev/ttymxc3" in call_result.stdout
    assert "port : 2200" in call_result.stdout
    assert "speed:1500000n81" in call_result.stdout


def test_show_notexisting(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(re.compile(".*")).respond_with_json(
        {"detail": "Serial not found"}, status=404
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "show", "NOTEXISTING"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert "Error: Serial not found" in call_result.stderr


# Testing "connect" subcommand
def test_connect_noname(serials_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "connect"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam serials connect: error:" in call_result.stderr


def test_connect_notexisting(serials_config, default_appliance):
    default_appliance["httpserver"].expect_request(re.compile(".*")).respond_with_json(
        {"detail": "Serial not found"}, status=404
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "serials", "connect", "NOTEXISTING"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert "Error: Serial not found" in call_result.stderr


def test_connect_valid(ws_config, ws_appliance):
    ws_appliance.start()
    proc = subprocess.Popen(
        ["laam", "-i", "idtest", "serials", "connect", "ttymxc3"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    time.sleep(1)
    proc.send_signal(signal.SIGINT)
    proc.wait()
    stdout, stderr = proc.communicate()
    ws_appliance.stop()
    assert proc.returncode == 1
    assert (
        f"Connecting to ws://{ws_appliance.host}:{ws_appliance.port}/ws/ port 2001"
        in stdout
    )
    assert "Leaving..." in stdout
    assert stderr == ""
