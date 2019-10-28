from cv2 import resize
from os import get_terminal_size


class Resizer:
    """A wrapper for resizing the loaded image
    """
    def __init__(self):
        """Resizes loaded image
        """
        oh, ow = self.image.shape[:2]
        tw = self.args.width
        th = self.args.height

        if all([x is None for x in [tw, th]]):
            tw, th = get_terminal_size()
        
        if self.args.ratio:
            if tw is None:
                tw = int(round(ow * th / oh))
            else:
                th = int(round(oh * tw / ow))
        
        if not self.args.command == "braille":
            nh = int(round(th / 1.75))
            nw = tw
        else:
            nh = int(round(th * 1.875))
            nw = tw * 2
        
        self.image = resize(self.image, (nw, nh))

