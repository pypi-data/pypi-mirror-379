"""Operations on entire memory sequences."""

from typing import Any, Callable

from PIL import Image

from trakcorelib.images.imagesequence.base import ImageSequence
from trakcorelib.images.imagesequence.memory import MemoryImageSequence


def apply(
    sequence: ImageSequence,
    func: Callable[[Image.Image, Any], Image.Image],
    *args: Any,  # noqa: ANN401  we cannot do better than Any in Python 3.9
    **kwargs: Any,  # noqa: ANN401  we cannot do better than Any in Python 3.9
) -> MemoryImageSequence:
    """Apply a function to all images in an image sequence.

    Args:
        sequence: Sequence to apply the function to.
        func: Function to apply to all images in the sequence. It should
            accept a Pillow Image object as the first argument, followed by
            any number of positional and keyword arguments, and return a
            Pillow Image object.
        args: Positional arguments for the function, following the first
            argument which should always be an image.
        kwargs: Keyword arguments for the function.

    Returns:
        An image sequence with the result of the applied operation to all
        images.

    """
    images = (func(image, *args, **kwargs) for image in sequence)
    return MemoryImageSequence(images)
