# Changelog

All notable changes to this project will be documented in this file.
This project follows [Semantic Versioning](https://semver.org).

## [1.0.1] – 2025-09-24

### Packaging

- Renamed the published package on PyPI from `stalin_sort` → `stalin-sort-python`. Installation is now done with:

    ```bash
    pip install stalin-sort-python
    ```

    Import inside Python remains the same:

    ```python
    import stalin_sort
    ```

- Updated `README.md` to reflect the new package name and installation and testing instructions.
- Moved `stalin_sort/*` to `src/stalin_sort/*` to follow best practices.

## [1.0.0] – 2025-09-24

### Added

- **Stalin Sort** in Python as a generator.
- Typed to pass mypy checks.
- Extra sorting options: `strict`, `decreasing`, and `key` function.
- Packaged and published to PyPI — `pip install stalin-sort`. Everyone has to suffer through that process at least once.
- Basic tests to ensure functionality.
- README with proper documentation.
