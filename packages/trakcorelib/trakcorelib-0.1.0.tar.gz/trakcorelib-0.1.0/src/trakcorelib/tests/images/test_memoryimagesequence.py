import numpy as np
from PIL import Image

from trakcorelib.images.imagesequence.memory import MemoryImageSequence


def test_new_8bit_grayscale() -> None:
    sequence = MemoryImageSequence.new_8bit_grayscale(10, (16, 16))
    assert len(sequence) == 10
    for image in sequence:
        assert image.mode == "L"
        assert image.size == (16, 16)
        np.testing.assert_equal(np.asarray(image), np.zeros((16, 16)))


def test_set_item() -> None:
    sequence = MemoryImageSequence.new_8bit_grayscale(10, (16, 16))

    np.testing.assert_equal(np.asarray(sequence[3]), np.zeros((16, 16)))
    sequence[3] = Image.fromarray(np.ones((16, 16)))
    np.testing.assert_equal(np.asarray(sequence[3]), np.ones((16, 16)))


def test_append() -> None:
    sequence = MemoryImageSequence.empty()
    assert len(sequence) == 0

    sequence.append(Image.new("L", (16, 32)))
    assert len(sequence) == 1
    np.testing.assert_equal(np.asarray(sequence[0]), np.zeros((32, 16)))


def test_insert() -> None:
    sequence = MemoryImageSequence.new_8bit_grayscale(10, (16, 16))

    assert len(sequence) == 10
    sequence.insert(3, Image.new("L", (16, 32)))
    assert len(sequence) == 11

    np.testing.assert_equal(np.asarray(sequence[3]), np.zeros((32, 16)))
