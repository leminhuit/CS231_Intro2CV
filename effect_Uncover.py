import cv2;
import numpy as np;

# Buoc 1 : Doc anh tu file
input = cv2.imread('./Images/image1.png')
input2 = cv2.imread('./Images/image2.png')

view = input.copy()
H = input.shape[1]
for D in range(H):
    view[:, :H-D] = input[:, D:]
    view[:, H-D:] = input2[:, H-D:];
    cv2.imshow('Animation', view)
    cv2.waitKey(1)