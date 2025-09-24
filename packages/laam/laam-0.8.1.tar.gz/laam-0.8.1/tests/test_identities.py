# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import subprocess

from laam.commands import identities

# Testing "identities" command

# Sub command:
#   {add,update,delete,list,show}
#                         Sub command
#     add                 add an identity
#     update              update an identity
#     delete              delete an identity
#     list                list available identities
#     show                show identity details

# "default_config" is a fixture in the conftest.py file


# Testing "add" subcommand
def test_add_no_uri_no_token():
    call_result = subprocess.run(
        ["laam", "identities", "add", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam identities add: error:" in call_result.stderr


def test_add_no_uri_yes_token():
    call_result = subprocess.run(
        ["laam", "identities", "add", "idtest", "--token", "tokentest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam identities add: error:" in call_result.stderr


def test_add_yes_uri_no_token():
    call_result = subprocess.run(
        ["laam", "identities", "add", "idtest", "--uri", "uritest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam identities add: error:" in call_result.stderr


def test_add_yes_uri_yes_token(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert call_result.stderr == ""
    assert identities._load_configuration() == {
        "idtest": {"token": "tokentest", "uri": "uritest"}
    }


# Testing "delete" subcommand
def test_delete_no_id():
    call_result = subprocess.run(
        ["laam", "identities", "delete"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert call_result.stdout == ""
    assert "laam identities delete: error:" in call_result.stderr


def test_delete_not_existing_id(default_config):
    call_result = subprocess.run(
        ["laam", "identities", "delete", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert call_result.stdout == ""
    assert "Unknown identity 'idtest'" in call_result.stderr


def test_delete_existing_id(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest1",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest2",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "idtest1" in call_result.stdout
    assert "idtest2" in call_result.stdout

    call_result = subprocess.run(["laam", "identities", "delete", "idtest1"])
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "idtest1" not in call_result.stdout
    assert "idtest2" in call_result.stdout
    assert identities._load_configuration() == {
        "idtest2": {"token": "tokentest", "uri": "uritest"}
    }


# Testing "list" subcommand


def test_list_empty(default_config):
    call_result = subprocess.run(
        ["laam", "identities", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "" in call_result.stdout


def test_list_one_id(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtestX",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0
    assert (default_config["tmp_path"] / "laam.yaml").exists()

    call_result = subprocess.run(
        ["laam", "identities", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "idtestX" in call_result.stdout


def test_list_two_ids(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest1",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest2",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0
    assert (default_config["tmp_path"] / "laam.yaml").exists()

    call_result = subprocess.run(
        ["laam", "identities", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "idtestX" not in call_result.stdout
    assert "idtest1" in call_result.stdout
    assert "idtest2" in call_result.stdout


# Testing "show" subcommand


def test_show_no_id():
    call_result = subprocess.run(
        ["laam", "identities", "show"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam identities show: error:" in call_result.stderr


def test_show_not_existing_id(default_config):
    call_result = subprocess.run(
        ["laam", "identities", "show", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert "Unknown identity 'idtest'" in call_result.stderr


def test_show_existing_id(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest",
            "--uri",
            "uritest",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "show", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "tokentest" in call_result.stdout
    assert "uritest" in call_result.stdout


# Testing "update" subcommand


def test_update_no_id():
    call_result = subprocess.run(
        ["laam", "identities", "update"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 2
    assert "laam identities update: error:" in call_result.stderr


def test_update_not_existing_id(default_config):
    call_result = subprocess.run(
        ["laam", "identities", "update", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 1
    assert "Unknown identity 'idtest'" in call_result.stderr


def test_update_only_token(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest",
            "--uri",
            "uritest",
            "--token",
            "tokentest1",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "update", "idtest", "--token", "tokentest2"]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "show", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "tokentest1" not in call_result.stdout
    assert "tokentest2" in call_result.stdout
    assert "uritest" in call_result.stdout
    assert identities._load_configuration() == {
        "idtest": {"token": "tokentest2", "uri": "uritest"}
    }


def test_update_only_uri(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest",
            "--uri",
            "uritest1",
            "--token",
            "tokentest",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "update", "idtest", "--uri", "uritest2"]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "show", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "uritest1" not in call_result.stdout
    assert "tokentest" in call_result.stdout
    assert "uritest2" in call_result.stdout
    assert identities._load_configuration() == {
        "idtest": {"token": "tokentest", "uri": "uritest2"}
    }


def test_update_token_uri(default_config):
    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "add",
            "idtest",
            "--uri",
            "uritest1",
            "--token",
            "tokentest1",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        [
            "laam",
            "identities",
            "update",
            "idtest",
            "--uri",
            "uritest2",
            "--token",
            "tokentest2",
        ]
    )
    assert call_result.returncode == 0

    call_result = subprocess.run(
        ["laam", "identities", "show", "idtest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert call_result.returncode == 0
    assert "uritest1" not in call_result.stdout
    assert "tokentest1" not in call_result.stdout
    assert "tokentest2" in call_result.stdout
    assert "uritest2" in call_result.stdout
    assert identities._load_configuration() == {
        "idtest": {"token": "tokentest2", "uri": "uritest2"}
    }
