import cv2  
import numpy as np

# image = cv2.imread('./Images/bloodPic.png', cv2.IMREAD_GRAYSCALE)
# # cv2.imshow("Original", image)

# image = cv2.bitwise_not(image)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# eroded = cv2.erode(image, kernel)
# # cv2.imshow("Eroded", eroded)

# dilated = cv2.dilate(eroded, kernel)
# cv2.imshow("Eroded then Dilated", dilated)

# # Using Opening
# opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=3)
# cv2.imshow("Opening", opening)

# edged = cv2.Canny(opening, 30, 200)

# contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print("So luong te bao mau co trong hinh la", len(contours))

# cv2.waitKey(0)

image = cv2.imread("./Images/bloodPic.png")
# image = cv2.bitwise_not(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

output = cv2.connectedComponentsWithStats(thresh, 8, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output

for i in range(0, numLabels):
	# if this is the first component then we examine the
	# *background* (typically we would just ignore this
	# component in our loop)
	if i == 0:
		text = "examining component {}/{} (background)".format(
			i + 1, numLabels)

	# otherwise, we are examining an actual connected component
	else:
		text = "examining component {}/{}".format( i + 1, numLabels)

	# print a status message update for the current connected
	# component
	print("[INFO] {}".format(text))

	# extract the connected component statistics and centroid for
	# the current label
	x = stats[i, cv2.CC_STAT_LEFT]
	y = stats[i, cv2.CC_STAT_TOP]
	w = stats[i, cv2.CC_STAT_WIDTH]
	h = stats[i, cv2.CC_STAT_HEIGHT]
	area = stats[i, cv2.CC_STAT_AREA]
	(cX, cY) = centroids[i]

	output = image.copy()
	cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 3)
	cv2.circle(output, (int(cX), int(cY)), 4, (0, 0, 255), -1)

	componentMask = (labels == i).astype("uint8") * 255

	# show our output image and connected component mask
cv2.imshow("Output", output)
cv2.imshow("Connected Component", componentMask)
cv2.waitKey(0)