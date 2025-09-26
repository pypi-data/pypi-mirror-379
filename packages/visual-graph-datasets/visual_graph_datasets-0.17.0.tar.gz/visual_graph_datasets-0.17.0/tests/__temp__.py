from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import py3Dmol

# Create a benzene molecule
benzene_smiles = 'C1=CC=CC=C1'
benzene_molecule = Chem.MolFromSmiles(benzene_smiles)

# Add hydrogens to the molecule
benzene_molecule = Chem.AddHs(benzene_molecule)

# Generate 3D coordinates
AllChem.EmbedMolecule(benzene_molecule, AllChem.ETKDG())

# Use py3Dmol for visualization
view = py3Dmol.view(width=400, height=400)
view.addModel(Chem.MolToMolBlock(benzene_molecule), format='mol')
view.setStyle({'stick': {}})
view.zoomTo()

# Display the 3D visualization
view.export_image('benzene_3d.png')