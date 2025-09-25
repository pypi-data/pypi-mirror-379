from typing import (Any, Callable, Generator, Iterable, Optional, Protocol,
                    TypeVar, cast, overload)


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


T = TypeVar("T")
K = TypeVar("K", bound=SupportsLessThan)
S = TypeVar("S", bound=SupportsLessThan)


@overload
def stalin_sort(
    arr: Iterable[S],
    *,
    strict: bool = False,
    decreasing: bool = False,
) -> Generator[S, None, None]: ...


@overload
def stalin_sort(
    arr: Iterable[T],
    *,
    strict: bool = False,
    decreasing: bool = False,
    key: Callable[[T], K]
) -> Generator[T, None, None]: ...


def stalin_sort(
    arr: Iterable[T],
    *,
    strict: bool = False,
    decreasing: bool = False,
    key: Optional[Callable[[T], K]] = None
) -> Generator[T, None, None]:
    """
    Sorts an iterable by removing elements that violate a monotonic sequence.
    Only the elements that fit the chosen ordering survive.

    This algorithm iterates through the input once, keeping only the elements
    that satisfy the given ordering constraint relative to the last kept element.
    Depending on `strict`, `decreasing`, and `key`, it can enforce strictly
    increasing/decreasing or non-decreasing/non-increasing sequences.

    Parameters
    ----------
    arr : Iterable[T]
        The input sequence of elements to process.
    strict : bool, optional
        If True, enforces a *strict* order (e.g., strictly increasing/decreasing).
        If False, allows equal elements to remain (non-strict order).
        Default is False.
    decreasing : bool, optional
        If False, keeps elements in increasing order (according to `key`).
        If True, keeps elements in decreasing order.
        Default is False.
    key : Callable[[T], K], optional
        A function extracting a comparison key from each element.
        Default is the identity function.

    Returns
    -------
    Generator[T, None, None]
        A generator yielding the elements that survive the Stalin Sort.

    Examples
    --------
    >>> list(stalin_sort([7, 7, 4, 2, 7]))
    [7, 7, 7]

    >>> list(stalin_sort([3, 3, 2, 7], strict=True))
    [3, 7]

    >>> list(stalin_sort([4, 2, 7, 3, 0], decreasing=True))
    [4, 2, 0]

    >>> list(stalin_sort(["sort", "this", "out", "immediately"], key=len))
    ['sort', 'this', 'immediately']

    Notes
    -----
    - This is not a traditional sorting algorithm: it does not reorder
      elements, only filters them according to the chosen order constraint.
    - Time complexity is O(n), where n is the length of `arr`.
    - Space complexity is O(1) additional space.
    """
    it = iter(arr)

    try:
        first = next(it)
    except StopIteration:
        return

    keep: Callable[[K, K], bool]
    if not decreasing and strict:
        keep = lambda last, current: last < current
    elif not decreasing and not strict:
        keep = lambda last, current: not (current < last)
    elif decreasing and strict:
        keep = lambda last, current: current < last
    else:
        keep = lambda last, current: not (last < current)

    if key is None:
        def _identity(x: T) -> T:
            return x
        key = cast(Callable[[T], K], _identity)

    last_key = key(first)
    yield first

    for x in it:
        kx = key(x)
        if keep(last_key, kx):
            yield x
            last_key = kx