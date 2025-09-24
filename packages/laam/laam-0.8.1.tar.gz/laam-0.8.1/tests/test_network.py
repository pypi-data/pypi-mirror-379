# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import subprocess

import pytest

# Testing "network" command

# Sub command:
#   {addresses,hostname,interfaces,routes,settings}
#                         Sub command
#     addresses           List addresses
#     hostname            Hostname
#     interfaces          List interfaces
#     routes              List routes
#     settings            Settings

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def network_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "addresses" command
def test_addresses(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/addresses", method="GET"
    ).respond_with_json(
        {"ADDRESS1": [{"flags": "FLAG1", "ip": "IPADDRESS1", "prefix": "PREFIX1"}]}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "addresses"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Addresses:" in call_result.stdout
    assert "ADDRESS1" in call_result.stdout
    assert "FLAG1" in call_result.stdout
    assert "IPADDRESS1" in call_result.stdout
    assert "PREFIX1" in call_result.stdout


def test_addresses_nogood(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/addresses", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "addresses"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"


def test_addresses_json(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/addresses", method="GET"
    ).respond_with_json(
        {"ADDRESS1": [{"flags": "FLAG1", "ip": "IPADDRESS1", "prefix": "PREFIX1"}]}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "addresses", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "ADDRESS1": [{"flags": "FLAG1", "ip": "IPADDRESS1", "prefix": "PREFIX1"}]
    }


# Testing "hostname" command
def test_hostname(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/hostname", method="GET"
    ).respond_with_json({"hostname": "LAA_HOSTNAME1"})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "hostname"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "LAA_HOSTNAME1" in call_result.stdout


def test_hostname_nogood(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/hostname", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "hostname"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"


# Testing "interfaces" command
def test_interfaces(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/interfaces", method="GET"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "INTERFACE1_NAME",
                    "type": "INTERFACE1_TYPE",
                    "status": "INTERFACE1_STATUS",
                    "mac": "INTERFACE1_MAC",
                }
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "interfaces"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Interfaces:" in call_result.stdout
    assert "INTERFACE1_NAME" in call_result.stdout
    assert "INTERFACE1_TYPE" in call_result.stdout
    assert "INTERFACE1_STATUS" in call_result.stdout
    assert "INTERFACE1_MAC" in call_result.stdout


def test_interfaces_nogood(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/interfaces", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "interfaces"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"


def test_interfaces_json(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/interfaces", method="GET"
    ).respond_with_json(
        {
            "items": [
                {
                    "name": "INTERFACE1_NAME",
                    "type": "INTERFACE1_TYPE",
                    "status": "INTERFACE1_STATUS",
                    "mac": "INTERFACE1_MAC",
                }
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "interfaces", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {
            "name": "INTERFACE1_NAME",
            "type": "INTERFACE1_TYPE",
            "status": "INTERFACE1_STATUS",
            "mac": "INTERFACE1_MAC",
        }
    ]


# Testing "routes" command
def test_routes(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/routes", method="GET"
    ).respond_with_json(
        {
            "ROUTE1": [
                {
                    "src": "SRC1",
                    "dst": "DST1",
                    "via": "VIA1",
                    "type": "TYPE1",
                    "protocol": "PROTOCOL1",
                    "dst_prefix": "DST_PREFIX1",
                }
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "routes"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Routes:" in call_result.stdout
    assert "ROUTE1" in call_result.stdout
    assert "SRC1" in call_result.stdout
    assert "DST1" in call_result.stdout
    assert "VIA1" in call_result.stdout
    assert "TYPE1" in call_result.stdout
    assert "PROTOCOL1" in call_result.stdout
    assert "DST_PREFIX1" in call_result.stdout


def test_routes_nogood(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/routes", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "routes"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"


def test_routes_json(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/routes", method="GET"
    ).respond_with_json(
        {
            "ROUTE1": [
                {
                    "src": "SRC1",
                    "dst": "DST1",
                    "via": "VIA1",
                    "type": "TYPE1",
                    "protocol": "PROTOCOL1",
                    "dst_prefix": "DST_PREFIX1",
                }
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "routes", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "ROUTE1": [
            {
                "src": "SRC1",
                "dst": "DST1",
                "via": "VIA1",
                "type": "TYPE1",
                "protocol": "PROTOCOL1",
                "dst_prefix": "DST_PREFIX1",
            }
        ]
    }


# Testing "settings" command
def test_settings(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/settings", method="GET"
    ).respond_with_data("SETTINGS1")
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "settings"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "SETTINGS1" in call_result.stdout


def test_settings_nogood(network_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/network/settings", method="GET"
    ).respond_with_data("Internal Server Error", status=500)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "network", "settings"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 500\n"
