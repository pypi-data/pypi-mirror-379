from dataclasses import dataclass
from typing import Iterator

import pytest

from syncup import sync


@pytest.mark.parametrize(
    "iter1,iter2",
    [
        [iter([]), iter([])],
        [iter([1, 2, 3]), iter([])],
        [iter([]), iter([1, 2, 3])],
    ],
)
def test_sync_empty_iterators(iter1: Iterator[int], iter2: Iterator[int]) -> None:
    """Test sync on empty iterators."""
    result = sync(iter1, iter2, key1=lambda x: x, key2=lambda x: x)
    assert list(result) == []


@pytest.mark.parametrize(
    "iter1,iter2,expected",
    [
        [iter([1, 2, 3]), iter([1, 3]), [(1, 1), (3, 3)]],
        [iter([1, 3]), iter([1, 2, 3]), [(1, 1), (3, 3)]],
    ],
)
def test_sync_iterators_comparable(
    iter1: Iterator[int], iter2: Iterator[int], expected: list[tuple[int, int]]
) -> None:
    """Test sync on iterators with comparable elements."""
    result = sync(iter1, iter2, key1=lambda x: x, key2=lambda x: x)
    assert list(result) == expected


@dataclass(eq=True, frozen=True)
class Wrapper:
    """A custom class implementing the Comparable protocol for testing."""

    value: int


def test_sync_on_custom_comparable() -> None:
    """Test sync on iterators with custom comparable elements."""
    iter1 = iter([Wrapper(3), Wrapper(2), Wrapper(1)])
    iter2 = iter([Wrapper(3), Wrapper(1)])
    expected = [(Wrapper(3), Wrapper(3)), (Wrapper(1), Wrapper(1))]

    result = sync(
        iter1=iter1,
        iter2=iter2,
        # Use the 'value' attribute for comparison
        key1=lambda x: x.value,
        key2=lambda x: x.value,
        # Reverse the order of the comparison to test reverse sorted inputs
        cmp_func=lambda x, y: (x < y) - (x > y),
    )

    assert list(result) == expected
