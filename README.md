# Molecular Analogue Generator

An RDKit-based project for molecular fragmentation, original-index tracking, dummy-atom replacement, combinatorial analogue generation, structure visualization, and optional PubChem identity screening.

## Starting point

- `notebooks/original_molecular_analogue.ipynb` is the **unaltered uploaded notebook** for reference.
- `notebooks/analogue_generation.ipynb` is a minimally corrected notebook: its final deduplication and screening cells were repaired. The interactive notebook still uses its original function definitions; the modules in `src/` are the next step toward full migration.
- `src/molecular_analogue_generator/` contains extracted/reusable utilities.

## Setup (VS Code terminal)

```bash
conda activate chem_env
python -m pip install -e '.[dev]'
```

Select the `chem_env` Jupyter kernel in VS Code and open `notebooks/analogue_generation.ipynb`. Run cells in order; the notebook asks for a parent SMILES and interactive selections. PubChem requests need internet access.

## Import reusable functions

```python
from molecular_analogue_generator.attachment import attach_replacement
from molecular_analogue_generator.pubchem_check import check_pubchem, canonical_unmapped_smiles
```

## Run tests

```bash
python -m pytest -q
```

## Publish from VS Code

Open this folder, choose **Source Control → Initialize Repository**, stage files, commit, then choose **Publish Branch → Publish to GitHub**. Inspect the notebook before publishing: do not commit proprietary structures, private data, or API credentials.

## Notes

PubChem no-match does not establish chemical novelty. Avoid rapid or repeated requests; deduplicate first and implement caching/backoff for large libraries. The original notebook has been preserved to avoid silently changing your experimental workflow.
