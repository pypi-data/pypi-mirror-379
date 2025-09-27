import numpy as np
from PIL import Image
import pytest

from trakcorelib.images.imagesequence.disk import DiskImageSequence
from trakcorelib.images.imagesequence.memory import MemoryImageSequence


def test_save_disk_image_sequence(
    example_8bit_disk_image_sequence: DiskImageSequence,
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    dest_directory = tmp_path_factory.mktemp("saved_disk_image_sequence")
    # Write as TIFF so images can be read back exactly as they are written.
    example_8bit_disk_image_sequence.save(dest_directory, "image_{}.tif")

    files = sorted(list(dest_directory.glob("*.tif")))
    assert len(files) == len(example_8bit_disk_image_sequence)
    for i, file in enumerate(files):
        assert file.exists()
        # Image identifiers for the example sequence start at 1, verify that
        # they have been used correctly.
        assert file.name == f"image_{i + 1:06d}.tif"

        written = Image.open(file)
        np.testing.assert_equal(
            np.asarray(written), np.asarray(example_8bit_disk_image_sequence[i])
        )


def test_save_memory_image_sequence(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    sequence = MemoryImageSequence.new_8bit_grayscale(10, (16, 16))

    dest_directory = tmp_path_factory.mktemp("saved_memory_image_sequence")
    sequence.save(dest_directory, "frame_{}.tif")

    files = sorted(list(dest_directory.glob("*.tif")))
    assert len(files) == 10
    for file in files:
        assert file.exists()
        written = Image.open(file)
        np.testing.assert_equal(np.asarray(written), np.zeros((16, 16)))


def test_save_memory_image_sequence_overwrite(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    sequence = MemoryImageSequence.new_8bit_grayscale(10, (16, 16))

    dest_directory = tmp_path_factory.mktemp("saved_memory_image_sequence")
    pattern = "frame_{}.tif"
    sequence.save(dest_directory, pattern)

    # Writing the sequence to the same directory without overwrite enabled
    # should fail.
    with pytest.raises(IOError):
        sequence.save(dest_directory, pattern, do_overwrite=False)
    # Writing it with overwrite enabled should succeed.
    sequence.save(dest_directory, pattern, do_overwrite=True)
