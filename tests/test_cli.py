import pytest

from keycut import cli


def test_main_errors_without_args():
    with pytest.raises(SystemExit):
        cli.main([])


def test_main_ok():
    cli.main(["bash"])
