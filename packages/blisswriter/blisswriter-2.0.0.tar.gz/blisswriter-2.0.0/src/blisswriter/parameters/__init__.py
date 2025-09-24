"""NeXus writer save options"""
from __future__ import annotations

from typing import Any

from . import base
from . import config

cli_saveoptions = {
    "noconfig": {
        "dest": "configurable",
        "action": "store_false",
        "help": "Do not use extra writer information from Redis",
    },
    "start_semaphore_file": {
        "dest": "start_semaphore_file",
        "default": None,
        "type": str,
        "help": "Create this file when started listening",
    },
}


def all_cli_saveoptions(configurable: bool = True) -> dict[str, dict[str, Any]]:
    if configurable:
        ret = dict(config.cli_saveoptions)
    else:
        ret = dict(base.cli_saveoptions)
    ret.update(cli_saveoptions)
    return ret


def default_saveoptions(configurable: bool = False) -> dict[str, Any]:
    if configurable:
        ret = config.default_saveoptions()
    else:
        ret = base.default_saveoptions()
    ret["configurable"] = configurable
    return ret
