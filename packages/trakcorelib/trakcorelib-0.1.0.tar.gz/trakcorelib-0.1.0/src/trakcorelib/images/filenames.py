"""Functions for extracting information from image filenames."""

from __future__ import annotations

import pathlib
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import os
    from collections.abc import Iterable, Sequence


def find_file_identifiers(
    files: Iterable[str | os.PathLike[str]],
    pattern: str | None = None,
) -> list[str]:
    r"""Find identifying numbers contained in filenames.

    This function will try to find unique identifiers that change between
    filenames.

    By default, it tries to find a common prefix and postfix and assumes that
    what is left are the unique identifiers. In this process, it ignores the
    file extension.

    Alternatively, users can specify a regular expression that matches the
    identifier instead. This pattern _does_ include the file extension.

    Args:
        files: Paths for which to find the identifying numbers.
        pattern: Optional regular expression pattern that matches the file name
            and has one group that contains the numeric identifier. For example:
            'image_(\d{6})\.tif'

    Returns:
        A list of identifiers for the files, in the same order as the files.

    """
    paths = [pathlib.Path(file) for file in files]
    if len(paths) == 0:
        return []

    if pattern is not None:
        # A regular expression was specified, so use that to extract the
        # identifying numbers.
        compiled = re.compile(pattern)
        if compiled.groups != 1:
            msg = (
                "Pattern should contain exactly one group that matches the identifier."
            )
            raise ValueError(msg)

        def find_identifier(filename: str) -> str:
            match = compiled.match(filename)
            if match is None:
                msg = f'Filename "{filename}" does not match the specified pattern.'
                raise ValueError(msg)
            return match.group(1)

        return [find_identifier(path.name) for path in paths]

    # Use the default approach of finding a common prefix and suffix and
    # assuming that what is left is an identifying number; ignore the file
    # extension.
    filenames = [path.stem for path in paths]
    prefix = find_common_prefix(filenames)
    suffix = find_common_suffix(filenames)
    return [
        filename.removeprefix(prefix).removesuffix(suffix) for filename in filenames
    ]


def find_common_prefix(strings: Sequence[str]) -> str:
    """Find the substring that all strings start with.

    Args:
        strings: Strings for which to extract the common prefix.

    Returns:
        The prefix common to all strings.

    """
    if len(strings) == 0:
        return ""

    # Use the first string as a reference, then loop over prefixes of ever
    # decreasing size to find the largest common prefix.
    reference = strings[0]
    for i_end in range(len(reference), 0, -1):
        prefix = reference[:i_end]
        if all(filename.startswith(prefix) for filename in strings):
            return prefix
    return ""


def find_common_suffix(strings: Sequence[str]) -> str:
    """Find the substring that all strings end with.

    Args:
        strings: Strings for which to extract the common suffix.

    Returns:
        The suffix common to all strings.

    """
    if len(strings) == 0:
        return ""

    # Use the first string as a reference, then loop over postfixes of ever
    # decreasing size to find the largest common prefix.
    reference = strings[0]
    for postfix_size in range(len(reference), 0, -1):
        i_start = len(reference) - postfix_size
        postfix = reference[i_start:]
        if all(filename.endswith(postfix) for filename in strings):
            return postfix
    return ""


def generate_default_identifiers(num_identifiers: int) -> list[str]:
    """Generate a list of identifiers.

    Args:
        num_identifiers: Number of identifiers to generate.

    Returns:
        A list of unique string identifiers. It consists of 0-based numeric
        indices, left-padded with zeros to guarantee sort order. For example,
        for 150 identifiers, the pattern "000", "001", ..., "149" is generated.

    """
    width = len(str(num_identifiers))
    integer_format = f"{{:0{width}d}}"
    return [integer_format.format(i) for i in range(num_identifiers)]
