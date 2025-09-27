import pathlib

import pytest

from trakcorelib.images import find_file_identifiers
from trakcorelib.images.filenames import (
    find_common_suffix,
    find_common_prefix,
    generate_default_identifiers,
)


def test_find_common_prefix_empty_list() -> None:
    prefix = find_common_prefix([])
    assert prefix == ""


def test_find_common_prefix() -> None:
    files = [
        "hello0001ab",
        "hello0002cd",
        "hello0003ef",
    ]
    prefix = find_common_prefix(files)
    assert prefix == "hello000"


def test_find_common_suffix_empty_list() -> None:
    postfix = find_common_suffix([])
    assert postfix == ""


def test_find_common_suffix() -> None:
    files = [
        "hello0001abworld",
        "hello0002cdworld",
        "hello0003efworld",
    ]
    postfix = find_common_suffix(files)
    assert postfix == "world"


@pytest.fixture
def simple_filenames_and_identifiers() -> tuple[list[str], list[str]]:
    # Note that the files are in non-sorted order.
    return (
        [
            "cam1_20200216_0759010001.jpg",
            "cam1_20200216_0759010002.jpg",
            "cam1_20200216_0759010003.jpg",
            "cam1_20200216_0759010005.jpg",
            "cam1_20200216_0759010004.jpg",
        ],
        ["1", "2", "3", "5", "4"],
    )


def test_find_file_identifiers_empty_list() -> None:
    identifiers = find_file_identifiers([])
    assert identifiers == []


def test_find_file_identifiers_str_name_only(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, reference = simple_filenames_and_identifiers
    identifiers = find_file_identifiers(names)
    assert identifiers == reference


def test_find_file_identifiers_pathlib_name_only(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, reference = simple_filenames_and_identifiers
    paths = (pathlib.Path(name) for name in names)
    identifiers = find_file_identifiers(paths)
    assert identifiers == reference


def test_find_file_identifiers_str_full_path(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, reference = simple_filenames_and_identifiers
    paths = (f"/home/user/project/{name}" for name in names)
    identifiers = find_file_identifiers(paths)
    assert identifiers == reference


def test_find_file_identifiers_pathlib_full_path(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, reference = simple_filenames_and_identifiers
    paths = (pathlib.Path("/home/user/project", name) for name in names)
    identifiers = find_file_identifiers(paths)
    assert identifiers == reference


def test_find_file_identifiers_with_pattern_no_group(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, _ = simple_filenames_and_identifiers
    with pytest.raises(ValueError):
        _ = find_file_identifiers(names, pattern=r".*\d{5}")


def test_find_file_identifiers_with_pattern(
    simple_filenames_and_identifiers: tuple[list[str], list[str]],
) -> None:
    names, reference = simple_filenames_and_identifiers
    # Match an extra "1" at the start of the number so we can check whether
    # the regex pattern is being used.
    identifiers = find_file_identifiers(names, pattern=r".*(\d{5})")
    assert identifiers == [f"1000{identifier}" for identifier in reference]


def test_generate_9_default_identifiers() -> None:
    identifiers = generate_default_identifiers(9)
    for i, identifier in enumerate(identifiers):
        assert identifier == str(i)


def test_generate_99_default_identifiers() -> None:
    identifiers = generate_default_identifiers(99)
    for i, identifier in enumerate(identifiers):
        assert identifier == f"{i:02d}"


def test_generate_999_default_identifiers() -> None:
    identifiers = generate_default_identifiers(999)
    for i, identifier in enumerate(identifiers):
        assert identifier == f"{i:03d}"
