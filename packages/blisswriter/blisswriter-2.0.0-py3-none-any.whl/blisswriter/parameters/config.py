"""Save options for a writer which relies on extra metadata published by Bliss"""
from __future__ import annotations

from typing import Any
from . import base

cli_saveoptions = dict(base.cli_saveoptions)


def default_saveoptions() -> dict[str, Any]:
    return base.extract_default_saveoptions(cli_saveoptions)
