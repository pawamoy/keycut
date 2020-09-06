"""Tests for the `cli` module."""

import pytest

from keycut import cli


def test_main():
    """Basic CLI test."""
    assert cli.main([]) == 0


def test_show_help(capsys):
    """
    Shows help.

    Arguments:
        capsys: Pytest fixture to capture output.
    """
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "keycut" in captured.out


def test_main_errors_without_args():
    with pytest.raises(SystemExit):
        cli.main([])


def test_main_ok():
    cli.main(["bash"])
