from abc import ABC, abstractmethod

from PIL import Image

from ..format import new_formatter
from ..utils import ensure_rgb

RESAMPLING_FILTERS: dict = {
    "nearest": Image.NEAREST,
    "box": Image.BOX,
    "bilinear": Image.BILINEAR,
    "hamming": Image.HAMMING,
    "bicubic": Image.BICUBIC,
    "lanczos": Image.LANCZOS,
}

DEFAULT_RESAMPLING: str = "nearest"


class BaseDrawer(ABC):
    def __init__(self, height=42, width=0, resample=DEFAULT_RESAMPLING, **kwargs):
        self.height = None
        self.width = None
        self.resample = None
        BaseDrawer.set(self, height=height, width=width, resample=resample)

        self.format = new_formatter(**kwargs)

    def __call__(self, image):
        # Ensure that the image is in the `RGB` mode.
        image = ensure_rgb(image)

        # Calculate the new size of the image, for processing the text matrix.
        image_size = self.calculate_size(image.size[::-1])

        # Process text matrix from the resized image.
        text_matrix = self.process(
            image.resize(image_size[::-1], resample=self.resample)
        )

        # Apply formatting.
        return self.format(text_matrix, image, self.resample)

    @abstractmethod
    def calculate_size(self, image_size):

    @abstractmethod
    def process(self, image):

    def set(self, height=None, width=None, resample=None):
        # Set resampling filter
        if resample is not None:
            self.resample = RESAMPLING_FILTERS[resample]

        # Set height and width
        if height is not None or width is not None:
            new_h = self.height if height is None else height
            new_w = self.width if width is None else width

            if new_h == 0 and new_w == 0:
                raise ValueError("Either height or width must be non-zero")

            self.height = new_h
            self.width = new_w
