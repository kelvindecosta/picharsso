import os
import cv2


def gray_scale(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return image
