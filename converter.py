import argparse
import cv2 as cv
import numpy as np
from sty import fg, bg
from os.path import exists, isfile


# Resize image
def resize(image, scale, b=False):
    h = image.shape[0]
    w = image.shape[1]

    if not b:
        h = int(round(h * scale / 1.75))
        w = int(round(w * scale))
    else:
        h = int(round(h * scale * 1.875))
        w = int(round(w * scale * 2))

    return cv.resize(image, (w, h))


# Convert grayscale image to ascii text
def image_to_ascii(image, color):
    # Set of ascii characters
    charset = " :!?PG@"
    charset = " .,:;irsXA253hMHGS#9b&@" 
    result = ""

    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # Normalizing image from range(0, 255) to (0, max index of charset)
    gray = cv.normalize(gray, None, 0, len(charset) - 1, cv.NORM_MINMAX)

    asciify = np.vectorize(lambda x: charset[x])
    text = asciify(gray)

    for i in range(text.shape[0]):
        for j in range(text.shape[1]):
            if color:
                pc = image[i, j]
                result += f"{fg(pc[0], pc[1], pc[2])}{text[i, j]}{fg.rs}"
            else:
                result += text[i, j]
        result += "\n"
    return result


def braille_from_sub(sub):
    pattern = {
        (0, 0) : 0x01, (0, 1) : 0x08,
        (1, 0) : 0x02, (1, 1) : 0x10,
        (2, 0) : 0x04, (2, 1) : 0x20,
        (3, 0) : 0x40, (3, 1) : 0x80
    }

    flag = 0x0
    for i in range(sub.shape[0]):
        for j in range(sub.shape[1]):
            px = sub[i, j]
            if px >= 64:
                flag = flag | pattern.get((i, j))
    return chr(ord('\u2800') + flag)


def image_to_braille(image, color):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    result = ""
    for i in range(0, gray.shape[0], 4):
        for j in range(0, gray.shape[1], 2):
            if color:
                nc = np.mean(np.mean(image[i:i+4, j:j+2], axis=0), axis=0)
                nc = np.vectorize(int)(nc)
                result += f"{fg(nc[0], nc[1], nc[2])}{braille_from_sub(gray[i:i+4, j:j+2])}{fg.rs}"
            else:
                result += braille_from_sub(gray[i:i+4, j:j+2])
        result += "\n"

    return result


# Parsing Arguments
def get_argparser():
    parser = argparse.ArgumentParser(description="Convert an Image to ASCII Art", prog="python converter.py")
    parser.add_argument("image_path", type=str, help="Path to Image File")

    parser.add_argument("-o", "--output", type=str, help="Path to Output File", metavar="")                     # Write to a file
    parser.add_argument("-v", "--verbose", action="store_true", help="Print Verbose")                           # Print stats
    parser.add_argument("-c", "--color", action="store_true", help="Color", default=False)                      # Color
    parser.add_argument("-b", "--braille", action="store_true", help="Braille", default=False)                  # Braille

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--scale", type=float, help="Scale Factor", default=0.15, metavar="")              # Reshape with scale
    group.add_argument("-w", "--width", type=int, help="New Width", metavar="")                                 # Reshape with width

    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()

    try:
        # Validate file
        image_path = args.image_path
        if not (exists(image_path) and isfile(image_path)):
            raise FileNotFoundError("File does not exist!")
    
        # Load image
        image = cv.imread(image_path)
        if image is None:
            raise ValueError("File is not an image!")

        scale = args.scale
        if scale <= 0:
            raise ValueError("Scale is invalid!")

        width = args.width
        if width:
            if width <= 0:
                raise ValueError("Width is invalid!")
            scale = width / (image.shape[1])

        
        image = resize(image, scale, args.braille)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        if not args.braille:
            text = image_to_ascii(image, args.color)
        else:
            text = image_to_braille(image, args.color)
        print(text)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()