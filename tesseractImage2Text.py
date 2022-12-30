import pytesseract

from PIL import Image, ImageFilter

import numpy as np
import matplotlib.pyplot as plt
from skimage import color
import cv2
import io
from skimage import data
from skimage.color import rgb2gray

front = Image.open("./Images/imageinput.jpg")

print(front.format, front.size, front.mode)

print(type(front))

text = pytesseract.image_to_string(front, lang = 'eng')

print(text)