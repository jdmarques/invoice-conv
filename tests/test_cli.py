from invoice_conv.cli import decode
import pytest
from click.testing import CliRunner
import os


def test_decode():
    runner = CliRunner()
    result = runner.invoke(decode, ["tests/test_data/test_invoices.zip"])
    if result.exit_code != 0:
        raise result.exception
    assert os.path.exists("invoices.xlsx")
