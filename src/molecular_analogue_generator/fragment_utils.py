from rdkit import Chem

def set_original_idx(mol):

    for atom in mol.GetAtoms():
        atom.SetIntProp("original_idx", atom.GetIdx())
        atom.SetProp("molAtomMapNumber", str(atom.GetIdx()))

    return mol

def find_current_idx(mol, original_idx):
    for atom in mol.GetAtoms():
        if atom.HasProp("original_idx"): 
            if atom.GetIntProp("original_idx") == original_idx:
                return atom.GetIdx()
    return None

def find_current_bond_idx(mol, original_bond_idx):
    for bond in mol.GetBonds():
        if bond.HasProp("original_bond_idx"):
            if bond.GetIntProp("original_bond_idx") == original_bond_idx:
                return bond.GetIdx()
    return None

def get_core_dummy_info(mol):
    result = []

    for atom in mol.GetAtoms():

        if atom.GetSymbol() == "*":

            neighbor_data = {
                "core_dummy_current_idx": atom.GetIdx(),            
                "core_dummy_neighbor_current_idx": None,
                "core_dummy_neighbor_original_idx": None
            }

            neighbors = atom.GetNeighbors()

            if len(neighbors) > 0:
                neighbor = neighbors[0]

                neighbor_data["core_dummy_neighbor_current_idx"] = neighbor.GetIdx()

                if neighbor.HasProp("original_idx"):
                    neighbor_data["core_dummy_neighbor_original_idx"] = neighbor.GetIntProp("original_idx")

            result.append(neighbor_data)

    return result

def get_replacement_dummy_info(mol):
    """
    Replacement groups are expected to contain exactly one dummy atom.
    """

    result = []

    for atom in mol.GetAtoms():

        if atom.GetSymbol() == "*":
           
            neighbors = atom.GetNeighbors()
            
            neighbor = neighbors[0]
                
            result.append({
                "replacement_dummy_current_idx":
                atom.GetIdx(),
                "replacement_dummy_neighbor_current_idx":
                neighbor.GetIdx()
            })
        
            return result
