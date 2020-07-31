"""
This module defines an abstract base drawer.

!!! question "Styles"
    Refer to the [Styles documentation](../../styles/index.md)
    for an in-depth guide to the **image processing behind Picharsso**.
"""

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
"""A collection of resampling filters.
See [Pillow's Filters](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters){target=_blank}.
"""

DEFAULT_RESAMPLING: str = "nearest"
"""The default resampling filter."""


class BaseDrawer(ABC):
    """
    An abstract base drawer.

    Attributes:
        height (int): The desired height of the text in characters.
        width (int): The desired width of the text in characters.
        resample (int): The resampling filter.
        format (Type[picharsso.format.BaseFormatter]): The formatter instance.

    Note:
        The following methods must be overwritten:

        - [`calculate_size`][picharsso.draw.base.BaseDrawer.calculate_size]
        - [`process`][picharsso.draw.base.BaseDrawer.process]
    """

    def __init__(self, height=42, width=0, resample=DEFAULT_RESAMPLING, **kwargs):
        """Initialization method.

        Args:
            height (Optional[int]): The desired height of the text in characters.
            width (Optional[int]): The desired width of the text in characters.
            resample (Optional[str]): The resampling filter.
            **kwargs (dict): Appropriate keyword arguments.
                    See [`BaseFormatter`][picharsso.format.base.BaseFormatter] and others.

        Note:
            When set as `0`, `height` is derived from `width` and vice versa.
            This is done to preserve the aspect ratio of the image.
        """
        self.height = None
        self.width = None
        self.resample = None
        BaseDrawer.set(self, height=height, width=width, resample=resample)

        self.format = new_formatter(**kwargs)

    def __call__(self, image):
        """Applies processing and formatting on the `image`
        and returns a single string.

        Args:
            image (PIL.Image.Image): The subject image.

        Returns:
            str: The string of text art.
        """
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
        """Calculates the size of the image for processing the text matrix.

        Args:
            image_size (Tuple[int, int]): The height and width of the subject image.

        Returns:
            Tuple[int, int]: The size of the image.
        """

    @abstractmethod
    def process(self, image):
        """Converts an image to a matrix of text.

        Args:
            image (PIL.Image.Image): The subject image,
                                    with `mode = "RGB"`,
                                    and `size = (<height>, <width>)`.

        Returns:
            numpy.ndarray: The text matrix,
                        with `shape = (<height>, <width>)`,
                        and `dtype = str`.
        """

    def set(self, height=None, width=None, resample=None):
        """Sets attributes of the drawer instance.

        Args:
            height (Option[int]): Sets `height`.
            width (Option[int]): Sets `width`.
            resample (Option[str]): Sets `resample`.

        Raises:
            ValueError: If both `height` and `width` are set to `0`.
        """
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


__all__ = ["BaseDrawer", "RESAMPLING_FILTERS", "DEFAULT_RESAMPLING"]
