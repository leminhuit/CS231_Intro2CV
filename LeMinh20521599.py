import numpy as np
import cv2 as cv

# Histogram Simple Implementation
# x = np.array([1,1,1,2,2,2,5,25,1,1])
# unique, counts = np.unique(x, return_counts=True)
# print(np.asarray((unique, counts)).T)

# Load hình ảnh Grayscale
image = cv.imread("./eff.jpg", 0)
# cv.imshow("Image Input", image)
# cv.waitKey(0)

# Tính histogram của ảnh
histogram = np.array(np.unique(image, return_counts=True))
histResult = list(zip(histogram[0], histogram[1]))
# print(histResult)

# Tính tổng tích lũy CDF
cdf = histogram.copy()

for i in range(1, len(cdf[1])):
    cdf[1, i] += cdf[1, i - 1]
# print(cdf)

# Tính mapping màu
H = cdf[1].copy()
cdfMin = min(cdf[1])
height, width = image.shape
for i in range(len(cdf[1])):
    H[i] = np.around((cdf[1,i] - cdfMin)/(height * width - cdfMin) * 255)

print(H[image[0, 1]])

for i in range(height):
    for j in range(width):
        image[i, j] = H[image[i, j]]

cv.imshow("Result", image)
cv.waitKey()