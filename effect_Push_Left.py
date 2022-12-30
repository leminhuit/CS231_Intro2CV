import cv2;
import numpy as np;

# Buoc 1 : Doc anh tu file
input = cv2.imread('./Images/image1.png')
input2 = cv2.imread('./Images/image2.png')

# Hieu ung Push Left
view = input.copy()
H = input.shape[1]
for D in range(H):
# Buoc 2.1 Cat phan dau cua view hien thi
    view[:, 0:D] = input[:, H-D:]
# Buoc 2.2 Cat phan cuoi cua view hien thi
    view[:, D:] = input2[:, 0:H-D]
# Buoc 2.3 Hien thi anh
    cv2.imshow('Animation', view)
    cv2.waitKey(1)