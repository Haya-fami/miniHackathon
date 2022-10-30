import pytesseract as tess
from PIL import Image

img = Image.open('test3.jpg')
text = tess.image_to_string(img)

print(text)


import cv2 as cv
import numpy as np
import sys

img = cv.imread("test1.jpg")



img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imwrite("test1.png",img)


