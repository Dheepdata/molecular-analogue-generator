from rdkit import Chem
from molecular_analogue_generator.pubchem_check import canonical_unmapped_smiles
from molecular_analogue_generator.attachment import attach_replacement


def test_atom_maps_do_not_affect_comparison():
    a = Chem.MolFromSmiles("[CH3:0][CH2:1][OH:2]")
    b = Chem.MolFromSmiles("CCO")
    assert canonical_unmapped_smiles(a) == canonical_unmapped_smiles(b)


def test_single_dummy_attachment():
    core = Chem.MolFromSmiles("[CH3:1][*:2]")
    core.GetAtomWithIdx(0).SetIntProp("original_idx", 0)
    replacement = Chem.MolFromSmiles("[*:1]O")
    product = attach_replacement(core, replacement, 0)
    assert canonical_unmapped_smiles(product) == "CO"
