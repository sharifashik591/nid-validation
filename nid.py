import cv2
from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

# Load the image using OpenCV
image = cv2.imread("picture/NID_Back.png")

# Convert to grayscale (barcodes work best in grayscale)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to enhance the barcode contrast
_, thresh_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

# Save the preprocessed image as a temporary file
temp_file = "preprocessed_image.png"
cv2.imwrite(temp_file, thresh_image)

# Load the preprocessed image with PIL
pil_image = PIL.open(temp_file)

# Decode the barcode
decoder = PDF417Decoder(input_image=pil_image)

if decoder.decode() > 0:
    for i in range(decoder.decode()):
        decoded = decoder.barcode_data_index_to_string(i)
        print(f"Decoded Data {i + 1}: {decoded}")
else:
    print("No PDF417 barcode detected.")
