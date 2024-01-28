from qreader import QReader
import cv2
import zipfile


class Invoice:
    def __init__(self):
        data = {
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

        # if input.endswith('.jpg'):
        #     self.input = cv2.imread(input)
        # elif input.endswith('.zip'):
        #     self.input = zipfile.ZipFile(input, 'r')
        #     self.read_data_package()
        # else:
        # raise NotImplementedError('Input file type not supported')

    def download_package(self, url):
        pass

    def read_data_package(self, input_pkg):
        # with zipfile.ZipFile(input_pkg) as package:
        #     for file_name in package.namelist():
        #         if file_name.endswith('.jpg') or file_name.endswith('.png'):                    # Get the image that contains the QR code
        #             with package.open(file_name) as img_file:
        #                 image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        #             # Use the detect_and_decode function to get the decoded QR data
        #             decoded_text = self.qr_reader.detect_and_decode(image=image)
        pass

    def decode_image(self, img_path):
        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        # Use the detect_and_decode function to get the decoded QR data
        return self.qr_reader.detect_and_decode(image=image)
