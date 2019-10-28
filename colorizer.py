from numpy import ones, vectorize
from numpy.lib.recfunctions import unstructured_to_structured
from cv2 import filter2D
from sty import fg


def color(text, color):
    """Colors text based on ANSI encodings
    
    Parameters
    ----------
    text : str
        Text to be colored
    color : tuple
        RGB values
    
    Returns
    -------
    str
        Colored text
    """
    return f"{fg(*color)}{text}{fg.rs}"


class Colorizer:
    """A wrapper for colorizing text
    """
    def colorize(self):
        """Colors text obtained from processing
        """
        if self.args.color:
            hr = int(round(self.image.shape[0] / self.text.shape[0]))
            wr = int(round(self.image.shape[1] / self.text.shape[1]))

            # Get average color
            kernel = ones((hr, wr), dtype=float) / (hr * wr)
            colors = unstructured_to_structured(filter2D(self.image, -1, kernel)[::hr, ::wr, :]).astype("O")
            
            self.text = vectorize(color)(self.text, colors)
