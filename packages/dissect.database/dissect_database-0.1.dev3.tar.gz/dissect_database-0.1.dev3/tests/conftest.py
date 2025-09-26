from __future__ import annotations

import gzip
from pathlib import Path
from typing import TYPE_CHECKING, BinaryIO

import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator


def absolute_path(filename: str) -> Path:
    return Path(__file__).parent / filename


def open_file(name: str, mode: str = "rb") -> Iterator[BinaryIO]:
    with absolute_path(name).open(mode) as fh:
        yield fh


def open_file_gz(name: str, mode: str = "rb") -> Iterator[BinaryIO]:
    with gzip.GzipFile(absolute_path(name), mode) as fh:
        yield fh


@pytest.fixture
def btree_db() -> Iterator[BinaryIO]:
    yield from open_file_gz("_data/bsd/btree.db.gz")


@pytest.fixture
def hash_db() -> Iterator[BinaryIO]:
    yield from open_file_gz("_data/bsd/hash.db.gz")


@pytest.fixture
def recno_db() -> Iterator[BinaryIO]:
    yield from open_file_gz("_data/bsd/recno.db.gz")


@pytest.fixture
def rpm_packages() -> Iterator[BinaryIO]:
    yield from open_file_gz("_data/bsd/rpm/Packages.gz")
