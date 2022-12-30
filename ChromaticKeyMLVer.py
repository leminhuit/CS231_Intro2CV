from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Importing the images 
fg = cv2.imread("foregroundForML.jpg")
bg = cv2.imread("testingBG.jpg")
bg2 = cv2.imread(".testGSC.jpg")
diffBg = cv2.imread("diffBG.jpg")

# Creating the dataset
fg = np.reshape(fg,(-1,3))
bg = np.reshape(bg,(-1,3))
bg2 = np.reshape(bg2[0:300,0:475], (-1,3))

X = np.array([*fg, *bg, *bg2])
y = np.array([*np.zeros(fg.shape[0]), *np.ones(bg.shape[0]), *np.ones(bg2.shape[0])], dtype=np.int8)

# Using the model
image = cv2.imread("greenscreenman.jpg")
height, width, _ = image.shape
clf = LogisticRegression(random_state=0).fit(X, y)
image = np.reshape(image, (-1, 3))
result = clf.predict(image)

diffBg = cv2.resize(diffBg, (width, height))
diffBg = np.reshape(diffBg, (-1, 3))

for i in range(result.shape[0]):
    if result[i]==1:
        image[i] = diffBg[i]

image = np.reshape(image, (height, width, 3))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = plt.imshow(image)
plt.show()