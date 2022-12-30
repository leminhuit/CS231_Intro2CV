import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("testGSC.jpg")
height, width, _ = image.shape
imageBG = cv2.imread("eff.jpg")
imageBG = cv2.resize(imageBG, (997, 561))

# Split the image into 3 distinct Colors
imageRedNumpy = np.asarray(image[:,:,2])
imageGreenNumpy = np.asarray(image[:,:,1])
imageBlueNumpy = np.asarray(image[:,:,0])

# Getting the Max and Min value on every channel
r_min, r_max = np.amin(imageRedNumpy[0:300, 0:475]), np.amax(imageRedNumpy[0:300, 0:475])
g_min, g_max = np.amin(imageGreenNumpy[0:300, 0:475]), np.amax(imageGreenNumpy[0:300, 0:475])
b_min, b_max = np.amin(imageBlueNumpy[0:300, 0:475]), np.amax(imageBlueNumpy[0:300, 0:475])

r_min -= 23; g_min -= 23; b_min -= 23
r_max += 23; g_max += 23; b_max += 23


for i in range(height):
    for j in range(width):
        if r_min <= image[i,j,2] <= r_max and g_min <= image[i,j,1] <= g_max and b_min <= image[i,j,0]<= b_max:
            image[i,j] = imageBG[i, j]

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = plt.imshow(image)
plt.show()