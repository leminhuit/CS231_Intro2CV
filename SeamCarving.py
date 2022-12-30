import cv2
import imageio 
import imutils
import matplotlib.pyplot as plt 
from scipy import ndimage as ndi 
import numpy as np 
from tqdm import tqdm 

REMOVAL_SEAM_COLOR = np.array([0, 0, 255])  # Color of seam when visualizing
INSERTED_SEAM_COLOR = np.array([0, 255, 0])  # Color of seam when visualizing

image = cv2.imread('./Images/effect.png', 0)
cv2.imshow("Input", image)
cv2.waitKey()

new_img = image.copy()

def gen_emap(input):
    """Generate an energy map using Gradient magnitude
    Args:
    Returns:
        np.array: an energy map (emap) of input image 
    """
    Gx = ndi.convolve1d(input, np.array([1, 0, -1]), axis=1, mode='wrap')
    Gy = ndi.convolve1d(input, np.array([1, 0, -1]), axis=0, mode='wrap')
    return np.sqrt(Gx**2 + Gy**2)

def gen_smap(emap):
    """Generate an seam map from energy map
    Args:
        np.array(h, w): an energy map
    Returns:
        np.array(h, w): an seam map (smap) of input energy map 
    """ 
    h, w = emap.shape 
    smap = emap.copy()
    for row in range(1, h):
        for col in range(0, w):
            if col == 0:
                smap[row, col] = min(smap[row-1, col:col+2]) + smap[row, col]
            elif col == w-1:
                smap[row, col] = min(smap[row-1, col-1:col+1]) + smap[row, col]
            else: 
                smap[row, col] = min(smap[row-1, col-1:col+2]) + smap[row, col]
    return smap

def get_minimum_seam(emap):
    """Get a minimum energy seam from emap
    Input: 
        np.array(h x w): a energy map
    Function return:
        np.array(h): a minimum energy seam of energy map
    """
    # Generate seam map
    smap = gen_smap(emap) 
    
    # Get seam
    seam = []
    h, w = smap.shape
    index = np.argmin(smap[h-1, :])
    for row in range(h-1, -1, -1):
        if index == 0:
            index = index + np.argmin(smap[row, index:index+2])
        elif index == w-1:
            index = index - 1 +  np.argmin(smap[row, index-1:index+1])
        else: 
            index = index - 1 + np.argmin(smap[row, index-1:index+2])
        seam.append(index)
    return np.array(seam)[::-1]

def remove_seam(seam):
    """
    Input:
        arr(h) - a seam 
    Function return:
        arr(h x w x c) - an image with the deleted seam 
    """
    new_img = image.copy()
    h, w = new_img.shape[0:2]
    new_img = np.zeros(shape=(h, w-1))
    for row in range(0, h):
        col = seam[row]
        new_img[row, :col] = new_img[row, :col]
        new_img[row, col:] = new_img[row, col+1:]
    return new_img.astype(np.uint8)

getSeam = get_minimum_seam(gen_emap(image))
imageResult = remove_seam(getSeam)