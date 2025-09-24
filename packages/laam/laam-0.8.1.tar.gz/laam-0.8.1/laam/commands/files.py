# vim: set ts=4
#
# Copyright 2025-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import argparse
import json
import os
import pathlib
import sys

from requests_toolbelt.multipart.encoder import MultipartEncoder

from laam.utils import print_error


def configure_parser(parser):
    ssub = parser.add_subparsers(
        dest="sub_cmd", help="Sub command", title="Sub command", required=True
    )

    # "list"
    files_list = ssub.add_parser("list", help="List files")
    files_list.set_defaults(func=handle_list)
    files_list.add_argument("--json", action="store_true", help="Output in json")

    # "pull"
    files_pull = ssub.add_parser("pull", help="Pull a file")
    files_pull.set_defaults(func=handle_pull)
    files_pull.add_argument("name", help="filename")
    files_pull.add_argument("file", type=pathlib.Path)

    # "push"
    files_push = ssub.add_parser("push", help="Push a file")
    files_push.set_defaults(func=handle_push)
    files_push.add_argument("file", type=argparse.FileType("rb"))
    files_push.add_argument("name", help="filename")

    # "rm"
    files_rm = ssub.add_parser("rm", help="Remove a file")
    files_rm.set_defaults(func=handle_rm)
    files_rm.add_argument("name", help="filename")


def handle_list(options, session) -> int:
    ret = session.get(f"{options.uri}/files")
    if print_error(ret):
        return 1
    if options.json:
        print(json.dumps(ret.json()["items"]))
    else:
        print("Files:")
        for s in ret.json()["items"]:
            print(f"* {s}")
    return 0


def handle_pull(options, session) -> int:
    ret = session.get(f"{options.uri}/files/{options.name}", stream=True)
    if print_error(ret):
        return 1

    if os.path.exists(options.file):
        overwrite = input(
            "The file already exists on this machine, do you want to overwrite it [y/n]? "
        )
        if overwrite != "y":
            print("Not overwriting the file, exiting", file=sys.stderr)
            return 1
        print("The file will be overwritten")

    with options.file.open("wb") as f:
        for data in ret.iter_content(32768):
            print(".", end="")
            f.write(data)
    return 0


def handle_push(options, session) -> int:
    me = MultipartEncoder(fields={"file": (options.name, options.file)})
    ret = session.post(
        f"{options.uri}/files/{options.name}",
        data=me,
        headers={"Content-Type": me.content_type},
    )
    if print_error(ret):
        return 1
    return 0


def handle_rm(options, session) -> int:
    ret = session.delete(f"{options.uri}/files/{options.name}")
    if print_error(ret, 204):
        return 1
    return 0


def help_string():
    return "Manage files in /var/lib/lava/dispatcher/tmp"
