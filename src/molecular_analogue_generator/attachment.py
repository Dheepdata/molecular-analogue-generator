import rdkit
from rdkit import Chem

from .fragment_utils import get_core_dummy_info

def attach_replacement(core, replacement, core_dummy_neighbor_original_idx):

    """
    Attach one replacement group to a selected position in the core.

    core_neighbor_original_idx:
        Original index of the core atom neighbouring the dummy.

    The replacement group must contain exactly one dummy atom,
    and that dummy must have exactly one neighbour.
    """

    # --------------------------------------------------
    # 1. Find the correct dummy in the current core
    # --------------------------------------------------

    core_info = get_core_dummy_info(core)

    matching_dummies = [
        info
        for info in core_info
        if info["core_dummy_neighbor_original_idx"]
        == core_dummy_neighbor_original_idx
    ]

    if len(matching_dummies) != 1:
        raise ValueError(
            f"Expected one dummy at original neighbour index "
            f"{core_dummy_neighbor_original_idx}, "
            f"but found {len(matching_dummies)}."
        )

    selected_dummy = matching_dummies[0]

    core_dummy_idx = selected_dummy["core_dummy_current_idx"]

    core_neighbor_idx = selected_dummy[
        "core_dummy_neighbor_current_idx"
    ]

    # --------------------------------------------------
    # 2. Find the replacement dummy and its neighbour
    # --------------------------------------------------

    replacement_dummies = [
        atom for atom in replacement.GetAtoms()
        if atom.GetAtomicNum() == 0
    ]

    if len(replacement_dummies) != 1:
        raise ValueError(
            "Replacement must contain exactly one dummy atom."
        )

    replacement_dummy = replacement_dummies[0]

    replacement_neighbors = list(
        replacement_dummy.GetNeighbors()
    )

    if len(replacement_neighbors) != 1:
        raise ValueError(
            "Replacement dummy must have exactly one neighbour."
        )

    replacement_dummy_idx = replacement_dummy.GetIdx()

    replacement_neighbor_idx = replacement_neighbors[0].GetIdx()

    # --------------------------------------------------
    # 3. Combine the molecules
    # --------------------------------------------------

    offset = core.GetNumAtoms()

    combined = Chem.CombineMols(core, replacement)

    rw_mol = Chem.RWMol(combined)

    # Replacement indices change after combining
    replacement_dummy_idx += offset
    replacement_neighbor_idx += offset

    # --------------------------------------------------
    # 4. Connect the two attachment atoms
    # --------------------------------------------------

    rw_mol.AddBond(
        core_neighbor_idx,
        replacement_neighbor_idx,
        Chem.BondType.SINGLE
    )

    # --------------------------------------------------
    # 5. Remove both dummy atoms
    # --------------------------------------------------

    dummy_indices = [
        core_dummy_idx,
        replacement_dummy_idx
    ]

    # Remove higher index first to avoid index-shifting errors
    for idx in sorted(dummy_indices, reverse=True):
        rw_mol.RemoveAtom(idx)

    # --------------------------------------------------
    # 6. Convert to a normal RDKit molecule
    # --------------------------------------------------

    new_mol = rw_mol.GetMol()

    Chem.SanitizeMol(new_mol)

    return new_mol
