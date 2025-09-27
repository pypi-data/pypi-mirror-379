import pathlib

import pytest

from trakcorelib.images import DiskImageSequence

from trakcorelib.tests.images.utils import (
    create_example_tiff,
    create_example_tiff_sequence,
)


@pytest.fixture(scope="session")
def example_8bit_grayscale_tiff(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    return create_example_tiff(
        tmp_path_factory, "example_8bit_grayscale.tiff", 8, is_grayscale=True
    )


@pytest.fixture(scope="session")
def example_12bit_grayscale_tiff(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    return create_example_tiff(
        tmp_path_factory, "example_12bit_grayscale.tiff", 12, is_grayscale=True
    )


@pytest.fixture(scope="session")
def example_16bit_grayscale_tiff(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    return create_example_tiff(
        tmp_path_factory, "example_16bit_grayscale.tiff", 16, is_grayscale=True
    )


@pytest.fixture(scope="session")
def example_8bit_rgb_tiff(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    return create_example_tiff(
        tmp_path_factory, "example_8bit_rgb.tiff", 8, is_grayscale=False
    )


@pytest.fixture(scope="session")
def example_image_8bit_sequence_paths(
    tmp_path_factory: pytest.TempPathFactory,
) -> list[pathlib.Path]:
    root_directory = tmp_path_factory.mktemp("8bit_image_sequence")
    return create_example_tiff_sequence(root_directory, 10, 8)


@pytest.fixture(scope="session")
def example_image_16bit_sequence_paths(
    tmp_path_factory: pytest.TempPathFactory,
) -> list[pathlib.Path]:
    root_directory = tmp_path_factory.mktemp("16bit_image_sequence")
    return create_example_tiff_sequence(root_directory, 10, 16)


@pytest.fixture()
def example_8bit_disk_image_sequence(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> DiskImageSequence:
    identifiers = [
        f"{i:06d}" for i in range(1, len(example_image_8bit_sequence_paths) + 1)
    ]
    return DiskImageSequence(example_image_8bit_sequence_paths, identifiers)
