import pathlib

import numpy as np
from PIL import Image
import pytest

from trakcorelib.images.imagesequence import DiskImageSequence
from trakcorelib.images.operations import (
    adjust_brightness,
    adjust_color,
    adjust_contrast,
    adjust_sharpness,
    apply_auto_contrast,
    combine_into_rgb_image,
    crop,
    equalize,
    resize,
    stitch,
)
from trakcorelib.tests.images.utils import create_example_image


def test_combine_into_rgb_image(
    example_8bit_disk_image_sequence: DiskImageSequence,
) -> None:
    red = example_8bit_disk_image_sequence[0]
    green = example_8bit_disk_image_sequence[1]
    blue = example_8bit_disk_image_sequence[2]

    combined = combine_into_rgb_image(red, green, blue)
    combined_arr = np.asarray(combined)
    np.testing.assert_equal(np.asarray(red), combined_arr[:, :, 0])
    np.testing.assert_equal(np.asarray(green), combined_arr[:, :, 1])
    np.testing.assert_equal(np.asarray(blue), combined_arr[:, :, 2])


@pytest.mark.parametrize(
    "crop_args,expected_size,expected_rows_slice,expected_cols_slice",
    [
        pytest.param(
            (100, 150, 32, 64),
            (32, 64),
            slice(150 - 32, 150 + 32),
            slice(100 - 16, 100 + 16),
            id="no overlap",
        ),
        pytest.param(
            (10, 150, 32, 64),
            (32, 64),
            slice(150 - 32, 150 + 32),
            slice(0, 32),
            id="left edge overlap",
        ),
        pytest.param(
            (310, 150, 32, 64),
            (32, 64),
            slice(150 - 32, 150 + 32),
            slice(-32, None),
            id="right edge overlap",
        ),
        pytest.param(
            (100, 250, 32, 64),
            (32, 64),
            slice(-64, None),
            slice(100 - 16, 100 + 16),
            id="bottom edge overlap",
        ),
        pytest.param(
            (100, 20, 32, 64),
            (32, 64),
            slice(0, 64),
            slice(100 - 16, 100 + 16),
            id="top edge overlap",
        ),
        pytest.param(
            (100, 150, 640, 64),
            (320, 64),
            slice(150 - 32, 150 + 32),
            slice(None, None),
            id="crop width exceeds original width",
        ),
        pytest.param(
            (100, 150, 32, 512),
            (32, 256),
            slice(None, None),
            slice(100 - 16, 100 + 16),
            id="crop height exceeds original height",
        ),
    ],
)
def test_crop(
    example_8bit_grayscale_tiff: pathlib.Path,
    crop_args: tuple[float, float, int, int],
    expected_size: tuple[int, int],
    expected_rows_slice: slice,
    expected_cols_slice: slice,
) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    # The image is 256 x 320 so we do not hit any edges cropping here.
    cropped = crop(image, *crop_args)
    assert cropped.size == expected_size
    np.testing.assert_equal(
        np.asarray(image)[expected_rows_slice, expected_cols_slice],
        np.asarray(cropped),
    )


def test_resize(example_8bit_grayscale_tiff: pathlib.Path) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    resized = resize(image, 2)
    assert resized.size[0] == 2 * image.size[0]
    assert resized.size[1] == 2 * image.size[1]


def test_stitch_single_image(example_8bit_grayscale_tiff: pathlib.Path) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    stitched = stitch([image])
    assert stitched.size == image.size
    np.testing.assert_equal(np.asarray(image), np.asarray(stitched))


def test_stitch_multiple_images(
    example_8bit_disk_image_sequence: DiskImageSequence,
) -> None:
    stitched = stitch([image for image in example_8bit_disk_image_sequence])
    assert stitched.size == (len(example_8bit_disk_image_sequence) * 320, 256)

    stitched_arr = np.asarray(stitched)
    for i, image in enumerate(example_8bit_disk_image_sequence):
        current_slice = stitched_arr[:, i * 320 : (i + 1) * 320]
        np.testing.assert_equal(np.asarray(image), current_slice)


def test_adjust_contrast(
    example_8bit_grayscale_tiff: pathlib.Path,
) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    adjusted = adjust_contrast(image, 1.5)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(adjusted), np.asarray(image))


def test_adjust_brightness(
    example_8bit_grayscale_tiff: pathlib.Path,
) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    adjusted = adjust_brightness(image, 1.5)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(adjusted), np.asarray(image))


def test_adjust_sharpness(
    example_8bit_grayscale_tiff: pathlib.Path,
) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    adjusted = adjust_sharpness(image, 1.5)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(adjusted), np.asarray(image))


def test_adjust_color(
    example_8bit_rgb_tiff: pathlib.Path,
) -> None:
    image = Image.open(example_8bit_rgb_tiff)
    adjusted = adjust_color(image, 1.5)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(adjusted), np.asarray(image))


def test_apply_auto_contrast(
    example_8bit_grayscale_tiff: pathlib.Path,
) -> None:
    image = Image.open(example_8bit_grayscale_tiff)
    adjusted = apply_auto_contrast(image)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(adjusted), np.asarray(image))


def test_equalize() -> None:
    # Set seed to make sure that we get a random image that does not span the
    # full [0, 255] range, in which case equalize() would have no effect.
    np.random.seed(12345)
    image = create_example_image(8, True)
    equalized = equalize(image)
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(equalized), np.asarray(image))
