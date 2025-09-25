from abc import abstractmethod
from typing import Callable
from typing import Iterator
from typing import Protocol
from typing import TypeVar

T = TypeVar("T")
"""A type variable for generic items."""


class Comparable(Protocol):
    """A protocol for comparable objects."""

    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        """Less than comparison."""

    @abstractmethod
    def __gt__(self: T, other: T) -> bool:
        """Greater than comparison."""


Cmp = TypeVar("Cmp", bound=Comparable)
"""A type variable for comparable types."""


def sync(
    iter1: Iterator[T],
    iter2: Iterator[T],
    key1: Callable[[T], Cmp],
    key2: Callable[[T], Cmp],
    cmp_func: Callable[[Cmp, Cmp], int] = lambda x, y: (x > y) - (x < y),
) -> Iterator[tuple[T, T]]:
    """
    Sync two iterators based on a comparison function and key functions.

    Args:
        iter1: The first iterator.
        iter2: The second iterator.
        key1: A function to extract the comparison key from items in iter1.
        key2: A function to extract the comparison key from items in iter2.
        cmp_func: A function to compare two keys, returning negative if the first is less than
            the second, zero if they are equal, and positive if the first is greater than
            the second. Defaults to the default equality operations.

    """
    try:
        item1 = next(iter1)
        item2 = next(iter2)
        while True:
            if (result := cmp_func(key1(item1), key2(item2))) == 0:
                yield (item1, item2)
                item1 = next(iter1)
                item2 = next(iter2)
            elif result < 0:
                item1 = next(iter1)
            else:
                item2 = next(iter2)
    except StopIteration:
        return
