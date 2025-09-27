"""Disk image sequences."""

from __future__ import annotations

import pathlib
import re
from typing import TYPE_CHECKING

from PIL import Image

from trakcorelib.images.filenames import (
    find_file_identifiers,
    generate_default_identifiers,
)
from trakcorelib.images.imagesequence.base import ImageSequence
from trakcorelib.images.imagesequence.memory import MemoryImageSequence
from trakcorelib.images.read import read_image_as_8bit_grayscale

if TYPE_CHECKING:
    import os
    from collections.abc import Iterable

    from trakcorelib.images.convert import BitDepthConvertMode


class DiskImageSequence(ImageSequence):
    """Sequence of images read from disk."""

    def __init__(
        self,
        paths: Iterable[str | os.PathLike[str]],
        identifiers: Iterable[str] | None = None,
        *,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
    ) -> None:
        r"""Initialise a sequence of images on disk.

        Images are sorted by their identifier.

        Args:
            paths: Paths to the images. The order of these files will
                be preserved as the indexing order of the sequence.
            identifiers: Optional identifiers for each of the paths, if
                not specified, 0-based indices (i.e. "0", "1", "2", ...) are
                used.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.

        """
        # Generate absolute paths, extract identifiers and sort both by their
        # identifier.
        parsed_paths = [pathlib.Path(path) for path in paths]
        if identifiers is None:
            identifiers = generate_default_identifiers(len(parsed_paths))
        else:
            identifiers = list(identifiers)
            if len(parsed_paths) != len(identifiers):
                msg = "Specify the same number of image paths as identifiers."
                raise ValueError(msg)

        self._paths: list[pathlib.Path] = []
        self._identifiers: list[str] = []
        for path, identifier in sorted(
            zip(parsed_paths, identifiers),
            key=lambda pair: pair[1],
        ):
            self._paths.append(path)
            self._identifiers.append(identifier)

        self._cache: dict[pathlib.Path, Image.Image] = {}

        self._do_convert_to_8bit_grayscale = do_convert_to_8bit_grayscale
        self._convert_mode: BitDepthConvertMode = convert_mode

    @property
    def identifiers(self) -> list[str]:
        """Identifiers for all frames."""
        return self._identifiers

    @property
    def paths(self) -> list[pathlib.Path]:
        """Paths to all images in the sequence."""
        return self._paths

    def __len__(self) -> int:
        """Retrieve the number of images in the sequence."""
        return len(self._paths)

    def __getitem__(self, index: int) -> Image.Image:
        """Retrieve the image at the specified index.

        If the image is not in the cache, read it from the disk. Otherwise, use
        the image in the cache.

        Args:
            index: Index in the sequence of the image to retrieve.

        Returns:
            The image at the specified index.

        """
        return self._get_image(index, do_cache=True)

    def path_by_identifier(self, identifier: str) -> pathlib.Path:
        """Retrieve the path of the image with the specified identifier.

        Args:
            identifier: Identifier to retrieve the image path for.

        Returns:
            Path to the image with the specified identifier.

        """
        index = self.index_by_identifier(identifier)
        return self._paths[index]

    def is_cached(self, index: int) -> bool:
        """Check whether the image at the specified index is in the cache."""
        return self._paths[index] in self._cache

    def clear_cache(self) -> None:
        """Remove all images from the cache.

        This frees up the memory used by the image sequence.
        """
        self._cache.clear()

    def to_memory_image_sequence(
        self,
        *,
        do_cache: bool = False,
    ) -> MemoryImageSequence:
        """Create a memory image sequence from this disk image sequence.

        This reads all images from disk and copies them into an in-memory image
        sequence.

        Args:
            do_cache: Whether to cache images in the current image sequence when
                reading.

        Returns:
            An in-memory sequence containing all images from a disk image
            sequence.

        """
        images = (
            self._get_image(index, do_cache=do_cache) for index in range(len(self))
        )
        return MemoryImageSequence(images, self._identifiers)

    def _get_image(self, index: int, *, do_cache: bool) -> Image.Image:
        """Retrieve the image at the specified index.

        If specified, the read image will be cached so it does not need to be
        read from disk the next time.

        Even if read images are not cached, the cache is always used to read
        from.
        """
        image_path = self._paths[index]

        # Check whether we have the image in the cache, if we do, return a copy
        # if we don't, read the image and return a copy. We return copies
        # because Pillow images are mutable (with .paste) and we do not want to
        # modify the cache as that may lead to surprising results.
        cached = self._cache.get(image_path)
        if cached is not None:
            return cached.copy()
        image = self._read_image(image_path)
        if do_cache:
            self._cache[image_path] = image
            return image.copy()
        return image

    def _read_image(self, path: pathlib.Path) -> Image.Image:
        """Read the image at the specified path."""
        if self._do_convert_to_8bit_grayscale:
            return read_image_as_8bit_grayscale(path, self._convert_mode)
        return Image.open(path)


class DirectoryImageSequence(DiskImageSequence):
    """Sequence of images read from a single directory on disk."""

    def __init__(
        self,
        directory: str | os.PathLike[str],
        filenames: Iterable[str],
        identifiers: Iterable[str] | None = None,
        *,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
    ) -> None:
        r"""Initialise a directory image sequence.

        Args:
            directory: Root directory of the images.
            filenames: Filenames of images in the sequence. The order of these
                filenames will be preserved as the indexing order of the
                sequence.
            identifiers: Optional identifiers for each of the paths, if not
                specified, 0-based indices (i.e. "0", "1", "2", ...) are used.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.

        """
        self._directory = pathlib.Path(directory)

        # Create an absolute path for every image file.
        paths = [self._directory / filename for filename in filenames]

        super().__init__(
            paths,
            identifiers,
            do_convert_to_8bit_grayscale=do_convert_to_8bit_grayscale,
            convert_mode=convert_mode,
        )

    @property
    def directory(self) -> pathlib.Path:
        """Root directory that the images for this sequence are in."""
        return self._directory

    @property
    def filenames(self) -> list[str]:
        """Filenames of all image files."""
        return [path.name for path in self.paths]

    @staticmethod
    def from_glob(
        directory: str | os.PathLike[str],
        filename_glob: str | Iterable[str],
        *,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
        identifier_pattern: str | None = None,
    ) -> DirectoryImageSequence:
        r"""Create a directory image sequence from a directory and a glob pattern.

        Args:
            directory: Root directory of the images.
            filename_glob: Glob (e.g. "*.tif") or multiple globs matching images
                in the sequence.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.
            identifier_pattern: Optional regular expression pattern that matches
                the file name and has one group that contains the numeric
                identifier. For example: 'image_(\d{6})\.tif'. If not specified,
                image identifiers are determined by finding a common prefix and
                suffix and assuming that what is left is an identifier.

        """
        directory = pathlib.Path(directory)

        # Create an absolute path for every image file matching the glob.
        if isinstance(filename_glob, str):
            files = directory.glob(filename_glob)
        else:
            files = (file for glob in filename_glob for file in directory.glob(glob))

        paths = [directory / file for file in files]
        filenames = (file.name for file in paths)

        # Find identifiers from the image filenames.
        identifiers = find_file_identifiers(paths, identifier_pattern)

        return DirectoryImageSequence(
            directory,
            filenames,
            identifiers,
            do_convert_to_8bit_grayscale=do_convert_to_8bit_grayscale,
            convert_mode=convert_mode,
        )

    @staticmethod
    def from_regex(
        directory: str | os.PathLike[str],
        pattern: str,
        *,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
    ) -> DirectoryImageSequence:
        r"""Create a directory image sequence from a directory and a regex pattern.

        Args:
            directory: Root directory of the images.
            pattern: Regular expression pattern that matches image filenames and
                has one group that contains the numeric identifier. For example:
                'image_(\d{6})\.tif'.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.

        """
        directory = pathlib.Path(directory)

        # Create an absolute path for every image file matching the pattern.
        filenames = [
            file.name
            for file in directory.iterdir()
            if file.is_file() and re.match(pattern, file.name) is not None
        ]
        identifiers = find_file_identifiers(filenames, pattern)

        return DirectoryImageSequence(
            directory,
            filenames,
            identifiers,
            do_convert_to_8bit_grayscale=do_convert_to_8bit_grayscale,
            convert_mode=convert_mode,
        )
