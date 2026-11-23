# Agent Instructions

## Project

- This is a small Python shopping-cart exercise.
- Source modules are under `src/`: `tuote.py` defines products, `ostos.py` models a product and its quantity, and `ostoskori.py` owns cart operations.
- Tests are under `src/tests/` and use `unittest.TestCase` with pytest discovery.
- Preserve the existing Finnish public names and module layout unless the task explicitly requires an API change.

## Development

- Use Python `>=3.14` and the repository's `uv` environment.
- Run the full test suite from the repository root with `uv run pytest`.
- Add or update focused tests in `src/tests/` alongside behavior changes.
- Keep changes small and avoid modifying unrelated course exercises or generated environment files.