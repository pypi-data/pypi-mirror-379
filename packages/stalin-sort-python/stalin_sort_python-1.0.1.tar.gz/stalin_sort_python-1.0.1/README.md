# Stalin Sort

[![Contributors](https://img.shields.io/github/contributors/hofjak/stalin-sort)](https://github.com/hofjak/stalin-sort)
[![Forks](https://img.shields.io/github/forks/hofjak/stalin-sort)](https://github.com/hofjak/stalin-sort)
[![Stars](https://img.shields.io/github/stars/hofjak/stalin-sort)](https://github.com/hofjak/stalin-sort)
[![Issues](https://img.shields.io/github/issues/hofjak/stalin-sort)](https://github.com/hofjak/stalin-sort)
[![Licence](https://img.shields.io/github/license/hofjak/stalin-sort)](https://github.com/hofjak/stalin-sort)

This project is a Python implementation of Stalin Sort, a meme sorting algorithm. It is probably the most efficient "sorting" algorithm with a time complexity of $\mathcal{O}(n)$.

Here’s what it does:

- You start at the beginning of a list.
- Walk through the elements one by one.
- If the current element is greater than or equal to the last “kept” element, you keep it.
- If the element is smaller, you simply discard it (like it never existed).
- At the end, the result is a non-decreasing subsequence of the input list.

In other words, instead of rearranging elements into sorted order, it just discards the ones that are "out of order."

Credit goes to [this repo](https://github.com/gustavo-depaula/stalin-sort) that collects implementations in various programming languages. My goal here was to create a complete, typed, and installable Python package for Stalin Sort.

## Table of Contents

- [Stalin Sort](#stalin-sort)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
  - [Performance](#performance)
  - [Development](#development)
  - [Run Tests](#run-tests)
  - [License](#license)

## Installation

```bash
pip install stalin-sort-python
```

## Usage

```python
from stalin_sort import stalin_sort

# Basic usage: non-strict, increasing order
print(list(stalin_sort([7, 7, 4, 2, 7])))
# [7, 7, 7]

# Strictly increasing, deduplication of elements
print(list(stalin_sort([3, 3, 2, 7], strict=True)))
# [3, 7]

# Decreasing order
print(list(stalin_sort([4, 2, 7, 3, 0], decreasing=True)))
# [4, 2, 0]

# With a key function
print(list(stalin_sort(["sort", "this", "out", "immediately"], key=len)))
# ['sort', 'this', 'immediately']
```

## Features

- ✅ Typed
- ✅ `strict` and non-strict order
- ✅ `decreasing=True` sequences
- ✅ Custom `key` functions (like `len`)
- ✅ Lazy evaluation
- ✅ Works with any iterable (lists, tuples, sets, strings, generators, ...)
- ✅ Works on any type supporting the `<` operator

## Performance

- **Time Complexity**: $\mathcal{O}(n)$ single pass through the data.
- **Space Complexity**: $\mathcal{O}(1)$ additional space. It only stores the key of the last accepted element.
- **Laziness**: Implemented as a generator, great for streams and large iterables.

## Development

Clone the repo and install in editable moode:

```bash
git clone https://github.com/hofjak/stalin-sort
cd stalin-sort
pip install -e .[dev]
```

## Run Tests

```bash
pytest
# Or
python -m pytest .\tests\
```

## License

[MIT License © Jakob Hofer](LICENSE)

⬆️ [Back to top](#stalin-sort)

---
> GitHub [@hofjak](https://github.com/hofjak)  &nbsp;&middot;&nbsp;
> Email <jakob.refoh@gmail.com>
