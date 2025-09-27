"""In-memory image sequence."""

from __future__ import annotations

from typing import TYPE_CHECKING

from PIL import Image

from trakcorelib.images.filenames import generate_default_identifiers
from trakcorelib.images.imagesequence.base import ImageSequence

if TYPE_CHECKING:
    from collections.abc import Iterable


class MemoryImageSequence(ImageSequence):
    """A mutable image sequence that resides in memory."""

    def __init__(
        self,
        images: Iterable[Image.Image],
        identifiers: Iterable[str] | None = None,
    ) -> None:
        """Initialise a memory image sequence.

        Args:
            images: Images that form the sequence.
            identifiers: Optional identifiers for each of the paths, if
                not specified, 0-based indices (i.e. "0", "1", "2", ...) are
                used.

        """
        self._images = list(images)
        if identifiers is None:
            self._identifiers = generate_default_identifiers(len(self._images))
        else:
            self._identifiers = list(identifiers)
            if len(self._images) != len(self._identifiers):
                msg = "Should have the same number of identifiers as images."
                raise ValueError(msg)

    @property
    def identifiers(self) -> list[str]:
        """Numeric identifiers for all frames."""
        return self._identifiers

    def __len__(self) -> int:
        """Retrieve the number of images in the sequence."""
        return len(self._images)

    def __getitem__(self, index: int) -> Image.Image:
        """Retrieve the image at the specified index.

        This is a reference to the image in the sequence, not a copy; mutating
        the image will also change it in the image sequence object.

        Args:
            index: Index in the sequence of the image to retrieve.

        Returns:
            The image at the specified index.

        """
        return self._images[index]

    def __setitem__(self, index: int, image: Image.Image) -> None:
        """Set the image at the specified index.

        Args:
            index: Index in the sequence of the image to set.
            image: Image to set.

        """
        self._images[index] = image

    def append(self, image: Image.Image) -> None:
        """Append an image to the sequence.

        Args:
            image: Image to append.

        """
        self._images.append(image)

    def insert(self, index: int, image: Image.Image) -> None:
        """Insert an image into the sequence.

        Args:
            index: Index at which to insert the image.
            image: Image to insert.

        """
        self._images.insert(index, image)

    @staticmethod
    def new_8bit_grayscale(
        num_images: int,
        size: tuple[int, int],
    ) -> MemoryImageSequence:
        """Create a sequence of 8-bit grayscale images.

        All images are initialised to all zeros (i.e. black).

        Args:
            num_images: Number of images in the sequence.
            size: A 2-tuple with the width and height of all images in the
                sequence.

        Returns:
            An in-memory sequence of black images.

        """
        images = (Image.new("L", size) for _ in range(num_images))
        return MemoryImageSequence(images)

    @staticmethod
    def empty() -> MemoryImageSequence:
        """Create an empty in-memory image sequence."""
        return MemoryImageSequence([])
