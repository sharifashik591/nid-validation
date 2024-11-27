from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

image = PIL.open("picture/NID_Back.png")
decoder = PDF417Decoder(image)

if (decoder.decode() > 0):
    decoded = decoder.barcode_data_index_to_string(0)
else:
    print("Not found")