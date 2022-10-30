#import libraries
import cv2 as cv
import numpy as np

#declaring variable and assigning frames are to be record  frames to it
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
