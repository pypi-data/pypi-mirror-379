"""Synchronised multi-image sequence class definition."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from trakcorelib.images.imagesequence.base import ImageSequence
from trakcorelib.images.imagesequence.disk import DirectoryImageSequence
from trakcorelib.images.multiimagesequence.base import MultiImageSequence

if TYPE_CHECKING:
    import os
    from collections.abc import Iterable

    from trakcorelib.images.convert import BitDepthConvertMode


T = TypeVar("T", bound=ImageSequence)


class BasicMultiImageSequence(MultiImageSequence[T]):
    """Collection of images sequences."""

    def __init__(
        self,
        sequences: Iterable[T],
        names: Iterable[str] | None = None,
        *,
        require_same_length: bool = True,
    ) -> None:
        """Initialise a multi-image sequence.

        Args:
            sequences: Image sequences to add to the collection.
            names: Optional list of names for the sequences. If not specified,
                sequences are named "seq1", "seq2", ...
            require_same_length: Whether to check that all specified image
                sequences have the same length.

        """
        self._sequences = list(sequences)
        if require_same_length and not all(
            len(sequence) == len(self._sequences[0]) for sequence in self._sequences
        ):
            msg = (
                "All image sequences in a synchronised multi-image sequence "
                "must have the same length."
            )
            raise ValueError(msg)

        if names is None:
            self._names = [f"seq{i + 1}" for i in range(len(self._sequences))]
        else:
            self._names = list(names)
            if len(self._names) != len(self._sequences):
                msg = "Specify the same number of names as image sequences."
                raise ValueError(msg)

    @property
    def names(self) -> list[str]:
        """Names of all sequences in the collection."""
        return self._names

    def __len__(self) -> int:
        """Retrieve the number of sequences in the collection."""
        return len(self._sequences)

    def __getitem__(self, index: int) -> T:
        """Retrieve the sequence at the specified index.

        Args:
            index: Index of the sequence to retrieve.

        Returns:
            The image sequence.

        """
        return self._sequences[index]

    @staticmethod
    def from_glob(  # noqa: PLR0913  many arguments because of configurability
        directories: Iterable[str | os.PathLike[str]],
        filename_glob: str | Iterable[str],
        names: Iterable[str] | None = None,
        *,
        require_same_length: bool = True,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
    ) -> BasicMultiImageSequence[DirectoryImageSequence]:
        """Create a multi-image sequence from directories and regex pattern(s).

        Args:
            directories: Root directories of the images for each sequence.
            filename_glob: Glob (e.g. "*.tif") or multiple globs matching images
                in the sequence. The same glob is use for all directories.
            names: Optional list of names for the sequences. If not specified,
                sequences are named "seq1", "seq2", ...
            require_same_length: Whether to check that all specified image
                sequences have the same length.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.

        """
        sequences = (
            DirectoryImageSequence.from_glob(
                directory,
                filename_glob,
                do_convert_to_8bit_grayscale=do_convert_to_8bit_grayscale,
                convert_mode=convert_mode,
            )
            for directory in directories
        )
        return BasicMultiImageSequence(
            sequences,
            names,
            require_same_length=require_same_length,
        )

    @staticmethod
    def from_regex(  # noqa: PLR0913  many arguments because of configurability
        directories: Iterable[str | os.PathLike[str]],
        pattern: str | Iterable[str],
        names: Iterable[str] | None = None,
        *,
        require_same_length: bool = True,
        do_convert_to_8bit_grayscale: bool = False,
        convert_mode: BitDepthConvertMode = "high",
    ) -> BasicMultiImageSequence[DirectoryImageSequence]:
        r"""Create a directory image sequence from a directory and a regex pattern.

        Args:
            directories: Root directories of the images for each sequence.
            pattern: Regular expression pattern(s) that matches image filenames
                and has one group that contains the numeric identifier. For
                example: 'image_(\d{6})\.tif'. Either a single pattern for all
                directories, or one pattern per directory may be specified.
            names: Optional list of names for the sequences. If not specified,
                sequences are named "seq1", "seq2", ...
            require_same_length: Whether to check that all specified image
                sequences have the same length.
            do_convert_to_8bit_grayscale: Whether to convert images to 8-bit
                grayscale upon reading them.
            convert_mode: Method used to convert images with higher bit depth to
                8-bits, if enabled.

        """
        directories = list(directories)
        if isinstance(pattern, str):
            patterns = [pattern] * len(directories)
        else:
            patterns = list(pattern)
            if len(patterns) != len(directories):
                msg = (
                    "Specify either a single pattern, or the same number of "
                    "patterns as directories."
                )
                raise ValueError(msg)

        sequences = (
            DirectoryImageSequence.from_regex(
                directory,
                pattern,
                do_convert_to_8bit_grayscale=do_convert_to_8bit_grayscale,
                convert_mode=convert_mode,
            )
            for directory, pattern in zip(directories, patterns)
        )
        return BasicMultiImageSequence(
            sequences,
            names,
            require_same_length=require_same_length,
        )
