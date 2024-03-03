import logging
import os
import tempfile
import zipfile

import cv2
import pandas
from qreader import QReader


class Invoice:
    pt_invoice_matches = {
        "A": "supplier VAT",
        "B": "client VAT",
        "C": "country code",
        "D": "document type",
        "E": "document state",
        "F": "document date",
        "G": "document UID",
        "H": "ATCUD",
        "I1": "tax country region",
        "I2": "tax base",
        "I3": "reduced tax base",
        "I4": "total reduced tax base",
        "N": "tax payable",
        "O": "gross total",
        "P": "withholding tax amount",
        "Q": "control",
        "R": "certificate",
    }
    data = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I1": [],
        "I2": [],
        "I3": [],
        "I4": [],
        "N": [],
        "O": [],
        "Q": [],
        "R": [],
    }

    @classmethod
    def update_from_string(cls, invoice_str):
        params = invoice_str.split("*")
        for param in params:
            key, value = param.split(":")

            # Set the value of the corresponding attribute
            try:
                cls.data[key].append(value)
            except KeyError:
                logging.warning(f"Unknown key {key}")

        size = max(map(len, cls.data.values()))
        for key in cls.data:
            if len(cls.data[key]) < size:
                cls.data[key].append("NA")

    @classmethod
    def export(cls):
        # template is probably gonna be a list of tuples with the following format:
        # [(component, position),...]
        data_formated = {}
        # for component in cls.data:
        for component in cls.pt_invoice_matches:
            data_formated[cls.pt_invoice_matches[component]] = cls.data.get(
                component
            )
        return pandas.DataFrame(data_formated)


class InvoiceReader:
    def __init__(self):
        self.qr_reader = QReader()
        self.invoices = Invoice()

    def download_package(self, url):
        # TODO download package from url,
        #  where url is most likely a google drive link
        pass

    def load_data_package(self, input_pkg):
        with zipfile.ZipFile(input_pkg) as package:
            with tempfile.TemporaryDirectory() as temp_dir:
                package.extractall(temp_dir)
                for file in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, file)
                    self.invoices.update_from_string(
                        self.decode_image(file_path)
                    )

    def decode_image(self, img_path):
        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        # Use the detect_and_decode function to get the decoded QR data
        decoded = self.qr_reader.detect_and_decode(image=image)
        return decoded[0]

    def export_invoices(self, output_file="invoices.xlsx", template=None):
        # A : [1,2,3]
        df = self.invoices.export()
        df.to_excel(output_file, index=False)
