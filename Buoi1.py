import cv2;
import numpy as np;

# Buoc 1 : Doc anh tu file
input = cv2.imread('test.jpg')

# Buoc 2 : Hien thi anh
cv2.imshow('img', input)
cv2.waitKey()

# # Buoc 3 : Tang do sang anh len 20 don vi
# def increase_brightness(img, value = 30):
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h, s, v = cv2.split(hsv)

#     lim = 255 - value
#     v[v > lim] = 255
#     v[v <= lim] += value

#     final_hsv = cv2.merge((h, s, v))
#     img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
#     return img

# input = increase_brightness(input, value=20)
# cv2.imshow('img', input)
# cv2.waitKey()

# # Buoc 4 : Lat doi xung truc dung
flipVertical = cv2.flip(input, 0)
cv2.imshow('img', flipVertical)
cv2.waitKey()

# flipHorizontal = cv2.flip(input, 1)
# cv2.imshow('img', flipHorizontal)
# cv2.waitKey()

# gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', gray)
# cv2.waitKey()

# inverse_image = cv2.bitwise_not(gray);
# inverse_image_with_color = cv2.bitwise_not(input);
# cv2.imshow('img', inverse_image)
# cv2.waitKey()
# cv2.imshow('img', inverse_image_with_color)
# cv2.waitKey()

# Buoc 2 : Vong lap voi D
# view = input.copy()
# H = input.shape[0]
# for D in range(H):
# # Buoc 2.1 Cat phan dau cua view hien thi
#     view[0:D, : ] = flipVertical[H-D:, :]
# # Buoc 2.2 Cat phan cuoi cua view hien thi
#     view[D:, : ] = input[0:H-D, :]
# # Buoc 2.3 Hien thi anh
#     cv2.imshow('Animation', view)
#     cv2.waitKey(1)

# Buoc 2 : Vong lap voi D
# view = input.copy()
# H = input.shape[0]
# for D in range(H,0,-1):
# # Buoc 2.1 Cat phan dau cua view hien thi
#     view[0:D, :] = input[H-D:, :]
# # Buoc 2.2 Cat phan cuoi cua view hien thi
#     view[D:, :] = input[0:H-D, :]
# # Buoc 2.3 Hien thi anh
#     cv2.imshow('Animation', view)
#     cv2.waitKey(1)

# view = input.copy()
# H = input.shape[1]
# for D in range(H):
# # Buoc 2.1 Cat phan dau cua view hien thi
#     view[:, 0:D] = flipVertical[:, H-D:]
# # Buoc 2.2 Cat phan cuoi cua view hien thi
#     view[:, D:] = input[:, 0:H-D]
# # Buoc 2.3 Hien thi anh
#     cv2.imshow('Animation', view)
#     cv2.waitKey(1)

view = input.copy()
H = input.shape[1]
for D in range(H,0,-1):
# Buoc 2.1 Cat phan dau cua view hien thi
    view[:, 0:D] = flipVertical[:, H-D:]
# Buoc 2.2 Cat phan cuoi cua view hien thi
    view[:, D:] = input[:, 0:H-D]
# Buoc 2.3 Hien thi anh
    cv2.imshow('Animation', view)
    cv2.waitKey(1)

# Trái qua phải :
# img = input
# H = input.shape[1]
# print('H: ',H)
# for D in range(H):
# # Buoc 2.1 Cat phan dau cua view hien thi
#     img = cv2.hconcat([flipVertical[:, H-D:],input[:, 0:H-D]])
# # Buoc 2.2 Cat phan cuoi cua view hien thi
# # Buoc 2.3 Hien thi anh
#     cv2.imshow('Animation', img)
#     cv2.waitKey(5)