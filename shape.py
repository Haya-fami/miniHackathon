import numpy as np
import cv2 as cv
import sys

img = np.zeros((520,520,3), np.uint8)

line = cv.line(img,(10,10),(500,500),(255,255,255),3)
rect = cv.rectangle(img,(10,10),(500,500),(255,0,0),2)
cir = cv.circle(img,(255,255),30,(0,0,255),-1)

pts = np.array([[20,30],[30,100],[150,100],[100,40]], np.int32)
#pts = pts.reshape((-1,1,2))
poly = cv.polylines(img,[pts],True,(0,255,255))

cv.imshow("shapes",line)
cv.imshow("shapes",rect)
cv.imshow("shapes",cir)
cv.imshow("shapes",poly)

cv.waitKey(0)
