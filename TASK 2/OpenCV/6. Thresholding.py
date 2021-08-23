import cv2
import numpy as np

img = cv2.imread(r'C:\Users\sriya\Desktop\OPEnCV\bookpage.jpg')

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #attempt to vary the threshold, and account for the curving pages
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()

