"""Submodule that provides utilities relating to the package itself."""

from __future__ import annotations

__all__ = [
    "AUTHOR",
    "NAME",
    "VERSION",
]

import importlib.metadata

NAME = __package__.split(".")[0]
AUTHOR = "Dom Walters"
VERSION = importlib.metadata.version(NAME)
