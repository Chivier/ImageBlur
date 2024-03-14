# Python script, set a image to square and resize it to 128x128 icon

import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import requests
from io import BytesIO
import sys

# Load image from path
path = sys.argv[1]
original_image = Image.open(path)

# Set the image to square, keeping the center
width, height = original_image.size
if width > height:
    left = (width - height)/2
    right = (width + height)/2
    top = 0
    bottom = height
else:
    left = 0
    right = width
    top = (height - width)/2
    bottom = (height + width)/2
original_image = original_image.crop((left, top, right, bottom))

# Resize the image to 128x128
icon_image = original_image.resize((128, 128))

# Save the image
icon_image.save('icon.png')