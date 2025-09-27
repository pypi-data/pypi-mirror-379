import pytest

from trakcorelib.images.imagesequence import MemoryImageSequence
from trakcorelib.images.multiimagesequence import BasicMultiImageSequence
from trakcorelib.tests.images.utils import create_example_tiff_sequence


def test_create_basic_multiimagesequence_default_names() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    synchronised = BasicMultiImageSequence(sequences)
    assert len(synchronised) == 3
    assert synchronised.names == ["seq1", "seq2", "seq3"]


def test_create_basic_multiimagesequence_with_names() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    names = ["cam1", "cam2", "cam3"]
    synchronised = BasicMultiImageSequence(sequences, names)
    assert len(synchronised) == 3
    assert synchronised.names == names


def test_create_basic_multiimagesequence_mismatching_sequence_length() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(11, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    with pytest.raises(ValueError):
        _ = BasicMultiImageSequence(sequences)


def test_create_basic_multiimagesequence_mismatching_sequence_length_no_check() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(11, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    # Should succeed despite different image sequence lengths.
    _ = BasicMultiImageSequence(sequences, require_same_length=False)


def test_create_basic_multiimagesequence_mismatching_names_length() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    names = ["cam1", "cam2"]
    with pytest.raises(ValueError):
        _ = BasicMultiImageSequence(sequences, names)


def test_get_item() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    synchronised = BasicMultiImageSequence(sequences)
    assert synchronised[0] is sequences[0]
    assert synchronised[1] is sequences[1]
    assert synchronised[2] is sequences[2]
    with pytest.raises(IndexError):
        _ = synchronised[3]


def test_iterate() -> None:
    sequences = [
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
        MemoryImageSequence.new_8bit_grayscale(10, (16, 16)),
    ]
    synchronised = BasicMultiImageSequence(sequences)
    for i, sequence in enumerate(synchronised):
        assert sequence is sequences[i]


def test_create_from_single_glob(tmp_path_factory: pytest.TempPathFactory) -> None:
    directories = [
        tmp_path_factory.mktemp("sequence_1"),
        tmp_path_factory.mktemp("sequence_2"),
        tmp_path_factory.mktemp("sequence_3"),
    ]
    for directory in directories:
        create_example_tiff_sequence(directory, 10, 8)

    sequences = BasicMultiImageSequence.from_glob(directories, "image_*.tif")
    assert len(sequences) == 3

    for i, sequence in enumerate(sequences):
        assert sequence.directory == directories[i]
        assert len(sequence) == 10


def test_create_from_multiple_globs(tmp_path_factory: pytest.TempPathFactory) -> None:
    directories = [
        tmp_path_factory.mktemp("sequence_1"),
        tmp_path_factory.mktemp("sequence_2"),
        tmp_path_factory.mktemp("sequence_3"),
    ]
    for directory in directories:
        create_example_tiff_sequence(directory, 10, 8)

    sequences = BasicMultiImageSequence.from_glob(directories, ("image*.tif", "*.jpg"))
    assert len(sequences) == 3

    for i, sequence in enumerate(sequences):
        assert sequence.directory == directories[i]
        assert len(sequence) == 10


def test_create_from_single_regex(tmp_path_factory: pytest.TempPathFactory) -> None:
    directories = [
        tmp_path_factory.mktemp("sequence_1"),
        tmp_path_factory.mktemp("sequence_2"),
        tmp_path_factory.mktemp("sequence_3"),
    ]
    for directory in directories:
        create_example_tiff_sequence(directory, 10, 8)

    sequences = BasicMultiImageSequence.from_regex(directories, r"image_(\d+)\.tif")
    assert len(sequences) == 3

    for i, sequence in enumerate(sequences):
        assert sequence.directory == directories[i]
        assert len(sequence) == 10


def test_create_from_multiple_regexes(tmp_path_factory: pytest.TempPathFactory) -> None:
    directories = [
        tmp_path_factory.mktemp("sequence_1"),
        tmp_path_factory.mktemp("sequence_2"),
        tmp_path_factory.mktemp("sequence_3"),
    ]
    for directory in directories:
        create_example_tiff_sequence(directory, 10, 8)

    sequences = BasicMultiImageSequence.from_regex(
        directories, (r"image_(\d+)\.tif", r".*(\d{6}).*", r"image_([0-9]+)\.tif$")
    )
    assert len(sequences) == 3

    for i, sequence in enumerate(sequences):
        assert sequence.directory == directories[i]
        assert len(sequence) == 10
