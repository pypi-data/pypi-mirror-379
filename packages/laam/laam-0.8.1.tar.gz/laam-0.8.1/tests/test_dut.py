# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import subprocess

import pytest

from tests.mock_appliance_ws import MockApplianceWs

# Testing "dut" command

# Sub command:
#   {check,new,render,test}
#                         Sub command
#     check               Check the configuration
#     new                 Create a device configuration file
#     render              Render device-type template and device dict
#     test                Boot test the DUT

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def dut_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


@pytest.fixture
def device_config(dut_config):
    subprocess.run(
        ["laam", "dut", "new", "device_config"],
        input="device_config",
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return {
        "filename": "device_config",
        "filename_dt": "device_config.dt",
        "filename_dd": "device_config.dd",
    }


@pytest.fixture
def ws_appliance():
    return MockApplianceWs()


@pytest.fixture
def ws_config(dut_config, ws_appliance):
    subprocess.run(
        ["laam", "identities", "update", "idtest", "--uri", ws_appliance.base_url]
    )
    return dut_config


# Testing "check" subcommand
def test_check_noconfig(dut_config):
    call_result = subprocess.run(
        ["laam", "dut", "check"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut check: error:" in call_result.stderr


def test_check_notexistingconfig(dut_config):
    call_result = subprocess.run(
        ["laam", "dut", "check", "config1"],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "No such file or directory" in call_result.stderr


def test_check_valid(dut_config, device_config):
    call_result = subprocess.run(
        ["laam", "dut", "check", device_config["filename"]],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert call_result.stdout == ""


def test_check_valid_withid(dut_config, device_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "dut", "check", device_config["filename"]],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert call_result.stdout == ""


def test_check_invalidyaml(dut_config):
    (dut_config["tmp_path"] / "config1").write_text("INVALID_YAML")
    call_result = subprocess.run(
        ["laam", "dut", "check", "config1"],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert "Invalid configuration" in call_result.stderr


# Testing "new" subcommand
def test_new_noconfig(dut_config):
    call_result = subprocess.run(
        ["laam", "dut", "new"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut new: error:" in call_result.stderr


def test_new_valid(dut_config):
    assert not (dut_config["tmp_path"] / "config1").exists()
    call_result = subprocess.run(
        ["laam", "dut", "new", "config1"],
        input="config1_dtb",
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "dtb name>" in call_result.stdout
    assert (dut_config["tmp_path"] / "config1").exists()
    assert (
        dut_config["tmp_path"] / "config1"
    ).read_text() == "bootloader: u-boot\ninterrupt: true\nname: config1_dtb\npower:\n  'off': []\n  'on': []\n  reset: []\nprompt: '=> '\nserial: ttymxc3\n"


# Testing "render" subcommand
def test_render_noconfig_nodt_nodd(dut_config):
    call_result = subprocess.run(
        ["laam", "dut", "render"],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut render: error:" in call_result.stderr


def test_render_yesconfig_nodt_nodd(dut_config, device_config):
    call_result = subprocess.run(
        ["laam", "dut", "render", device_config["filename"]],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut render: error:" in call_result.stderr


def test_render_yesconfig_yesdt_nodd(dut_config, device_config):
    call_result = subprocess.run(
        [
            "laam",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
        ],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut render: error:" in call_result.stderr


def test_render_valid(dut_config, device_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials/ttymxc3"
    ).respond_with_json({"port": 2001})
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert (dut_config["tmp_path"] / device_config["filename"]).exists()
    assert (
        dut_config["tmp_path"] / device_config["filename"]
    ).read_text() == "bootloader: u-boot\ninterrupt: true\nname: device_config\npower:\n  'off': []\n  'on': []\n  reset: []\nprompt: '=> '\nserial: ttymxc3\n"
    assert (dut_config["tmp_path"] / device_config["filename_dt"]).exists()
    assert (
        dut_config["tmp_path"] / device_config["filename_dt"]
    ).read_text() == "{% extends 'base-uboot.jinja2' %}\n\n{% set uboot_needs_interrupt = uboot_needs_interrupt | default(True) %}\n{% set bootloader_prompt = bootloader_prompt | default('=> ') %}\n"
    assert (dut_config["tmp_path"] / device_config["filename_dd"]).exists()
    assert (
        dut_config["tmp_path"] / device_config["filename_dd"]
    ).read_text() == "{% extends 'device_config.jinja2' %}\n\n{% set hard_reset_command = [\n    ''\n] %}\n{% set power_off_command = [\n    ''\n] %}\n{% set power_on_command =  [\n    ''\n] %}\n\n{% set connection_command = 'telnet localhost 2001' %}\n\n{% set usbg_ms_commands = {\n    'disable': ['laacli', 'usbg-ms', 'off'],\n    'enable': ['laacli', 'usbg-ms', 'on', '{IMAGE}']\n} %}\n{% set docker_shell_extra_arguments = [\n    '--add-host=lava-worker.internal:host-gateway',\n    '--volume=/usr/bin/laacli:/usr/bin/laacli:ro',\n    '--volume=/usr/bin/lsibcli:/usr/bin/lsibcli:ro',\n    '--volume=/run/dbus/system_bus_socket:/run/dbus/system_bus_socket:rw'\n] %}\n"


def test_render_notexistingconfig(ws_config, device_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/devices/serials/ttymxc3"
    ).respond_with_json({"port": 2001})
    assert not (ws_config["tmp_path"] / "config1").exists()
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            "config1",
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "No such file or directory:" in call_result.stderr


# Testing "test" subcommand
def test_test_noconfig(dut_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "dut", "test"],
        cwd=dut_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam dut test: error:" in call_result.stderr


def test_test_valid(ws_config, device_config, ws_appliance):
    ws_appliance.start()
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "dut", "test", device_config["filename"]],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert "Times the test managed to run: 1 out of 1" in call_result.stdout
    assert "Times USB test passed: 1 out of 1" in call_result.stdout
    assert "Times Network test passed: 1 out of 1" in call_result.stdout
    assert call_result.returncode == 0


def test_test_valid_repeat5(ws_config, device_config, ws_appliance):
    ws_appliance.start()
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "test",
            device_config["filename"],
            "--repeat",
            "5",
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert "Times the test managed to run: 5 out of 5" in call_result.stdout
    assert "Times USB test passed: 5 out of 5" in call_result.stdout
    assert "Times Network test passed: 5 out of 5" in call_result.stdout
    assert call_result.returncode == 0


def test_test_no_ethernet(ws_config, device_config, ws_appliance):
    ws_appliance.start(status="no_ethernet")
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "dut", "test", device_config["filename"]],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert "Times the test managed to run: 1 out of 1" in call_result.stdout
    assert "Times USB test passed: 1 out of 1" in call_result.stdout
    assert "Times Network test passed: 0 out of 1" in call_result.stdout
    assert call_result.returncode == 0


def test_test_no_usb(ws_config, device_config, ws_appliance):
    ws_appliance.start(status="no_usb")
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "dut", "test", device_config["filename"]],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert "Times the test managed to run: 1 out of 1" in call_result.stdout
    assert "Times USB test passed: 0 out of 1" in call_result.stdout
    assert "Times Network test passed: 1 out of 1" in call_result.stdout
    assert call_result.returncode == 0


def test_test_usbg_ms_notexisting(ws_config, device_config, ws_appliance):
    ws_appliance.start()
    assert not (ws_config["tmp_path"] / "file.img").exists()
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "test",
            device_config["filename"],
            "--usbg-ms",
            "file.img",
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert call_result.returncode == 2
    assert "No such file or directory:" in call_result.stderr


def test_test_usbg_ms(ws_config, device_config, ws_appliance):
    ws_appliance.start()
    (ws_config["tmp_path"] / "file.img").write_text("CONTENT_IMAGE_FILE_1")
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "render",
            device_config["filename"],
            device_config["filename_dt"],
            device_config["filename_dd"],
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    call_result = subprocess.run(
        [
            "laam",
            "-i",
            "idtest",
            "dut",
            "test",
            device_config["filename"],
            "--usbg-ms",
            "file.img",
        ],
        cwd=ws_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    ws_appliance.stop()
    assert "Times the test managed to run: 1 out of 1" in call_result.stdout
    assert "Times USB test passed: 1 out of 1" in call_result.stdout
    assert "Times Network test passed: 1 out of 1" in call_result.stdout
    assert call_result.returncode == 0
