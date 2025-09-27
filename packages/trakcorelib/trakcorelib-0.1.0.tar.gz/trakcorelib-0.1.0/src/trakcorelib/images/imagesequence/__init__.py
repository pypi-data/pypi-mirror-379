"""Image sequences.

Different variants exist, for example from disk, from a specific directory, or
in-memory only.
"""

from trakcorelib.images.imagesequence.base import ImageSequence
from trakcorelib.images.imagesequence.disk import (
    DirectoryImageSequence,
    DiskImageSequence,
)
from trakcorelib.images.imagesequence.memory import MemoryImageSequence
from trakcorelib.images.imagesequence.operations import apply

__all__ = [
    "DirectoryImageSequence",
    "DiskImageSequence",
    "ImageSequence",
    "MemoryImageSequence",
    "apply",
]
