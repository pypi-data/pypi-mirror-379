import pathlib

from trakcorelib.images.read import read_image_as_8bit_grayscale


def test_read_8bit_tiff(example_8bit_grayscale_tiff: pathlib.Path) -> None:
    image = read_image_as_8bit_grayscale(example_8bit_grayscale_tiff)
    assert image.mode == "L"


def test_read_12bit_tiff(example_12bit_grayscale_tiff: pathlib.Path) -> None:
    image = read_image_as_8bit_grayscale(example_12bit_grayscale_tiff)
    assert image.mode == "L"


def test_read_16bit_tiff(example_16bit_grayscale_tiff: pathlib.Path) -> None:
    image = read_image_as_8bit_grayscale(example_16bit_grayscale_tiff)
    assert image.mode == "L"
