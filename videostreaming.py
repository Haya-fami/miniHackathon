import numpy as np
import cv2 as cv

img = cv.imread("test1.png")
img = cv.resize(img,(10,10),(400,400))
cv.imshow("image",img)
cv.waitKey(0)

cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    v, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


