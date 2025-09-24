# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import subprocess

import pytest

# Sub command:
#   {logs,fleet,version}  Sub command
#     logs                Appliance logs
#     fleet               Bakfleet Information
#     version             Appliance Version


# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def system_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "logs" command
def test_logs_invalid(system_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "logs", "AAAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_logs_valid(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services/appliance/logs", method="GET"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-12T15:28:29.181Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "systemd",
                "message": "Starting Time & Date Service...",
                "priority": "6",
                "pid": "1",
            },
            {
                "dt": "2025-08-12T15:28:29.337Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "dbus-daemon",
                "message": "[system] Successfully activated service 'org.freedesktop.timedate1'",
                "priority": "6",
                "pid": "554",
            },
            {
                "dt": "2025-08-12T15:28:29.337Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "systemd",
                "message": "Started Time & Date Service.",
                "priority": "6",
                "pid": "1",
            },
        ]
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "logs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert (
        "2025-08-12T15:28:29+00:00 [1] [systemd] Starting Time & Date Service..."
        in call_result.stdout
    )
    assert (
        "2025-08-12T15:28:29+00:00 [554] [dbus-daemon] [system] Successfully activated service 'org.freedesktop.timedate1'"
        in call_result.stdout
    )
    assert (
        "2025-08-12T15:28:29+00:00 [1] [systemd] Started Time & Date Service."
        in call_result.stdout
    )


def test_logs_json(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services/appliance/logs", method="GET"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-12T15:28:29.181Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "systemd",
                "message": "Starting Time & Date Service...",
                "priority": "6",
                "pid": "1",
            },
            {
                "dt": "2025-08-12T15:28:29.337Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "dbus-daemon",
                "message": "[system] Successfully activated service 'org.freedesktop.timedate1'",
                "priority": "6",
                "pid": "554",
            },
            {
                "dt": "2025-08-12T15:28:29.337Z",
                "dt_iso": "2025-08-12T15:28:29+00:00",
                "logger": "systemd",
                "message": "Started Time & Date Service.",
                "priority": "6",
                "pid": "1",
            },
        ]
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "logs", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "dt": "2025-08-12T15:28:29.181Z",
            "dt_iso": "2025-08-12T15:28:29+00:00",
            "logger": "systemd",
            "message": "Starting Time & Date Service...",
            "priority": "6",
            "pid": "1",
        },
        {
            "dt": "2025-08-12T15:28:29.337Z",
            "dt_iso": "2025-08-12T15:28:29+00:00",
            "logger": "dbus-daemon",
            "message": "[system] Successfully activated service 'org.freedesktop.timedate1'",
            "priority": "6",
            "pid": "554",
        },
        {
            "dt": "2025-08-12T15:28:29.337Z",
            "dt_iso": "2025-08-12T15:28:29+00:00",
            "logger": "systemd",
            "message": "Started Time & Date Service.",
            "priority": "6",
            "pid": "1",
        },
    ]


# Testing "fleet" command
def test_fleet_invalid(system_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "fleet", "AAAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_fleet_valid(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/system/fleet", method="GET"
    ).respond_with_json(
        {
            "token": "abcdefgh-ilmn-opqr-stuvz-01234567890",
            "online": True,
            "serial": "99999",
            "organization": "xyz",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "fleet"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Fleet:" in call_result.stdout
    assert "serial: 99999" in call_result.stdout
    assert "org   : xyz" in call_result.stdout
    assert "online: True" in call_result.stdout
    assert "token : abcdefgh-ilmn-opqr-stuvz-01234567890" in call_result.stdout


def test_fleet_json(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/system/fleet", method="GET"
    ).respond_with_json(
        {
            "token": "abcdefgh-ilmn-opqr-stuvz-01234567890",
            "online": True,
            "serial": "99999",
            "organization": "xyz",
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "fleet", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "token": "abcdefgh-ilmn-opqr-stuvz-01234567890",
        "online": True,
        "serial": "99999",
        "organization": "xyz",
    }


# Testing "version" command
def test_version_invalid(system_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "version", "AAAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_version_valid(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/system/version", method="GET"
    ).respond_with_json({"version": "X.Y.Z"})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert call_result.stdout == "X.Y.Z\n"


def test_version_json(system_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/system/version", method="GET"
    ).respond_with_json({"version": "X.Y.Z"})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "system", "version", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {"version": "X.Y.Z"}
