# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import re
import subprocess

import pytest

# Testing "files" command

# Sub command:
#   {list,pull,push,rm}  Sub command
#     list               List files
#     pull               Pull a file
#     push               Push a file
#     rm                 Remove a file

# The following are fixtures in the conftest.py file
# - default_config
# - default_appliance


@pytest.fixture
def files_config(default_appliance, default_config):
    (default_config["tmp_path"] / "laam.yaml").write_text(
        f"idtest:\n  token: tokentest\n  uri: {default_appliance['base_url']}"
    )
    return default_config


# Testing "list" subcommand
def test_list_invalid(default_appliance, files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "list", "AAA"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 2
    assert "laam: error:" in call_result.stderr


def test_list_valid_1(default_appliance, files_config):
    default_appliance["httpserver"].expect_request("/api/v1/files").respond_with_json(
        {"items": ["file1"]}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Files:" in call_result.stdout
    assert "file1" in call_result.stdout
    assert "file2" not in call_result.stdout


def test_list_valid_2(default_appliance, files_config):
    default_appliance["httpserver"].expect_request("/api/v1/files").respond_with_json(
        {"items": ["file2"]}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Files:" in call_result.stdout
    assert "file1" not in call_result.stdout
    assert "file2" in call_result.stdout


def test_list_empty(default_appliance, files_config):
    default_appliance["httpserver"].expect_request("/api/v1/files").respond_with_json(
        {"items": []}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Files:" in call_result.stdout
    assert "file1" not in call_result.stdout
    assert "file2" not in call_result.stdout


def test_list_all(default_appliance, files_config):
    default_appliance["httpserver"].expect_request("/api/v1/files").respond_with_json(
        {"items": ["file1", "file2"]}
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "Files:" in call_result.stdout
    assert "file1" in call_result.stdout
    assert "file2" in call_result.stdout


# Testing "pull" subcommand
def test_pull_noname_nofile(files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam files pull: error:" in call_result.stderr


def test_pull_yesname_nofile(files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull", "name1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam files pull: error:" in call_result.stderr


def test_pull_valid(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(
        "/api/v1/files/name1"
    ).respond_with_data(
        "CONTENT_APPLIANCE_FILE_1", content_type="text/plain", status=200
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull", "name1", "file1"],
        cwd=files_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "." in call_result.stdout
    assert (files_config["tmp_path"] / "file1").exists()
    assert (
        files_config["tmp_path"] / "file1"
    ).read_text() == "CONTENT_APPLIANCE_FILE_1"


def test_pull_notexistingname(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(re.compile(".*")).respond_with_data(
        "File not found", status=404
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull", "nameNotExisting", "file1"],
        cwd=files_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stdout == ""
    assert call_result.stderr == "Unable to call the appliance API\nCode: 404\n"
    assert not (files_config["tmp_path"] / "file1").exists()


def test_pull_nooverwritefile(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(
        "/api/v1/files/name1"
    ).respond_with_data(
        "CONTENT_APPLIANCE_FILE_1", content_type="text/plain", status=200
    )
    (files_config["tmp_path"] / "file1").write_text("CONTENT_ORIGINAL_LOCAL_FILE_1")
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull", "name1", "file1"],
        cwd=files_config["tmp_path"],
        input="n",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert "Not overwriting the file, exiting" in call_result.stderr
    assert (files_config["tmp_path"] / "file1").exists()
    assert (
        files_config["tmp_path"] / "file1"
    ).read_text() == "CONTENT_ORIGINAL_LOCAL_FILE_1"


def test_pull_overwritefile(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(
        "/api/v1/files/name1"
    ).respond_with_data(
        "CONTENT_APPLIANCE_FILE_1", content_type="text/plain", status=200
    )
    (files_config["tmp_path"] / "file1").write_text("CONTENT_ORIGINAL_LOCAL_FILE_1")
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "pull", "name1", "file1"],
        cwd=files_config["tmp_path"],
        input="y",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert "The file will be overwritten" in call_result.stdout
    assert (files_config["tmp_path"] / "file1").exists()
    assert (
        files_config["tmp_path"] / "file1"
    ).read_text() == "CONTENT_APPLIANCE_FILE_1"


# Testing "push" subcommand
def test_push_nofile_noname(default_appliance, files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "push"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam files push: error:" in call_result.stderr


def test_push_yesfile_noname(files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "push", "file1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam files push: error:" in call_result.stderr


def test_push_valid(default_appliance, files_config):
    (files_config["tmp_path"] / "file1").write_text("CONTENT_ORIGINAL_LOCAL_FILE_1")
    default_appliance["httpserver"].expect_request(
        "/api/v1/files/name1"
    ).respond_with_data(status=200)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "push", "file1", "name1"],
        cwd=files_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert call_result.stdout == ""
    assert (files_config["tmp_path"] / "file1").exists()
    assert (
        files_config["tmp_path"] / "file1"
    ).read_text() == "CONTENT_ORIGINAL_LOCAL_FILE_1"


def test_push_notexistingfile(default_appliance, files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "push", "file1", "name1"],
        cwd=files_config["tmp_path"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "No such file or directory" in call_result.stderr
    assert not (files_config["tmp_path"] / "file1").exists()


# Testing "rm subcommand
def test_rm_noname(default_appliance, files_config):
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "rm"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam files rm: error:" in call_result.stderr


def test_rm_valid(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(
        "/api/v1/files/name1"
    ).respond_with_data(status=204)
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "rm", "name1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 0
    assert call_result.stdout == ""


def test_rm_notexistingname(default_appliance, files_config):
    default_appliance["httpserver"].expect_request(re.compile(".*")).respond_with_data(
        "File not found", status=404
    )
    call_result = subprocess.run(
        ["laam", "-i", "idtest", "files", "rm", "name1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    default_appliance["httpserver"].check_assertions()
    assert call_result.returncode == 1
    assert call_result.stderr == "Unable to call the appliance API\nCode: 404\n"
