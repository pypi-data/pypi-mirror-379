import pathlib
import random

import pytest

from trakcorelib.images import DirectoryImageSequence


def test_create_directory_image_sequence_from_paths(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    directory = example_image_8bit_sequence_paths[0].parent
    filenames = [path.name for path in example_image_8bit_sequence_paths]

    # Shuffle pathnames to test sorting by identifier.
    random.shuffle(filenames)

    sequence = DirectoryImageSequence(directory, filenames)
    assert len(sequence) == len(example_image_8bit_sequence_paths)
    assert sequence.directory == directory


def test_create_directory_image_sequence_from_glob(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    directory = example_image_8bit_sequence_paths[0].parent
    pattern = "*.tif"

    sequence = DirectoryImageSequence.from_glob(directory, pattern)
    assert len(sequence) == len(example_image_8bit_sequence_paths)
    assert sequence.directory == directory

    # Check whether the paths are stored in identifier order.
    for i, path in enumerate(sequence.paths):
        assert path.name == f"image_{i + 1:06d}.tif"


def test_create_directory_image_sequence_single_extension_from_multiple_globs(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    directory = example_image_8bit_sequence_paths[0].parent

    # Adding more globs that do not match any files should make no difference.
    sequence = DirectoryImageSequence.from_glob(directory, ["*.tif", "*.jpg", "*.png"])
    assert len(sequence) == len(example_image_8bit_sequence_paths)
    assert sequence.directory == directory

    # Check whether the paths are stored in identifier order.
    for i, path in enumerate(sequence.paths):
        assert path.name.startswith(f"image_{i + 1:06d}")


def test_create_directory_image_sequence__multiple_extensions_from_multiple_globs(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    directory = example_image_8bit_sequence_paths[0].parent

    # Also create an empty .jpg file in the directory.
    (directory / "image_000011.jpg").touch()

    sequence = DirectoryImageSequence.from_glob(directory, ["*.tif", "*.jpg"])
    assert len(sequence) == len(example_image_8bit_sequence_paths) + 1
    assert sequence.directory == directory

    # Check whether the paths are stored in identifier order.
    for i, path in enumerate(sequence.paths):
        assert path.name.startswith(f"image_{i + 1:06d}")


def test_create_directory_image_sequence_from_regex(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    directory = example_image_8bit_sequence_paths[0].parent
    pattern = r"image_(\d+)\.tif"

    sequence = DirectoryImageSequence.from_regex(directory, pattern)
    assert len(sequence) == len(example_image_8bit_sequence_paths)
    assert sequence.directory == directory

    # Check whether the paths are stored in identifier order.
    for i, path in enumerate(sequence.paths):
        assert path.name == f"image_{i + 1:06d}.tif"


def test_create_empty_directory_image_sequence(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    # This directory is guaranteed to contain no image files.
    directory = tmp_path_factory.mktemp("empty_sequence")
    sequence = DirectoryImageSequence.from_glob(directory, "*.tif")
    assert len(sequence) == 0
    assert sequence.directory == directory
