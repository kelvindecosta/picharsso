from cv2 import resize
from os import get_terminal_size


class Resizer:
    """A wrapper for resizing the loaded image
    """
    def resize_image(self):
        """Resizes loaded image
        """
        oh, ow = self.image.shape[:2]
        tw = self.args.width
        th = self.args.height

        if th is False and tw is False:
            tw, th = get_terminal_size()
        else:
            if th is None:
                _, th = get_terminal_size()
            
            if tw is None:
                tw, _ = get_terminal_size()
        
        self.image = resize(self.image, self.calc_size(oh, ow, th, tw)[::-1])


    def calc_size(self, oh, ow, th, tw):
        """Calculates new image size based on original image and text dimensions
        
        Parameters
        ----------
        oh : int
            original image height
        ow : int
            original image width
        th : int
            text height
        tw : int
            text width
        
        Returns
        -------
        (int, int)
            new image height, width
        """        
        if self.args.art == "braille":
            if bool(th) and bool(tw):
                nh = th * 4
                nw = tw * 2
            elif bool(th):
                nh = th * 4
                nw = int(round(ow / oh * nh))
            else:
                nw = tw * 2
                nh = int(round(oh / ow * nw))
        elif self.args.art == "ascii":
            if bool(th) and bool(tw):
                nh = th
                nw = tw
            elif bool(th):
                nh = th
                nw = int(round(ow / oh * nh * 1.75))
            else:
                nw = tw
                nh = int(round(oh / ow * nw / 1.75))

        return nh, nw
