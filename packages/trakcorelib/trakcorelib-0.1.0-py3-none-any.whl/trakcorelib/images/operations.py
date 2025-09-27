"""Operations on images."""

from collections.abc import Sequence

from PIL import Image, ImageEnhance, ImageOps

from trakcorelib.images.convert import convert_to_8bit_grayscale


def combine_into_rgb_image(
    image_red: Image.Image,
    image_green: Image.Image,
    image_blue: Image.Image,
) -> Image.Image:
    """Combine three images into individual channgels of a single RGB image.

    Args:
        image_red: Image to use for the red channel.
        image_green: Image to use for the green channel.
        image_blue: Image to use for the blue channel.

    Returns:
        A new 8-bit RGB image where each channel is assigned from the specified
        image.

    """
    if image_red.size != image_green.size or image_red.size != image_blue.size:
        msg = (
            "Combining images into a single RGB image requires them to all "
            "have the same size."
        )
        raise ValueError(msg)

    # Convert to 8-bit grayscale images with default settings.
    red = convert_to_8bit_grayscale(image_red)
    green = convert_to_8bit_grayscale(image_green)
    blue = convert_to_8bit_grayscale(image_blue)

    # Merge now-guaranteed 8-bit grayscale images into a single 8-bit RGB image.
    return Image.merge("RGB", (red, green, blue))


def crop(
    image: Image.Image,
    x_centre: float,
    y_centre: float,
    width: int,
    height: int,
) -> Image.Image:
    """Crops an image around a specified centre point.

    This crops the image with the specified width and height around the
    specified centre point.

    The new image boundaries are capped to the original image size. Hence, the
    specified "centre point" is only the actual centre away from the image
    edges.

    Args:
        image: Image to crop.
        x_centre: x-coordinate of the cropping centre point in pixels.
        y_centre: y-coordinate of the cropping centre point in pixels.
        width: Width of the cropped image.
        height: Height of the cropped image.

    Returns:
        A new cropped image.

    """
    original_width, original_height = image.size

    left = max(round(x_centre - width / 2), 0)
    top = max(round(y_centre - height / 2), 0)

    right = left + width
    if right > original_width:
        right = original_width
        left = max(original_width - width, 0)

    bottom = top + height
    if bottom > original_height:
        bottom = original_height
        top = max(original_height - height, 0)

    return image.crop((left, top, right, bottom))


def resize(image: Image.Image, size_multiplier: float) -> Image.Image:
    """Resize an image according to a size multiplier.

    Args:
        image: Image to resize.
        size_multiplier: Factor applied to the current image size. For example,
            a factor of 2 applied to an image of size (1024, 1024) will yield an
            image of size (2048, 2048).

    Returns:
        A new resized image.

    """
    width, height = image.size
    new_width = round(width * size_multiplier)
    new_height = round(height * size_multiplier)
    return image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)


def stitch(images: Sequence[Image.Image]) -> Image.Image:
    """Stitch images horizontally together.

    This only supports 8-bit grayscale images. Images of different heights are
    aligned to the top edge of the image (i.e. y = 0).

    Args:
        images: Images to stitch together.

    Returns:
        A new image with all images stitched together horizontally.

    """
    if any(image.mode != "L" for image in images):
        msg = "Stitching images is only supported for 8-bit grayscale images."
        raise NotImplementedError(msg)

    total_width = sum(image.size[0] for image in images)
    total_height = max(image.size[1] for image in images)

    stitched = Image.new("L", (total_width, total_height))
    x = 0
    for image in images:
        stitched.paste(image, (x, 0))
        x += image.size[0]
    return stitched


def adjust_contrast(image: Image.Image, factor: float) -> Image.Image:
    """Adjust image contrast.

    Args:
        image: Image to adjust contrast for.
        factor: A factor of 0.0 gives a solid gray image, a factor of 1.0 gives
            the original image, and greater values increase the contrast of the
            image.

    Returns:
        A new image with adjusted contrast.

    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)


def adjust_brightness(image: Image.Image, factor: float) -> Image.Image:
    """Adjust image brightness.

    Args:
        image: Image to adjust brightness for.
        factor: A factor of 0.0 gives a black image, a factor of 1.0 gives the
            original image, and greater values increase the brightness of the
            image.

    Returns:
        A new image with adjusted brightness.

    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


def adjust_sharpness(image: Image.Image, factor: float) -> Image.Image:
    """Adjust image sharpness.

    Args:
        image: Image to adjust sharpness for.
        factor: A factor of 0.0 gives a blurred image, a factor of 1.0 gives
            the original image, and a factor of 2.0 gives a sharpened image.

    Returns:
        A new image with adjusted sharpness.

    """
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)


def adjust_color(image: Image.Image, factor: float) -> Image.Image:
    """Adjust image color balance.

    Args:
        image: Image to adjust color for.
        factor: A enhancement factor of 0.0 gives a black and white image. A
            factor of 1.0 gives the original image.

    Returns:
        A new image with adjusted color balance.

    """
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)


def apply_auto_contrast(image: Image.Image) -> Image.Image:
    """Apply auto contrast to an image.

    This uses a default configuration for the auto contrast algorithm from
    Pillow.

    Args:
        image: Image to apply auto contrast to.

    Returns:
        A new image with auto contrast applied.

    """
    return ImageOps.autocontrast(image, cutoff=0.3, ignore=None)


def equalize(image: Image.Image) -> Image.Image:
    """Equalize the histogram of an image.

    This enhances the contrast of the image by equalizing its histogram.

    Args:
        image: Image to equalize.

    Returns:
        A new image with equalized histogram.

    """
    return ImageOps.equalize(image, mask=None)
