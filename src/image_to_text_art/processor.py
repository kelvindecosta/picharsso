from numpy import zeros, resize, vectorize, ascontiguousarray, array
from cv2 import cvtColor, COLOR_RGB2GRAY, normalize, NORM_MINMAX


# Braille pattern
PATTERN = {
    (0, 0) : 0x01, (0, 1) : 0x08,
    (1, 0) : 0x02, (1, 1) : 0x10,
    (2, 0) : 0x04, (2, 1) : 0x20,
    (3, 0) : 0x40, (3, 1) : 0x80
}


class Processor:
    """A wrapper for processing the image
    """
    def art(self):
        """Processes image and extracts values for text art
        """
        self.load_image()
        self.resize_image()

        if self.args.color:
            canvas = cvtColor(self.image, COLOR_RGB2GRAY)
        else:
            canvas = self.image
        
        run = {
            "braille" : self.braille,
            "ascii" : self.ascii
        }

        run.get(self.args.art)(canvas)

        self.colorize()
        self.display()


    def braille(self, canvas):
        """Processes image and extracts values for Braille based text art
        """
        canvas = canvas.astype(int)

        text = zeros(canvas[::4, ::2].shape, dtype=int)

        for y in range(4):
            for x in range(2):
                text += resize((canvas[y::4, x::2] > self.args.threshold) * PATTERN.get((y, x)), text.shape)
        
        text = vectorize(lambda x : chr(ord('\u2800') + x))(text)
        text = ascontiguousarray(text)
        self.text = text


    def ascii(self, canvas):
        """Processes image and extracts values for ASCII based text art
        """
        # Load charsets from config
        charset = self.configuration.charsets[self.args.charset]
        if self.args.negative:
            charset = charset[::-1]

        canvas = normalize(canvas, None, 0, len(charset)-1, NORM_MINMAX)
        self.text = vectorize(lambda x: charset[x])(canvas)