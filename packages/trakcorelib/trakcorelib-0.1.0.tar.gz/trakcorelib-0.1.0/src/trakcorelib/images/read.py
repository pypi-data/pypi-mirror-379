"""Functions for reading images."""

from __future__ import annotations

from typing import TYPE_CHECKING

from PIL import Image

from trakcorelib.images.convert import BitDepthConvertMode, convert_to_8bit_grayscale

if TYPE_CHECKING:
    import os


def read_image_as_8bit_grayscale(
    path: str | os.PathLike[str], convert_mode: BitDepthConvertMode = "high",
) -> Image.Image:
    """Read an image from a file and converts it to a bit depth of 8.

    Args:
        path: Path to the image to read.
        convert_mode: Method used to convert images with higher bit depth to
            8-bits.

    Returns:
        An 8-bit Pillow Image object (PIL.Image.Image) read from the specified
        file.

    """
    image = Image.open(path)
    return convert_to_8bit_grayscale(image, convert_mode)
