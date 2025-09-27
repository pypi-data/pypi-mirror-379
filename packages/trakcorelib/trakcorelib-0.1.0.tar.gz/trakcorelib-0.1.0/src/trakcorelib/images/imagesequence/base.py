"""Image sequence base class definition."""

from __future__ import annotations

import abc
import pathlib
import string
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import os
    from collections.abc import Iterator

    from PIL import Image


class ImageSequence(abc.ABC):
    """Sequence of images."""

    @abc.abstractmethod
    def __len__(self) -> int:
        """Retrieve the number of images in the sequence."""
        ...

    @abc.abstractmethod
    def __getitem__(self, index: int) -> Image.Image:
        """Retrieve the image at the specified index.

        Args:
            index: Index in the sequence of the image to retrieve.

        Returns:
            The image as a Pillow Image object.

        """
        ...

    @property
    @abc.abstractmethod
    def identifiers(self) -> list[str]:
        """Identifiers for all frames."""
        ...

    def __iter__(self) -> Iterator[Image.Image]:
        """Return an iterator over all images in the sequence."""
        for i in range(len(self)):
            yield self[i]

    def by_identifier(self, identifier: str) -> Image.Image:
        """Retrieve the image with the specified identifier.

        Args:
            identifier: Identifier to retrieve the image for.

        Returns:
            The image with the specified identifier.

        """
        index = self.index_by_identifier(identifier)
        return self[index]

    def index_by_identifier(self, identifier: str) -> int:
        """Retrieve an index from an identifier, or raise if it does not exist."""
        try:
            return self.identifiers.index(identifier)
        except ValueError:
            msg = f"No image with identifier {identifier} exists in the sequence."
            raise ValueError(msg) from None

    def save(
        self,
        directory: str | os.PathLike[str],
        filename_pattern: str = "image_{}.tif",
        *,
        do_overwrite: bool = False,
        image_format: str | None = None,
    ) -> None:
        """Save the image sequence to disk.

        Args:
            directory: Directory to save the images to.
            filename_pattern: Filename pattern for each individual image. It
                should be a format string with a single field to be replaced by
                the unique identifier for that image. For example:
                "image_{}.tif", which will create "image_000001.tif",
                "image_000002.tif", ... for identifiers "1", "2", ...
            do_overwrite: Whether to allow overwriting existing files.
            image_format: File format to write the images as, specified as a
                string accepted by Pillow, see: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
                By default, the filename extension is used to determine the file
                format.

        """
        parsed = list(string.Formatter().parse(filename_pattern))
        if len(parsed) != 2:
            msg = (
                "Filename pattern should be a format string with a single "
                'replacement field, for example: "image_{}.tif".'
            )
            raise ValueError(msg)

        directory = pathlib.Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        for i, image in enumerate(self):
            file = directory / filename_pattern.format(self.identifiers[i])
            if not do_overwrite and file.exists():
                msg = f'File "{file}" already exists.'
                raise OSError(msg)
            image.save(file, format=image_format)
