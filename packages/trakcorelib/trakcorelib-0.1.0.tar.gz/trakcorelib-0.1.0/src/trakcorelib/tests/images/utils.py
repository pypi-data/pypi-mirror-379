from __future__ import annotations

import pathlib

import numpy as np
import PIL.Image as Image
import pytest


def create_example_tiff_sequence(
    root_directory: pathlib.Path, num_images: int, bit_depth: int
) -> list[pathlib.Path]:
    image_paths: list[pathlib.Path] = []
    for i in range(num_images):
        # Name the files with an identifier starting with 1 instead of 0.
        image_path = root_directory / f"image_{i + 1:06d}.tif"
        image = create_example_image(bit_depth, is_grayscale=True)
        image.save(image_path, "tiff")
        image_paths.append(image_path)
    return image_paths


def create_example_tiff(
    tmp_path_factory: pytest.TempPathFactory,
    name: str,
    bit_depth: int,
    is_grayscale: bool,
) -> pathlib.Path:
    image = create_example_image(bit_depth, is_grayscale)
    image_path = tmp_path_factory.mktemp("images") / name
    image.save(image_path, "TIFF")
    return image_path


def create_example_random_image(
    bit_depth: int,
    is_grayscale: bool = True,
    random_value_range: tuple[int, int] | None = None,
) -> Image.Image:
    return create_example_image(
        bit_depth, is_grayscale=is_grayscale, random_value_range=random_value_range
    )


def create_example_constant_image(bit_depth: int, constant_value: int) -> Image.Image:
    return create_example_image(bit_depth, constant_value=constant_value)


def create_example_image(
    bit_depth: int,
    is_grayscale: bool = True,
    constant_value: int | None = None,
    random_value_range: tuple[int, int] | None = None,
) -> Image.Image:
    if bit_depth < 1:
        raise ValueError("Specify a bit depth larger than 0.")
    if bit_depth > 16:
        raise ValueError(
            "Creating images with a bit depth higher than 16 is not supported."
        )
    if bit_depth > 8 and not is_grayscale:
        raise ValueError(
            "Creating colour images with a bit depth higher than 8 is not supported."
        )

    # Create random image.
    max_value = 2**bit_depth - 1
    width = 256
    height = 320
    size = (width, height) if is_grayscale else (width, height, 3)
    dtype = np.uint8 if bit_depth <= 8 else np.uint16
    if constant_value is not None:
        data = np.full(size, constant_value, dtype=dtype)
    else:
        range = random_value_range if random_value_range is not None else (0, max_value)
        data = np.random.randint(range[0], range[1], size, dtype=dtype)

        # Make sure we have at least one minimum value and one maximum value.
        def get_random_index() -> int:
            return np.random.randint(data.size)

        data.flat[get_random_index()] = range[0]
        data.flat[get_random_index()] = range[1]

    mode = determine_image_mode(bit_depth, is_grayscale)
    return Image.fromarray(data, mode=mode)


def determine_image_mode(bit_depth: int, is_grayscale: bool) -> str:
    if is_grayscale:
        return "L" if bit_depth <= 8 else "I;16"
    else:
        return "RGB"
