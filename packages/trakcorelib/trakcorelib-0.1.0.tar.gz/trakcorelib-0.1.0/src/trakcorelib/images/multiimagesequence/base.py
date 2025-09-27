"""Multi-image sequence base class definition."""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Generic, TypeVar

from trakcorelib.images.imagesequence.base import ImageSequence

if TYPE_CHECKING:
    from collections.abc import Iterator


T = TypeVar("T", bound=ImageSequence)


class MultiImageSequence(Generic[T]):
    """Collection of related image sequences."""

    @property
    @abc.abstractmethod
    def names(self) -> list[str]:
        """Names of all sequences in the collection."""
        ...

    @abc.abstractmethod
    def __len__(self) -> int:
        """Retrieve the number of sequences in the collection."""
        ...

    @abc.abstractmethod
    def __getitem__(self, index: int) -> T:
        """Retrieve the sequence at the specified index.

        Args:
            index: Index of the sequence to retrieve.

        Returns:
            The image sequence.

        """
        ...

    def __iter__(self) -> Iterator[T]:
        """Return an iterator over all sequences in the collection."""
        for i in range(len(self)):
            yield self[i]
