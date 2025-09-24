# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import subprocess

import pytest

# Testing "usbs" command

# Sub command:
#   {list,show}  Sub command
#     list       List USB devices
#     show       USB details

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def usbs_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "list" command
def test_list_invalid():
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "list", "AAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_list_valid(usbs_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/usbs", method="GET"
    ).respond_with_json(
        {
            "items": [
                {
                    "bus": "001",
                    "device": "001",
                    "id": "1d6b:0002",
                    "tag": "Linux Foundation 2.0 root hub",
                },
                {
                    "bus": "001",
                    "device": "002",
                    "id": "0424:2916",
                    "tag": "Microchip Technology, Inc. (formerly SMSC) USB2916 Smart Hub",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert (
        "Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub"
        in call_result.stdout
    )
    assert (
        "Bus 001 Device 002: ID 0424:2916 Microchip Technology, Inc. (formerly SMSC) USB2916 Smart Hub"
        in call_result.stdout
    )


def test_list_json(usbs_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/usbs", method="GET"
    ).respond_with_json(
        {
            "items": [
                {
                    "bus": "001",
                    "device": "003",
                    "id": "0424:2840",
                    "tag": "Microchip Technology, Inc. (formerly SMSC) Hub Feature Controller",
                },
                {
                    "bus": "002",
                    "device": "001",
                    "id": "1d6b:0003",
                    "tag": "Linux Foundation 3.0 root hub",
                },
                {
                    "bus": "002",
                    "device": "002",
                    "id": "0424:5916",
                    "tag": "Microchip Technology, Inc. (formerly SMSC) USB5916 Smart Hub",
                },
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "list", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "bus": "001",
            "device": "003",
            "id": "0424:2840",
            "tag": "Microchip Technology, Inc. (formerly SMSC) Hub Feature Controller",
        },
        {
            "bus": "002",
            "device": "001",
            "id": "1d6b:0003",
            "tag": "Linux Foundation 3.0 root hub",
        },
        {
            "bus": "002",
            "device": "002",
            "id": "0424:5916",
            "tag": "Microchip Technology, Inc. (formerly SMSC) USB5916 Smart Hub",
        },
    ]


# Testing "show" command
def test_show_nobus_nodevice():
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "show"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam usbs show: error:" in call_result.stderr


def test_show_yesbus_nodevice():
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "show", "001"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam usbs show: error:" in call_result.stderr


def test_show_valid(usbs_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/usbs/001/001", method="GET"
    ).respond_with_data("USB_001_001_INFO")
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "show", "001", "001"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "USB_001_001_INFO" in call_result.stdout


def test_show_notexisting(usbs_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/usbs/001/010", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "usbs", "show", "001", "010"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"
