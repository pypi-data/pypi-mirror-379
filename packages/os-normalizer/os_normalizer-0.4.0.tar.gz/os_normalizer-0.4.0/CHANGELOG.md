# Changelog

All notable changes to this project are documented here.
This file adheres to Keep a Changelog and Semantic Versioning.

## [0.3.3] - 2025-09-21

- Added: `tests/case_utils.py` to share parametrization helpers across suites.
- Added: Platform-specific suites for clearer test changes.
- Removed: Legacy `tests/test_os_normalizer.py` harness now that coverage lives beside each platform.

## [0.3.2] - 2025-09-11

- Added: More `pyproject.toml` metadata (description, keywords, classifiers, project URLs).
- Added: `LICENSE` (MIT) and referenced it from project metadata.
- Added: `RELEASING.md` with step-by-step TestPyPI/PyPI instructions.
- Changed: Switched to Hatchling build backend via `[build-system]` in `pyproject.toml`.
- Changed: Exclude dev artifacts from sdist (`tests/`, caches, lockfiles, egg-info).

## [0.3.1] - 2025-09-09

- Added: Table printing of all OS values.

## [0.3.0] - 2025-09-09

- Added: Support merging in new data to combine observations.
- Added: Tests covering merge behavior.

## [0.2.0] - 2025-09-09

- Added: Additional `os_key` data for broader OS coverage.
- Changed: Improve Linux and macOS parsing; update BSD product extraction; better Windows version identification; fix Darwin kernel parsing.
- Changed: Break up network parsing into vendor-specific modules; general code cleanup; repo structure tidy-up.
- Changed: Rename `OSParse` to `OSData`; project renamed to `os_normalizer`.
- Changed: Adopt Ruff and reformat codebase; fix linter errors; improve test harness.
- Fixed: Failing tests (including `tests/test_full.py`).
- Removed: Old `Observation` class; now parse text and data directly.

## [0.1.0] - 2025-09-06

- Initial release.

[Unreleased]: https://github.com/johnscillieri/os-normalizer/compare/v0.3.3...HEAD
[0.3.3]: https://github.com/johnscillieri/os-normalizer/compare/v0.3.2...v0.3.3
[0.3.1]: https://github.com/johnscillieri/os-normalizer/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/johnscillieri/os-normalizer/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/johnscillieri/os-normalizer/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/johnscillieri/os-normalizer/releases/tag/v0.1.0
