# Molecular Analogue Generator

An RDKit-based Python project for systematic molecular analogue generation through scaffold modification, fragment replacement, and combinatorial chemical structure generation.

## Overview

Molecular analogue generation is an important approach in medicinal chemistry and drug discovery, allowing researchers to explore structural variations of a parent compound.

This project aims to develop a flexible molecular analogue generation workflow using Python and RDKit.

Starting from a user-defined parent molecule, the program enables selective bond fragmentation, identification of attachment points, replacement of molecular fragments, and generation of structurally related analogues.

The project also incorporates PubChem screening to identify whether generated molecular structures are already registered in the PubChem database.

## Features

- Accepts parent molecules using SMILES notation.
- Molecular structure visualization using RDKit.
- Fragmentation at user-selected bonds.
- Identification of dummy atoms and their neighbouring atoms.
- Tracking of original atom and bond indices during molecular transformations.
- Replacement of molecular fragments using predefined functional groups.
- Combinatorial generation of multiple molecular analogues.
- Canonical SMILES generation and duplicate structure removal.
- Removal of atom-map labels before molecular identity comparison.
- PubChem identity screening using the PUG REST API.

## Project Structure

```text
molecular-analogue-generator/
│
├── notebooks/
│   ├── original_molecular_analogue.ipynb
│   └── analogue_generation.ipynb
│
├── src/
│   └── molecular_analogue_generator/
│       ├── __init__.py
│       ├── fragment_utils.py
│       ├── attachment.py
│       ├── replacement_groups.py
│       ├── analogue_generator.py
│       ├── visualization.py
│       └── pubchem_check.py
│
├── examples/
│   └── pubchem_example.py
│
├── tests/
│   └── test_structure.py
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Technologies Used

- Python 3.10+
- RDKit – Molecular structure manipulation and visualization
- Pandas – Data organization and processing
- NumPy – Numerical operations
- Requests – PubChem API communication
- Jupyter Notebook – Interactive development
- VS Code – Development environment

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/molecular-analogue-generator.git

cd molecular-analogue-generator
```

Replace `YOUR_USERNAME` with your GitHub username.

**2. Create a Conda environment**

```bash
conda create -n analogue_env python=3.10

conda activate analogue_env
```

**3. Install the dependencies**

```bash
python -m pip install -e '.[dev]'
```

**4. Launch Jupyter Notebook**

```bash
jupyter notebook
```

Open:

`notebooks/analogue_generation.ipynb`

Alternatively, open the project in VS Code and select the appropriate Jupyter kernel.

## Methodology

The analogue generation workflow consists of the following stages.

**1. Parent molecule input**

A molecular structure is supplied as a SMILES string and converted into an RDKit molecule object.

**2. Molecular fragmentation**

Selected bonds are fragmented to obtain a core structure containing dummy atoms at the attachment positions.

**3. Atom-index tracking**

Original atom indices are stored as atom properties, allowing attachment positions to be tracked even when atom indices change during molecular transformations.

**4. Fragment replacement**

Selected replacement groups are attached to the corresponding positions in the molecular core.

**5. Combinatorial analogue generation**

Different combinations of replacement groups are used to generate a library of molecular analogues.

**6. Structure standardization and duplicate removal**

Atom-map labels are removed from copies of the generated structures, followed by canonical SMILES generation to identify duplicate representations.

**7. PubChem screening**

Generated SMILES are submitted to PubChem through its PUG REST API to check for existing compound records.

A PubChem no-match result does not necessarily indicate that a compound is novel or previously unreported.

## Example: PubChem Screening

```python
from molecular_analogue_generator.pubchem_check import (
    check_pubchem
)

smiles = "CC(=O)Oc1ccccc1C(=O)O"

result = check_pubchem(smiles)

print(result)
```

The function returns the molecular SMILES, PubChem search status, compound CID (when available), and PubChem URL.

## Testing

Run the included tests using:

```bash
python -m pytest -q
```

## Future Development

- Automated carbon-chain extension and homologous series generation.
- Additional functional-group replacement libraries.
- Expanded scaffold modification strategies.
- Molecular descriptor calculation.
- Integration with ADMET prediction tools.
- Physicochemical property-based filtering.
- Similarity-based analogue ranking.
- Automated export of generated molecular libraries.
- Development of a graphical user interface.

## Applications

This project is intended for computational chemistry research, molecular structure exploration, medicinal chemistry, and preliminary virtual library generation.

## Project Status

**Under active development.**

The current implementation focuses on RDKit-based structural transformations and molecular analogue generation. Additional screening and molecular property prediction capabilities are planned.

## Acknowledgements

- [RDKit](https://www.rdkit.org/) – Open-source cheminformatics toolkit.
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) – Public chemical information database maintained by NCBI.

## Disclaimer

The generated molecular structures are computational predictions and have not necessarily been synthesized or experimentally validated. PubChem screening is intended for preliminary compound identification and should not be considered definitive evidence of chemical novelty.
