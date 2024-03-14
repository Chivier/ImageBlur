# Python script, blur a image using a Gaussian filter

import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import requests
from io import BytesIO
import sys

# Load image from path
path = sys.argv[1]
original_image = Image.open(path)

# Apply Gaussian filter
blur_image = original_image.filter(ImageFilter.GaussianBlur(15)) 

# Save the image
blur_image.save('blurred.png')
