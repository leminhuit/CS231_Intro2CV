import cv2;
import numpy as np;

# Buoc 1 : Doc anh tu file
input = cv2.imread('./Images/image1.png')
input2 = cv2.imread('./Images/image2.png')

view = input2.copy()
H = input.shape[1]
for D in range(H):
    view[:, H-D:] = input[:, 0:D]
    cv2.imshow('Animation', view)
    cv2.waitKey(3)