# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import base64
import json
import subprocess

import pytest

# Testing "laacli" command

# Sub command:
#   {button,led,power,rev,screenshot,temp,usb,usbg-ms,watt}
#                         Sub command
#     button              Virtual buttons
#     led                 User LED
#     power               Power rails
#     rev                 LAA revision
#     screenshot          OLED screenshot
#     temp                Query temperature (°C)
#     usb                 USB hub
#     usbg-ms             USB Gadget Mass storage
#     watt                Power consumption

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def laacli_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "button" subcommand
def test_button_nobutton_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli button: error:" in call_result.stderr


def test_button_yesbutton_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli button: error:" in call_result.stderr


def test_button_invalid(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/button"
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button", "3", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli button: error:" in call_result.stderr


@pytest.mark.parametrize("onoff", ["on", "off"])
@pytest.mark.parametrize("buttonValue", ["1", "2", "power", "reset"])
def test_button(laacli_config, default_appliance, buttonValue, onoff):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/button",
        method="POST",
        json={"button": buttonValue, "state": onoff},
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button", buttonValue, onoff],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_button_1_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/button", method="POST", json={"button": "1", "state": "on"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button", "1", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_button_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/button", method="POST", json={"button": "reset", "state": "off"}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "button", "reset", "off", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "led" subcommand
def test_led_noled(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "led"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli led: error:" in call_result.stderr


def test_led_invalid(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "led", "black"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli led: error:" in call_result.stderr


@pytest.mark.parametrize("ledColor", ["green", "yellow", "off"])
def test_led_green(laacli_config, default_appliance, ledColor):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/led", method="POST", json={"color": ledColor}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "led", ledColor],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_led_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/led", method="POST", json={"color": "green"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "led", "green"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_led_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/led", method="POST", json={"color": "green"}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "led", "green", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "power" subcommand
def test_power_norail_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli power: error:" in call_result.stderr


def test_power_yesrail_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power", "1v8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli power: error:" in call_result.stderr


def test_power_invalidrail(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power", "230v", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli power: error:" in call_result.stderr


@pytest.mark.parametrize("statusValue", ["on", "off", "reset"])
@pytest.mark.parametrize("railValue", ["1v8", "3v3", "5v", "12v"])
def test_power(laacli_config, default_appliance, railValue, statusValue):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/power",
        method="POST",
        json={"vbus": railValue, "state": statusValue},
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power", railValue, statusValue],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_power_1v8_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/power", method="POST", json={"vbus": "1v8", "state": "on"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power", "1v8", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_power_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/power", method="POST", json={"vbus": "12v", "state": "reset"}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "power", "12v", "reset", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "rev" subcommand
def test_rev(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/rev", method="POST"
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "rev"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_rev_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/rev", method="POST"
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "rev"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_rev_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/rev", method="POST"
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "rev", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "screenshot" subcommand
def test_screenshot_nofilename(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "screenshot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli screenshot: error:" in call_result.stderr


def test_screenshot_valid(laacli_config, default_appliance):
    assert not (laacli_config["tmp_path"] / "screenshot1.jpg").exists()
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/screenshot", method="POST"
    ).respond_with_json(
        {
            "stdout": "APPLIANCE_LOG_OK",
            "stderr": "",
            "code": 0,
            "screenshot": base64.b64encode("SCREENSHOT".encode("utf-8")).decode(
                "utf-8"
            ),
        }
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "screenshot", "screenshot1.jpg"],
        cwd=laacli_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert (laacli_config["tmp_path"] / "screenshot1.jpg").exists()
    assert (laacli_config["tmp_path"] / "screenshot1.jpg").read_text() == "SCREENSHOT"


def test_screenshot_nogood(laacli_config, default_appliance):
    assert not (laacli_config["tmp_path"] / "screenshot1.jpg").exists()
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/screenshot", method="POST"
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "screenshot", "screenshot1.jpg"],
        cwd=laacli_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_screenshot_notfound(laacli_config, default_appliance):
    assert not (laacli_config["tmp_path"] / "screenshot1.jpg").exists()
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/screenshot", method="POST"
    ).respond_with_data("File not found", status=404)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "screenshot", "screenshot1.jpg"],
        cwd=laacli_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1


# Testing "temp" subcommand
def test_temp_noprobe(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "temp"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli temp: error:" in call_result.stderr


def test_temp_invalid(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "temp", "weather"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli temp: error:" in call_result.stderr


def test_temp_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/temp", method="POST", json={"probe": "amb"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "temp", "amb"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


@pytest.mark.parametrize("tempType", ["amb", "dut", "sys"])
def test_temp_amb(laacli_config, default_appliance, tempType):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/temp", method="POST", json={"probe": tempType}
    ).respond_with_json({"stdout": "10degrees", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "temp", tempType],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "10degrees" in call_result.stdout


def test_temp_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/temp", method="POST", json={"probe": "sys"}
    ).respond_with_json({"stdout": "25degrees", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "temp", "sys", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "25degrees",
        "stderr": "",
        "code": 0,
    }


# Testing "usb" subcommand
def test_usb_noport_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usb: error:" in call_result.stderr


def test_usb_yesport_nostate(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usb: error:" in call_result.stderr


def test_usb_invalid(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb", "1", "nope"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usb: error:" in call_result.stderr


def test_usb_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usb", method="POST", json={"port": 1, "state": "on"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb", "1", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


@pytest.mark.parametrize("statusValue", ["on", "off", "reset", "start"])
@pytest.mark.parametrize("usbValue", ["1", "2", "3", "4"])
def test_usb(laacli_config, default_appliance, usbValue, statusValue):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usb",
        method="POST",
        json={"port": int(usbValue), "state": statusValue},
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb", usbValue, statusValue],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_usb_0_on_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usb", method="POST", json={"port": 0, "state": "on"}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usb", "0", "on", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "usbg-ms" subcommand
def test_usbgms_nostate_nofilename(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usbg-ms: error:" in call_result.stderr


def test_usbgms_yesstate_nofilename(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "on"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usbg-ms: error:" in call_result.stderr


def test_usbgms_invalid_status(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "nope", "file1.img"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli usbg-ms: error:" in call_result.stderr


def test_usbgms_on(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usbg-ms",
        method="POST",
        json={"state": "on", "filename": "file1.img"},
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "on", "file1.img"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_usbgms_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usbg-ms",
        method="POST",
        json={"state": "on", "filename": "file1.img"},
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "on", "file1.img"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


def test_usbgms_off(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usbg-ms", method="POST", json={"state": "off", "filename": ""}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "off"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_usbgms_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/usbg-ms",
        method="POST",
        json={"state": "on", "filename": "file1.img"},
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "usbg-ms", "on", "file1.img", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }


# Testing "watt" subcommand
def test_watt_norail(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "watt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli watt: error:" in call_result.stderr


def test_watt_invalid(laacli_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "watt", "240v"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam laacli watt: error:" in call_result.stderr


def test_watt_nogood(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/watt", method="POST", json={"vbus": "1v8"}
    ).respond_with_json({"stdout": "", "stderr": "APPLIANCE_LOG_KO", "code": 1})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "watt", "1v8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "APPLIANCE_LOG_KO" in call_result.stderr


@pytest.mark.parametrize("rail", ["1v8", "3v3", "5v", "12v"])
def test_watt_1v8(laacli_config, default_appliance, rail):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/watt", method="POST", json={"vbus": rail}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "watt", rail],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "APPLIANCE_LOG_OK" in call_result.stdout


def test_watt_json(laacli_config, default_appliance):
    default_appliance["httpserver"].expect_request(
        "/api/v1/laacli/watt", method="POST", json={"vbus": "5v"}
    ).respond_with_json({"stdout": "APPLIANCE_LOG_OK", "stderr": "", "code": 0})
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "laacli", "watt", "5v", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert json.loads(call_result.stdout) == {
        "stdout": "APPLIANCE_LOG_OK",
        "stderr": "",
        "code": 0,
    }
