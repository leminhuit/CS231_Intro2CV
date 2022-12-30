import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading the image and template in
img = cv2.imread('./Images/9-ro.jpeg');
mask = cv2.imread('./Images/template.png');
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Defining some function to solve the problem
def normalize_img(img: np.array):
    min = np.amin(img)
    max = np.amax(img)
    return (img - min) / (max - min)

def crossCorrelation(H: np.array, F:np.array) -> np.array:
    Hshape, Fshape = H.shape, F.shape
    result = np.zeros((Hshape[0] - Fshape[0], Hshape[1] - Fshape[1]))
    for i in range(Hshape[0] - Fshape[0]):
        for j in range(Hshape[1] - Fshape[1]):
            result[i][j] = np.sum(H[i:i + Fshape[0], j : j + Fshape[1]] * F)
    return result

def imshow(img, figsize=(6, 6)):
    fig, ax = plt.subplots(1, 1, figsize=(figsize))
    ax.axis('off')
    ax.imshow(img)

# Normalizing the image and the mask
img = normalize_img(img);
mask = normalize_img(mask);

# Apply cross correlation to the 2 normalized images
result = crossCorrelation(img, mask);
result = normalize_img(result);
result = 1 - result;
cv2.imshow("Result",result);
cv2.waitKey();

w, h = mask.shape[1], mask.shape[0]
THRESHOLD = 0.95
loc = np.where(result >= THRESHOLD)

for y, x in zip(loc[0], loc[1]):
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

imshow(img)


