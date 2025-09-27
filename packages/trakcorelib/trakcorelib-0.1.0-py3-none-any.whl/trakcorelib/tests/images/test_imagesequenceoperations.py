from trakcorelib.images.imagesequence import DiskImageSequence, apply
from trakcorelib.images.operations import resize


def test_image_sequence_apply_resize(
    example_8bit_disk_image_sequence: DiskImageSequence,
) -> None:
    resized = apply(example_8bit_disk_image_sequence, resize, size_multiplier=2.0)
    assert len(resized) == len(example_8bit_disk_image_sequence)
    for i, resized_image in enumerate(resized):
        assert resized_image.size[0] == 2 * example_8bit_disk_image_sequence[i].size[0]
        assert resized_image.size[1] == 2 * example_8bit_disk_image_sequence[i].size[1]
