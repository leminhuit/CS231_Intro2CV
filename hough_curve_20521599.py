'''
Sử dụng code được cung cấp để hoàn tất thuật toán tìm đường thẳng:

Bước 1: Tính ảnh biên cạnh: Edge (dùng ảnh năng lượng)

Bước 2: Khởi tạo H là ma trận 0

Bước 3:

Với mỗi điểm (x, y) thuộc Edge

với mỗi điểm theta thuộc 0->360

tính pro = xcos(theta) + y sin(theta)

Cộng tích lũy H[pro, theta]++1

Bước 4: Chọn ra những điểm pro và theta "đủ lớn":

H[pro0, theta0] > threshold (threshold có thể chọn 50-100)

Trực quan hóa phương trình: pro0 = xcos(theta0) + y sin(theta0)


'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./test.jpg',0);
edges = cv2.Canny(img, 50, 150)

# print(img.shape)

def deg2grad(deg):
	return deg*3.141592654/180
# Step 0.5: initialize hough table
theta_range = np.arange(-3.14, 3.14, 0.01)
H = np.zeros((500, len(theta_range)), dtype=np.uint8)
# print(H.shape)

# Step 1: accumulate hough space
def accumulate(point):
	#for theta in range(360):
	for theta in theta_range:
		pro = point[0]*np.cos(theta) + point[1]*np.sin(theta)
		# If pro in range of Hough space
		if pro >= 0 and pro < 500:
		# map theta to Hough space
		# (theta - (-3.14))/0.01
			H[int(pro), int((theta+3.14)/0.01)] += 1
	return H
	
def Hough_space(img):
	lines = []
	height, width = img.shape
	for y in range(height):
		for x in range(width):
			if img[y,x] > 200:
				accumulate([x,y])
	height_H, width_H =H.shape
	for pro in range(height_H):
		for theta in range(width_H):
			if H[pro,theta] > 150:
				H[pro,theta] = 255
				lines.append([[pro,theta]])
	return lines

def Hough_space2(img):
    lines=[]
    index = np.where(img>200)
    listOfCoordinates= list(zip(index[1], index[0]));
    for point in listOfCoordinates:
        accumulate(point)
    index_H = np.where(H>150)
    listOfCoordinates_H= list(zip(index_H[0], index_H[1]))
    for point_H in listOfCoordinates_H:
        H[point_H] = 255
        lines.append([[point_H[0],point_H[1]]])
    return lines
	
# bước 4 
# lines = np.array(Hough_space(edges))
lines2 = np.array(Hough_space2(edges))

print(lines2)
for line in lines2:
	rho,theta = line[0]
	theta=theta*0.01 - 3.14
	print(theta)
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("Image", img)

cv2.waitKey(0)






