from invoice_conv.invoice_reader import InvoiceReader
import pytest


def test_invoice_reader_decode_image():
    test_1_decoded = "A:504666347*B:254155421*C:PT*D:FR*E:N*F:20240102*G:FR U003/49261*\
            H:JFN95T4X-49261*I1:PT*I3:14.21*I4:0.85*N:0.85*O:15.06*Q:cOQh*R:432"
    test_2_decoded = "A:501383328*B:999999990*C:PT*D:FS*E:N*F:20231127*G:FS 102F/1845*\
            H:JFR7GTKJ-1845*I1:PT*I2:3.74*I7:1.52*I8:0.35*N:0.35*O:5.61*Q:G3gO*R:2648"

    reader = InvoiceReader()
    decoded_text = reader.decode_image("tests/test_data/test_1.jpg")
    assert decoded_text == test_1_decoded

    decoded_text = reader.decode_image("tests/test_data/test_2.png")
    assert decoded_text == test_2_decoded


def test_invoice_reader_exporter():
    reader = InvoiceReader()
    reader.read_data_package("tests/test_data/test_invoices.zip")
    reader.export("tests/test_data/test_package.zip", "tests/test_data/")
