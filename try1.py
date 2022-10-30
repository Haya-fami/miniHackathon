import cv2 as cv
import pytesseract as tess

img = cv.imread("test4.jpg")

gray = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

"""""
#gray image
def im_grayscale(img):
    gray = cv.cvtColor(img, cv.COLOR_GRAY2BGR )
    return(gray)

#imbalanced cancellation
def noise_cancel(gray):
    clear = cv.medianBlur(gray, 5)
    return (clear)

#fetching text
def threshold_pickup(clear):
    imtext = cv.threshold(clear,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    return(imtext)

def text_im(imtext):
    text = tess.image_to_string(imtext)
    return (text)
    

gray = im_grayscale(img)
clear = noise_cancel(gray)
imtext = threshold_pickup(clear)
text = text_im(imtext)


print(text)
"""

cv.imshow('image',gray)
cv.waitKey(0)

