import click

from invoice_conv.invoice_reader import InvoiceReader


@click.command()
@click.argument("data")
@click.option("--template", help="TODO")
def decode(data, template):
    """TODO"""
    reader = InvoiceReader()
    reader.load_data_package(data)
    reader.export_invoices(template=template)


def main():
    decode()
