"""
Test: Extra

Version: 5.9.0
Date updated: 19/09/2025 (dd/mm/yyyy)
"""

# Library
# ---------------------------------------------------------------------------
import pytest

from absfuyu import extra as ext


def test_ext_load():
    assert ext.is_loaded() is True
