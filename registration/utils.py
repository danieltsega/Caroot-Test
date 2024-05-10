# utils.py

import barcode
from barcode.writer import ImageWriter

def generate_barcode(laptop):
    barcode_data = f"{laptop.owner_type}-{laptop.owner_id}"
    barcode_class = barcode.get_barcode_class('code128')
    barcode_instance = barcode_class(barcode_data, writer=ImageWriter())
    filename = f"barcode-{laptop.owner_id}"
    barcode_instance.save(filename)
    return filename
