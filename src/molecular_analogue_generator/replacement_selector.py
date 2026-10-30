import rdkit
from rdkit import Chem



from molecular_analogue_generator.replacement_groups import replacement_groups


categories = list(replacement_groups.keys())


def select_categories(dummy_number):

    print(f"\nSelect categories for dummy neighbor {dummy_number}")
    print("-------------------------------------------")

    for i, name in enumerate(categories):
        print(f"{i} | {name}")

    choices = input(
        "Enter 3-4 category numbers separated by commas: "
    )

    selected_indices = [
        int(x.strip()) for x in choices.split(",")
    ]

    selected_categories = [
        categories[i] for i in selected_indices
    ]

    print("Selected categories:", selected_categories)

    return selected_categories


def collect_replacements(selected_categories):

    selected_groups = {}

    for category in selected_categories:

        for name, smiles in replacement_groups[category].items():

            selected_groups[name] = smiles

    return selected_groups


def prepare_replacement_groups(selected_groups):

    prepared = []

    for name, smiles in selected_groups.items():

        mol = Chem.MolFromSmiles(smiles)

        prepared.append({
            "name": name,
            "smiles": smiles,
            "mol": mol
        })

    return prepared