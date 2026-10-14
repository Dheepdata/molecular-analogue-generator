from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Geometry import Point2D
from IPython.display import SVG, display

def draw_with_original_bond_indices(mol, width=500, height=400):

    # Make sure the molecule has 2D coordinates
    if not mol.GetNumConformers():
        Chem.rdDepictor.Compute2DCoords(mol)

    # Create SVG drawer
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)

    # Drawing options
    opts = drawer.drawOptions()

    # Do not show RDKit's current bond indices
    opts.addBondIndices = False

    # Draw the molecule first
    drawer.DrawMolecule(mol)

    # Set font size for our bond numbers
    drawer.SetFontSize(14)

    # Set text colour
    drawer.SetColour((1.0, 0.0, 0.0))

    # Get 2D coordinates
    conf = mol.GetConformer()

    # Add original bond indices
    for bond in mol.GetBonds():

        # Check whether the bond has our original index
        if not bond.HasProp("original_bond_idx"):
            continue

        original_idx = bond.GetIntProp("original_bond_idx")

        # Get the two atoms connected by this bond
        atom1_idx = bond.GetBeginAtomIdx()
        atom2_idx = bond.GetEndAtomIdx()

        pos1 = conf.GetAtomPosition(atom1_idx)
        pos2 = conf.GetAtomPosition(atom2_idx)

        # Calculate midpoint of the bond
        mid_x = (pos1.x + pos2.x) / 2
        mid_y = (pos1.y + pos2.y) / 2

        # Calculate bond direction
        dx = pos2.x - pos1.x
        dy = pos2.y - pos1.y

        # Calculate bond length
        length = (dx**2 + dy**2) ** 0.5

        if length != 0:

            # Perpendicular direction
            perp_x = -dy / length
            perp_y = dx / length

            # Move label slightly away from the bond
            offset = 0.15

            label_x = mid_x + perp_x * offset
            label_y = mid_y + perp_y * offset

        else:
            label_x = mid_x
            label_y = mid_y

        # Position for label
        label_position = Point2D(label_x, label_y)

        # Draw original bond number
        drawer.DrawString(
            str(original_idx),
            label_position
        )

    # Finish drawing
    drawer.FinishDrawing()

    # Get SVG
    svg = drawer.GetDrawingText()

    # Display
    display(SVG(svg))
