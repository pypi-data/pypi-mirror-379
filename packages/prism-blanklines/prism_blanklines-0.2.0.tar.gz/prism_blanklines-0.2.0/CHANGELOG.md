# Changelog

## [0.2.0] - 2025-01-26

- Added configurable indent width detection (default 2 spaces, configurable via `indent_width`)
- Added atomic file operations with temporary files for safer processing
- Added CLI `--dry-run` flag to preview changes without applying them
- Added CLI `--verbose` flag for detailed processing information
- Added specific exception handling for file operations (encoding, permissions, I/O errors)
- Implemented singleton configuration pattern for cleaner code architecture
- Added pre-compiled regex patterns for improved performance
- Added end-of-file newline preservation to maintain existing file formatting
- Renamed `tab_width` to `indent_width` for clarity (breaking change)
- Major code quality improvements and critical issue fixes

## [0.1.3] - 2025-01-09

- Fixed blank lines being incorrectly added after multi-line docstrings in function bodies

## [0.1.2] - 2025-01-09

- Fixed blank lines being removed between consecutive class methods
- Added --version flag to display version from pyproject.toml
- Fixed blank lines after docstrings in function bodies
- Fixed internal blank lines being removed from multi-line docstrings
- Fixed comment block "leave-as-is" behavior for blank line preservation

## [0.1.1] - 2025-01-09

- Initial release