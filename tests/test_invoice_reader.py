import os
import tempfile
from invoice_conv.invoice_reader import InvoiceReader
import pytest


class TestInvoiceReader:
    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")

    def test_invoice_reader_decode_image(self):
        test_1_decoded = "A:504666347*B:254155421*C:PT*D:FR*E:N*F:20240102*G:FR U003/49261*\
H:JFN95T4X-49261*I1:PT*I3:14.21*I4:0.85*N:0.85*O:15.06*Q:cOQh*R:432"
        test_2_decoded = "A:501383328*B:999999990*C:PT*D:FS*E:N*F:20231127*G:FS 102F/1845*\
H:JFR7GTKJ-1845*I1:PT*I2:3.74*I7:1.52*I8:0.35*N:0.35*O:5.61*Q:G3gO*R:2648"

        reader = InvoiceReader()
        decoded_text = reader.decode_image(
            os.path.join(self.test_data_dir, "test_1.jpg")
        )
        assert decoded_text == test_1_decoded

        decoded_text = reader.decode_image(
            os.path.join(self.test_data_dir, "test_2.png")
        )
        assert decoded_text == test_2_decoded

    def test_invoice_reader_exporter(self):
        reader = InvoiceReader()

        reader.load_data_package(
            os.path.join(self.test_data_dir, "test_invoices.zip")
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_exported = os.path.join(temp_dir, "invoices.xlsx")
            reader.export_invoices(temp_exported)
            assert os.path.exists(temp_exported)
