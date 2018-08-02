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


# Convert image to ascii text
def image_to_ascii(image):
    # Set of ascii characters
    charset = " .,:;irsXA253hMHGS#9b&@"
    result = ""

    # Normalizing image from range(0, 255) to (0, max index of charset)
    image = cv.normalize(image, None, 0, len(charset) - 1, cv.NORM_MINMAX)

    for row in image:
        for pixel in row:
            result += charset[pixel]
        result += "\n"

    return result
