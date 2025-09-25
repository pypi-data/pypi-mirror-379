from __future__ import annotations

from stalin_sort import stalin_sort


class OnlyLess:
    def __init__(self, v: int) -> None:
        self.v = v

    def __lt__(self, other: OnlyLess) -> bool:
        return self.v < other.v

    def __repr__(self) -> str:
        return f"OnlyLess({self.v})"


def test_empty_iterable():
    assert list(stalin_sort([])) == []


def test_nondecreasing_default():
    assert list(stalin_sort([3, 1, 2, 2, 5])) == [3, 5]
    assert list(stalin_sort([1, 2, 2, 2, 3])) == [1, 2, 2, 2, 3]


def test_strict_increasing():
    assert list(stalin_sort([1, 2, 2, 3], strict=True)) == [1, 2, 3]


def test_key_function_len():
    words = ["b", "aa", "aa", "ccc", "cc"]
    assert list(stalin_sort(words, key=len)) == ["b", "aa", "aa", "ccc"]


def test_order_stability_on_ties():
    arr = [2, 2, 2, 2]
    assert list(stalin_sort(arr, strict=False)) == [2, 2, 2, 2]


def test_generator_input_supported_default():
    gen = (x for x in [1, 1, 2, 1, 3])
    assert list(stalin_sort(gen)) == [1, 1, 2, 3]


def test_reverse_mode():
    arr = [5, 4, 4, 2, 7]
    assert list(stalin_sort(arr, decreasing=True)) == [5, 4, 4, 2]


def test_custom_comparable_type():
    data = [OnlyLess(1), OnlyLess(1), OnlyLess(0), OnlyLess(2)]
    out = stalin_sort(data)
    assert [o.v for o in out] == [1, 1, 2]


def test_strict_reverse_mode():
    arr = [5, 4, 4, 2, 7]
    assert list(stalin_sort(arr, strict=True, decreasing=True)) == [5, 4, 2]


def test_custom_comparable_type_reverse_mode():
    data = [OnlyLess(1), OnlyLess(1), OnlyLess(0), OnlyLess(2)]
    out = stalin_sort(data, decreasing=True)
    assert [o.v for o in out] == [1, 1, 0]


def test_custom_key_function():
    data = ["apple", "banana", "apricot", "cherry", "date", "mississippi"]
    out = stalin_sort(data, key=len)
    assert list(out) == ["apple", "banana", "apricot", "mississippi"]