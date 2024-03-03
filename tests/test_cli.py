from invoice_conv.cli import decode
import pytest
from click.testing import CliRunner
import os


class TestInvoiceReader:
    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")

    def test_decode(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            result = runner.invoke(
                decode, [os.path.join(self.test_data_dir, "test_invoices.zip")]
            )
            if result.exit_code != 0:
                raise result.exception
            assert os.path.exists("invoices.xlsx")
