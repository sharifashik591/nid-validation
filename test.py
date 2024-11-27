from pylibdmtx.pylibdmtx import decode
from PIL import Image

# Load the image containing the DataMatrix
image_path = "picture/NID_Back.png"
image = Image.open(image_path)

# Decode the DataMatrix
decoded_data = decode(image)
for data in decoded_data:
    print(f"Decoded Data: {data.data.decode('utf-8')}")



# import cv2
# from pylibdmtx.pylibdmtx import decode

# image = cv2.imread("picture/NID_Back.png")
# h, w  = image.shape[:2]
# decdd = decode((image[:, :, :1].tobytes(), w, h))
# print(decdd)