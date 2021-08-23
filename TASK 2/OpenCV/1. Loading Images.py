import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread(r'C:\Users\sriya\Desktop\OPEnCV\watch.jpg',cv2.IMREAD_GRAYSCALE)
#imread_color-1 imread_unchanged=-1

cv2.imshow('image',img)
cv2.waitKey(0) #waits for key to be pressed
cv2.destroyAllWindows() #closes on pressing any key

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()