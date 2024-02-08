from qreader import QReader
import cv2
import zipfile
import pandas
import tempfile
import os


class Invoice:
    def __init__(self):
        self.data = {
            "A": {"value": None, "description": "supplier nif"},
            "B": {"value": None, "description": "client nif"},
            "C": {"value": None, "description": "country code"},
            "D": {"value": None, "description": "currency code"},
            "E": {"value": None, "description": "delivery"},
            "F": {"value": None, "description": "transaction date"},
            "G": {"value": None, "description": "sale terminal id"},
            "H": {"value": None, "description": "invoice id"},
            "I1": {"value": None, "description": "tax rate"},
            "I3": {"value": None, "description": "tax base"},
            "I4": {"value": None, "description": "tax value"},
            "N": {"value": None, "description": "total value"},
            "O": {"value": None, "description": "paid value"},
            "Q": {"value": None, "description": "digital signature"},
            "R": {"value": None, "description": "control"},
        }

    @classmethod
    def from_string(cls, invoice_str):
        obj = cls()

        params = invoice_str.split("*")

        for param in params:
            key, value = param.split(":")

            # Set the value of the corresponding attribute
            obj.data[key]["value"] = value

        return cls(invoice_str)


class InvoiceReader:
    def __init__(self):
        self.qr_reader = QReader()
        self.invoices = []

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
                    self.invoices.append(self.decode_image(file_path))

    def decode_image(self, img_path):
        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        # Use the detect_and_decode function to get the decoded QR data
        return self.qr_reader.detect_and_decode(image=image)

    def export_invoices(self, output_file="invoices.xlsx", template=None):
        df = pandas.DataFrame([invoice.data for invoice in self.invoices])
        df.to_excel(output_file, index=False)
