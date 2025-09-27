import pathlib

import numpy as np
from PIL import Image
import pytest

from trakcorelib.images import DiskImageSequence


def test_create_disk_image_sequence_from_paths(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    sequence = DiskImageSequence(example_image_8bit_sequence_paths)
    assert len(sequence) == len(example_image_8bit_sequence_paths)


def test_read_image_at_index(
    example_image_8bit_sequence_paths: list[pathlib.Path],
) -> None:
    sequence = DiskImageSequence(example_image_8bit_sequence_paths)

    reference = Image.open(example_image_8bit_sequence_paths[3])
    image = sequence[3]
    np.testing.assert_equal(np.asarray(image), np.asarray(reference))

    # Modifying the image should not affect the original image sequence.
    image.paste(Image.new("L", (4, 4)))
    np.testing.assert_equal(np.asarray(sequence[3]), np.asarray(reference))
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(image), np.asarray(sequence[3]))

    # Also for the second time, when it is fetched from the cache immediately.
    image_cached = sequence[3]
    image_cached.paste(Image.new("L", (4, 4)))
    np.testing.assert_equal(np.asarray(sequence[3]), np.asarray(reference))
    with pytest.raises(AssertionError):
        np.testing.assert_equal(np.asarray(image_cached), np.asarray(sequence[3]))


def test_clear_cache(example_8bit_disk_image_sequence: DiskImageSequence) -> None:
    # The sequence starts out without any cached images.
    assert all(
        (
            not example_8bit_disk_image_sequence.is_cached(i)
            for i in range(len(example_8bit_disk_image_sequence))
        )
    )

    # Reading an image should cache it.
    _image = example_8bit_disk_image_sequence[3]
    assert example_8bit_disk_image_sequence.is_cached(3)

    # Clearing the cache should remove it again.
    example_8bit_disk_image_sequence.clear_cache()
    assert all(
        (
            not example_8bit_disk_image_sequence.is_cached(i)
            for i in range(len(example_8bit_disk_image_sequence))
        )
    )


def test_iterate_images(example_8bit_disk_image_sequence: DiskImageSequence) -> None:
    iter_count = 0
    for image in example_8bit_disk_image_sequence:
        assert image is not None
        iter_count += 1
    assert iter_count == len(example_8bit_disk_image_sequence)


def to_memory_image_sequence(example_disk_image_sequence: DiskImageSequence) -> None:
    sequence = example_disk_image_sequence.to_memory_image_sequence()
    assert len(sequence) == len(example_disk_image_sequence)
    assert sequence.identifiers == example_disk_image_sequence.identifiers
    for i, image in enumerate(sequence):
        # Contents of the image should be the same.
        np.testing.assert_equal(np.asarray(image), sequence[i])
        # But it should be a copy, not the same Image object.
        assert image is not sequence[i]


def test_by_identifier(example_8bit_disk_image_sequence: DiskImageSequence) -> None:
    path = example_8bit_disk_image_sequence.path_by_identifier("000003")
    assert path.name == "image_000003.tif"
    assert path == example_8bit_disk_image_sequence.paths[2]

    image = example_8bit_disk_image_sequence.by_identifier("000003")
    reference_image = Image.open(path)
    np.testing.assert_equal(np.asarray(image), np.asarray(reference_image))


def test_create_disk_image_sequence_from_16bit_paths_no_convert(
    example_image_16bit_sequence_paths: list[pathlib.Path],
) -> None:
    sequence = DiskImageSequence(example_image_16bit_sequence_paths)
    assert len(sequence) == len(example_image_16bit_sequence_paths)
    for image in sequence:
        assert image.mode == "I;16"


def test_create_disk_image_sequence_from_16bit_paths_convert_to_8bit(
    example_image_16bit_sequence_paths: list[pathlib.Path],
) -> None:
    sequence = DiskImageSequence(
        example_image_16bit_sequence_paths, do_convert_to_8bit_grayscale=True
    )
    assert len(sequence) == len(example_image_16bit_sequence_paths)
    for image in sequence:
        assert image.mode == "L"
