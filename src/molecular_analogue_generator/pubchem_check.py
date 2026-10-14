"""Conservative PubChem identity lookup; requires internet access."""
import requests
from rdkit import Chem


def remove_atom_map_labels(mol):
    clean = Chem.Mol(mol)
    for atom in clean.GetAtoms():
        atom.SetAtomMapNum(0)
    return clean


def canonical_unmapped_smiles(mol):
    return Chem.MolToSmiles(remove_atom_map_labels(mol), canonical=True, isomericSmiles=True)


def check_pubchem(smiles, session=None):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"SMILES": smiles, "Status": "Invalid SMILES", "CID": None, "PubChem_URL": None}
    clean_smiles = canonical_unmapped_smiles(mol)
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/smiles/cids/JSON"
    try:
        client = session if session is not None else requests
        response = client.post(url, data={"smiles": clean_smiles},
                               params={"identity_type": "same_stereo_isotope"}, timeout=30)
        if response.status_code == 404:
            return {"SMILES": clean_smiles, "Status": "Not found in PubChem", "CID": None, "PubChem_URL": None}
        response.raise_for_status()
        cids = response.json().get("IdentifierList", {}).get("CID", [])
        if cids:
            return {"SMILES": clean_smiles, "Status": "Found", "CID": cids,
                    "PubChem_URL": [f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}" for cid in cids]}
        return {"SMILES": clean_smiles, "Status": "Not found in PubChem", "CID": None, "PubChem_URL": None}
    except (requests.RequestException, ValueError) as exc:
        return {"SMILES": clean_smiles, "Status": "API Error", "CID": None,
                "PubChem_URL": None, "Error": str(exc)}


if __name__ == "__main__":
    print(check_pubchem("CC(=O)Oc1ccccc1C(=O)O"))
