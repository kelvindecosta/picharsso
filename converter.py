import argparse
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


# Convert grayscale image to ascii text
def gs_image_to_ascii(image):
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


def get_argparser():
    parser = argparse.ArgumentParser(description="Convert an Image to ASCII Art", prog="python converter.py")
    parser.add_argument("image_path", type=str, help="Path to Image File")
    parser.add_argument("-s", "--scale", type=float, help="Scale Factor", default=0.150, metavar="")
    parser.add_argument("-o", "--output", type=str, help="Path to Output File", metavar="")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print Verbose")

    return parser


if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()

    try:
        image_path = args.image_path
        if not os.path.exists(image_path) or not os.path.isfile(image_path):
            raise FileNotFoundError("File does not exist!")

        image = gray_scale(image_path)
        if image is None:
            raise ValueError("File is not an image!")

        scale = args.scale
        if scale <= 0:
            raise ValueError("Scale is invalid!")

        image = resize(image, scale)
        text = gs_image_to_ascii(image)

        output = args.output
        if output:
            with open(output, "w+") as f:
                f.write(text)

        if args.verbose:
            for data in ["image_path", "scale", "output"]:
                print("{:10} : {}".format(data, eval(data)))
            print("\n")
        print("ASCII IMAGE\n")
        print(text)
    except Exception as e:
        print(e)
