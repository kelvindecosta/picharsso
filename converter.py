import os
import cv2 as cv


# Open file as grayscale image
def gray_scale(path):
    image = cv.imread(path, cv.IMREAD_GRAYSCALE)
    return image


# Resize image
def resize(image, scale):
    h, w = image.shape

    # Scale width further by 1.75 to normalize aspect ratio of a text character
    h = int(round(h * scale))
    w = int(round(w * scale * 1.75))

    return cv.resize(image, (w, h))
