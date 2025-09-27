"""Functions for converting images."""

from __future__ import annotations

import math
from typing import Literal

import numpy as np
from PIL import Image

__all__ = ["convert_to_8bit_grayscale"]

BitDepthConvertMode = Literal["low", "high", "minmax", "custom"]


def convert_to_8bit_grayscale(
    image: Image.Image,
    mode: BitDepthConvertMode = "high",
    custom_range: tuple[int, int] | None = None,
) -> Image.Image:
    """Convert an image to an 8-bit image by bitshifting.

    This does nothing if the image already has 8-bit depth.

    Args:
        image: A Pillow Image object (PIL.Image.Image)
        mode: When bit shifting images with higher bit depth than 8, use this
            bit-shifting mode. Options:
            - 'high': use 8 most significant bits;
            - 'low': use 8 least significant bits;
            - 'minmax': compress the used range of the original image to 8 bits;
            - 'custom': compress the custom range specified in the custom-range
              argument to 8 bits.
        custom_range: Custom range to compress to 8 bits, used only when
            'custom' is specified.

    Returns:
        An 8 bit Pillow Image object (PIL.Image.Image).

    """
    if image.mode == "L":
        # We are already an 8-bit grayscale image.
        return image

    if image.mode.startswith("I;16"):
        # Use custom conversion for 16-bit images, which often contain data with
        # a smaller bit depth, e.g. 12 bits.
        return convert_16bit_grayscale_to_8bit_grayscale(image, mode, custom_range)

    # Otherwise, use Pillow's default conversion to 8-bit grayscale.
    return image.convert("L")


def convert_16bit_grayscale_to_8bit_grayscale(
    image: Image.Image,
    mode: BitDepthConvertMode = "high",
    custom_range: tuple[int, int] | None = None,
) -> Image.Image:
    assert image.mode.startswith("I;16")

    # Convert image to Numpy array.
    data = np.array(image)

    # Guess the bit depth based on the maximum pixel value in the image; this
    # assumes that the brightest pixel is at least half of the dynamic range.
    maximum = data.max()
    bit_depth = math.ceil(math.log2(maximum))

    if mode == "high":
        # Use the highest 8 bits of the image.
        data = np.right_shift(data, bit_depth - 8)
    elif mode == "low":
        # Use the lowest 8 bits of the image.
        data = np.bitwise_and(data, 255)
    elif mode == "minmax":
        minimum = data.min()
        data = (data.astype(float) - minimum) / (maximum - minimum) * 255
    elif mode == "custom":
        # Convert a custom range or the range [minimum, maximum] to [0, 255].
        if custom_range is None:
            msg = 'Specify a custom normalisation range when using mode "custom".'
            raise ValueError(msg)
        data = (
            (data.astype(float) - custom_range[0])
            / (custom_range[1] - custom_range[0])
            * 255
        )
        data[data < 0] = 0
        data[data > 255] = 255

    # Convert data array to 8-bits, then convert to Pillow image.
    return Image.fromarray(data.astype(np.uint8))
