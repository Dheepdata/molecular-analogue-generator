"""Combinatorial attachment of selected replacement groups."""
from itertools import product
from rdkit import Chem
from .attachment import attach_replacement


def generate_analogues(core, position_groups):
    """Yield (replacement_names, molecule) for each combination.

    position_groups maps original core-neighbour indices to lists of
    {"name": str, "mol": RDKit Mol} replacement entries.
    Errors are raised to the caller, not silently discarded.
    """
    positions = list(position_groups)
    for combination in product(*(position_groups[p] for p in positions)):
        current = Chem.Mol(core)
        names = []
        for position, item in zip(positions, combination):
            current = attach_replacement(current, item["mol"], position)
            names.append(item["name"])
        yield names, current
