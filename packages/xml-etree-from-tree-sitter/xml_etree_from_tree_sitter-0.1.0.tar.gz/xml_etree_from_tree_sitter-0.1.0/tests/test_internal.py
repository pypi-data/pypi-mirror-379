"""Test the `internal` module and associated CLI functions."""

# ruff: noqa: D103, S101
from __future__ import annotations

import xml_etree_from_tree_sitter as etree


def test_name() -> None:
    assert etree.internal.NAME == "xml_etree_from_tree_sitter"


def test_author() -> None:
    assert etree.internal.AUTHOR == "Dom Walters"


def test_version() -> None:
    assert etree.internal.VERSION == "0.1.0"
