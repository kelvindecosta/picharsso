from PIL import Image


def ensure_rgb(image):
    # If the image has a color palette,
    # convert to the `RGBA` mode.
    if image.mode == "P":
        image = image.convert("RGBA")

    # If the image is in `RGBA` mode,
    # create a white background.
    if image.mode == "RGBA":
        temp = Image.new("RGB", image.size, (255, 255, 255))
        temp.paste(image, mask=image.split()[3])
        image = temp

    # Convert to `RGB` mode
    return image.convert("RGB")
