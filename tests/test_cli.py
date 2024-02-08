from invoice_conv.cli import decode
import pytest
from click.testing import CliRunner
import os


def test_decode():
    runner = CliRunner()
    result = runner.invoke(decode, ["--data", "tests/test_data/test_invoices.zip"])
    if result.exit_code != 0:
        raise AssertionError(result.output)
    assert os.path.exists("invoices.csv")

