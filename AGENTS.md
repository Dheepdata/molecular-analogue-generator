# AGENTS.md

This repository is an RDKit-based molecular analogue generation project. Treat chemistry correctness and deterministic SMILES behavior as the primary constraints when changing code.

## Project layout

- [README.md](README.md): user-facing overview and workflow.
- [src/molecular_analogue_generator](src/molecular_analogue_generator): package source code.
  - [attachment.py](src/molecular_analogue_generator/attachment.py): replacement attachment logic for core/replacement fragments.
  - [fragment_utils.py](src/molecular_analogue_generator/fragment_utils.py): helper logic for dummy atoms and atom tracking.
  - [pubchem_check.py](src/molecular_analogue_generator/pubchem_check.py): canonical SMILES normalization and PubChem identity checks.
- [tests/test_structure.py](tests/test_structure.py): small but important validation suite.
- [notebooks/analogue_generation.ipynb](notebooks/analogue_generation.ipynb): exploratory notebook; keep source-level work in the package unless the task explicitly targets notebook behavior.

## Working conventions

- The package is installed from source via `python -m pip install -e '.[dev]'`.
- Run validation with `python -m pytest -q` after any code change affecting chemistry logic, utilities, or API behavior.
- Keep edits small and testable; the project is centered on pure RDKit transformations and string-based molecule comparisons.
- Prefer reusable helpers over notebook-only logic; most reliable code belongs in the package under [src/molecular_analogue_generator](src/molecular_analogue_generator).

## Chemistry-specific guidance

- Compare molecules by canonical, atom-map-free SMILES using the helpers in [src/molecular_analogue_generator/pubchem_check.py](src/molecular_analogue_generator/pubchem_check.py).
- Preserve original atom/bond index metadata when attachment logic depends on tracked positions; changes in index handling frequently break attachment and fragmentation workflows.
- Dummy atoms are central to the replacement workflow. Validate replacement groups still have exactly one dummy atom and one neighbor before attaching them.
- PubChem requests are external and may fail without internet access. Do not introduce tests that rely on live network calls.

## Typical task patterns

- If adding or changing structural operations, update or add focused tests in [tests/test_structure.py](tests/test_structure.py).
- If a bug is caused by molecule comparison or sanitization, inspect the canonicalization helpers before changing more widely.
- If the task is notebook-only, keep the underlying reusable logic in source files and avoid duplicating chemistry workflows inside the notebook.

## Useful references

- [README.md](README.md)
- [pyproject.toml](pyproject.toml)
- [tests/test_structure.py](tests/test_structure.py)
