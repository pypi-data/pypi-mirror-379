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
#   {list,logs}  Sub command
#     list       List services
#     logs       Services logs

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def services_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "list" command
def test_list_invalid(services_config, default_appliance):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "list", "AAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_list_1(services_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services", method="GET"
    ).respond_with_json(
        {
            "items": [
                {"name": "apache2", "status": "running"},
                {"name": "avahi-daemon", "status": "running"},
                {"name": "baklaweb", "status": "running"},
                {"name": "baklaweb-bakfleet", "status": "running"},
                {"name": "baklaweb-webtelnet", "status": "running"},
                {"name": "chronyd", "status": "running"},
                {"name": "dnsmasq", "status": "running"},
                {"name": "docker", "status": "running"},
                {"name": "kea-dhcp4", "status": "running"},
                {"name": "lava-dispatcher-host", "status": "running"},
                {"name": "lsibd", "status": "running"},
                {"name": "nfs-server", "status": "running"},
                {"name": "ser2net", "status": "running"},
                {"name": "sshd.socket", "status": "running"},
                {"name": "systemd-networkd", "status": "running"},
                {"name": "tftpd-hpa.socket", "status": "running"},
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "apache2: running" in call_result.stdout
    assert "avahi-daemon: running" in call_result.stdout
    assert "baklaweb: running" in call_result.stdout
    assert "baklaweb-bakfleet: running" in call_result.stdout
    assert "baklaweb-webtelnet: running" in call_result.stdout
    assert "chronyd: running" in call_result.stdout
    assert "dnsmasq: running" in call_result.stdout
    assert "docker: running" in call_result.stdout
    assert "kea-dhcp4: running" in call_result.stdout
    assert "lava-dispatcher-host: running" in call_result.stdout
    assert "lsibd: running" in call_result.stdout
    assert "nfs-server: running" in call_result.stdout
    assert "ser2net: running" in call_result.stdout
    assert "sshd.socket: running" in call_result.stdout
    assert "systemd-networkd: running" in call_result.stdout
    assert "tftpd-hpa.socket: running" in call_result.stdout


def test_list_2(services_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services", method="GET"
    ).respond_with_json(
        {
            "items": [
                {"name": "apache2", "status": "dead"},
                {"name": "avahi-daemon", "status": "dead"},
                {"name": "baklaweb", "status": "dead"},
                {"name": "baklaweb-bakfleet", "status": "dead"},
                {"name": "baklaweb-webtelnet", "status": "dead"},
                {"name": "chronyd", "status": "dead"},
                {"name": "dnsmasq", "status": "dead"},
                {"name": "docker", "status": "dead"},
                {"name": "kea-dhcp4", "status": "dead"},
                {"name": "lava-dispatcher-host", "status": "dead"},
                {"name": "lsibd", "status": "dead"},
                {"name": "nfs-server", "status": "dead"},
                {"name": "ser2net", "status": "dead"},
                {"name": "sshd.socket", "status": "dead"},
                {"name": "systemd-networkd", "status": "dead"},
                {"name": "tftpd-hpa.socket", "status": "dead"},
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "apache2: dead" in call_result.stdout
    assert "avahi-daemon: dead" in call_result.stdout
    assert "baklaweb: dead" in call_result.stdout
    assert "baklaweb-bakfleet: dead" in call_result.stdout
    assert "baklaweb-webtelnet: dead" in call_result.stdout
    assert "chronyd: dead" in call_result.stdout
    assert "dnsmasq: dead" in call_result.stdout
    assert "docker: dead" in call_result.stdout
    assert "kea-dhcp4: dead" in call_result.stdout
    assert "lava-dispatcher-host: dead" in call_result.stdout
    assert "lsibd: dead" in call_result.stdout
    assert "nfs-server: dead" in call_result.stdout
    assert "ser2net: dead" in call_result.stdout
    assert "sshd.socket: dead" in call_result.stdout
    assert "systemd-networkd: dead" in call_result.stdout
    assert "tftpd-hpa.socket: dead" in call_result.stdout


def test_list_json(services_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services", method="GET"
    ).respond_with_json(
        {
            "items": [
                {"name": "apache2", "status": "running"},
                {"name": "avahi-daemon", "status": "running"},
                {"name": "baklaweb", "status": "running"},
                {"name": "baklaweb-bakfleet", "status": "running"},
                {"name": "baklaweb-webtelnet", "status": "running"},
                {"name": "chronyd", "status": "running"},
                {"name": "dnsmasq", "status": "running"},
                {"name": "docker", "status": "running"},
                {"name": "kea-dhcp4", "status": "running"},
                {"name": "lava-dispatcher-host", "status": "running"},
                {"name": "lsibd", "status": "running"},
                {"name": "nfs-server", "status": "running"},
                {"name": "ser2net", "status": "running"},
                {"name": "sshd.socket", "status": "running"},
                {"name": "systemd-networkd", "status": "running"},
                {"name": "tftpd-hpa.socket", "status": "running"},
            ]
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "list", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == [
        {"name": "apache2", "status": "running"},
        {"name": "avahi-daemon", "status": "running"},
        {"name": "baklaweb", "status": "running"},
        {"name": "baklaweb-bakfleet", "status": "running"},
        {"name": "baklaweb-webtelnet", "status": "running"},
        {"name": "chronyd", "status": "running"},
        {"name": "dnsmasq", "status": "running"},
        {"name": "docker", "status": "running"},
        {"name": "kea-dhcp4", "status": "running"},
        {"name": "lava-dispatcher-host", "status": "running"},
        {"name": "lsibd", "status": "running"},
        {"name": "nfs-server", "status": "running"},
        {"name": "ser2net", "status": "running"},
        {"name": "sshd.socket", "status": "running"},
        {"name": "systemd-networkd", "status": "running"},
        {"name": "tftpd-hpa.socket", "status": "running"},
    ]


# Testing "logs" command
def test_logs_noname(services_config, default_appliance):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "logs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam services logs: error:" in call_result.stderr


def test_logs_1(services_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services/apache2/logs", method="GET"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-12T14:25:58Z",
                "dt_iso": "2025-08-12T14:25:58+00:00",
                "logger": "172.16.31.22",
                "message": "GET /api/v1/services HTTP/1.1  200 760  -   laam vX.Y ",
                "priority": 6,
            },
            {
                "dt": "2025-08-12T14:27:30Z",
                "dt_iso": "2025-08-12T14:27:30+00:00",
                "logger": "172.16.31.22",
                "message": "GET /api/v1/services/apache2/logs HTTP/1.1  200 19344  -   laam vX.Y ",
                "priority": 6,
            },
            {
                "dt": "2025-08-12T14:28:34Z",
                "dt_iso": "2025-08-12T14:28:34+00:00",
                "logger": "172.16.31.22",
                "message": "GET /api/v1/services/apache2/logs HTTP/1.1  200 19540  -   laam vX.Y ",
                "priority": 6,
            },
        ]
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "logs", "apache2"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert (
        "2025-08-12T14:25:58+00:00 [172.16.31.22] GET /api/v1/services HTTP/1.1  200 760  -   laam vX.Y"
        in call_result.stdout
    )
    assert (
        "2025-08-12T14:27:30+00:00 [172.16.31.22] GET /api/v1/services/apache2/logs HTTP/1.1  200 19344  -   laam vX.Y"
        in call_result.stdout
    )
    assert (
        "2025-08-12T14:28:34+00:00 [172.16.31.22] GET /api/v1/services/apache2/logs HTTP/1.1  200 19540  -   laam vX.Y"
        in call_result.stdout
    )


def test_logs_2(services_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/services/lsibd/logs", method="GET"
    ).respond_with_json(
        [
            {
                "dt": "2025-08-12T14:05:35.243Z",
                "dt_iso": "2025-08-12T14:05:35+00:00",
                "logger": "lsibd",
                "message": "WD Ping",
                "priority": "6",
                "pid": "560",
            },
            {
                "dt": "2025-08-12T14:05:35.243Z",
                "dt_iso": "2025-08-12T14:05:35+00:00",
                "logger": "lsibd",
                "message": "WD Ping",
                "priority": "6",
                "pid": "560",
            },
            {
                "dt": "2025-08-12T14:05:35.243Z",
                "dt_iso": "2025-08-12T14:05:35+00:00",
                "logger": "lsibd",
                "message": "WD Ping",
                "priority": "6",
                "pid": "560",
            },
            {
                "dt": "2025-08-12T14:05:35.243Z",
                "dt_iso": "2025-08-12T14:05:35+00:00",
                "logger": "lsibd",
                "message": "WD Ping",
                "priority": "6",
                "pid": "560",
            },
        ]
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "services", "logs", "lsibd"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "2025-08-12T14:05:35+00:00 [560] [lsibd] WD Ping" in call_result.stdout
    assert "2025-08-12T14:05:35+00:00 [560] [lsibd] WD Ping" in call_result.stdout
    assert "2025-08-12T14:05:35+00:00 [560] [lsibd] WD Ping" in call_result.stdout
