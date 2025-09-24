
# BioSim Mol* Viewer

BioSim Mol* Viewer is a powerful tool for visualizing molecular structures using Mol* in a web environment. This package allows users to load, manipulate, and visualize molecular structures with ease.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Viewer](#basic-viewer)
  - [Protein Viewer](#protein-viewer)
  - [Molecule Merger Viewer](#molecule-merger-viewer)
- [API Reference](#api-reference)
- [Examples](#examples)

## Installation

To install the package, clone the repository and install the necessary dependencies:

```sh
git clone git@github.com:Biosim-AI/biosim_molstar.git
cd deeporigin_molstar
pip install -r requirements.txt
```

or 

```sh
pip install -e git+ssh://git@github.com/Biosim-AI/deeporigin_molstar.git@tag_of_version
```

## Usage

### Basic Viewer

The `Viewer` class is the base template class for rendering molecular structures.
it contains all the necessary methods for reading, writing and constructing molstar visualizations.

### Protein Viewer

The `ProteinViewer` class extends the `Viewer` class and provides additional methods specific to visualizations of protein structures.

```python
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer
from deeporigin_molstar import JupyterViewer

# Example usage of the ProteinViewer
protein_viewer = ProteinViewer(data='path/to/protein.pdb', format='pdb')
html_content = protein_viewer.render_protein()
JupyterViewer.visualize(html_content)
```

### Viewing trajectories

Trajectories can be viewed using:

```python
from deeporigin_molstar.src.viewers import ProteinViewer
from deeporigin_molstar import JupyterViewer

xtc_file = "path.to.xtc"
pdb_file = "path/to/pdb.pdb"
        
protein_viewer = ProteinViewer(data=pdb_file, format="pdb")
html_content = protein_viewer.render_trajectory(xtc_file)
    
JupyterViewer.visualize(html_content)
```

### Docking Viewer

The `DockingViewer` class is used to merge and visualize multiple molecular structures.

```python
from deeporigin_molstar.src.viewers.docking_viewer import DockingViewer

# Example usage of the MoleculeMergerViewer
merger_viewer = DockingViewer()
html_content = merger_viewer.render_merged_structures(
    protein_data='path/to/protein.pdb',
    protein_format='pdb',
    ligand_data='path/to/ligand.mol2',
    ligand_format='mol2'
)
print(html_content)
```


### Molecule Viewer

The `MoleculeViewer` class is used to visualize molecule conformations.

```python
from deeporigin_molstar.src.viewers.molecule_viewer import MoleculeViewer

# Example usage of the MoleculeMergerViewer
molecule_viewer = MoleculeViewer(data='path/to/protein.[mol2, sdf, pdb]', format='[mol2, sdf, pdb]')
html_content = molecule_viewer.render_ligand()
print(html_content)
```
## API Reference

### Viewer

- `Viewer(data: str, format: str, html: str = '')`
  - Base class for rendering molecular structures.
  - **Parameters**:
    - `data`: Path to the molecular data file.
    - `format`: Format of the molecular data (e.g., 'pdb', 'pdbqt').
    - `html`: Initial HTML content.

- `render() -> str`
  - Renders the molecular structure and returns the HTML content.

### ProteinViewer

- `ProteinViewer(data: str, format: str, html: str = '')`
  - Extends `Viewer` with additional methods for protein visualization.

### DockingViewer

- `DockingViewer(html: str = '')`
  - Used to merge and visualize multiple molecular structures.

- `render_merged_structures(protein_data: str, protein_format: str, ligand_data: str, ligand_format: str) -> str`
  - Renders merged molecular structures.
  - **Parameters**:
    - `protein_data`: Path to the protein data file.
    - `protein_format`: Format of the protein data.
    - `ligand_data`: Path to the ligand data file.
    - `ligand_format`: Format of the ligand data.

### MoleculeViewer

- `DockingViewer(data: str, format: str, html: str = '')`
  - Extends `Viewer` with additional methods for molecule visualization.

## Examples

Here are some example scripts demonstrating how to use the package. For more examples, please refer to the `examples` directory.

### Example 1: Protein Viewer

```python
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer

protein_viewer = ProteinViewer(data='path/to/protein.pdb', format='pdb')
html_content = protein_viewer.render_active_site()
print(html_content)
```

### Example 2: Render Protein Mutagens Analysis Result

```python
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer

protein_viewer = ProteinViewer(data='path/to/protein.pdb', format='pdb')
residue_gaps = [10, 20, 30]  # example gaps
residue_mutations = [15, 25, 35]  # example mutations
html_content = protein_viewer.render_protein_mutagens_result(residue_gaps, residue_mutations)
print(html_content)
```


### Example 3: Render Protein with pockets

```python
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer

protein_viewer = ProteinViewer(data='path/to/protein.pdb', format='pdb')

pocket_paths = ['path/to/pocket1.pdb', 'path/to/pocket2.pdb']

pocket_config = protein_viewer.get_pocket_visualization_config()
pocket_config.surface_colors = ['red', 'blue']

html_content = protein_viewer.render_protein_with_pockets(pocket_paths=pocket_paths)
print(html_content)
```


### Example 4: Render Proteins overlaying result

```python
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer

html = ProteinViewer.render_structures_overlaying(
    first_raw_data='path/to/pocket1.pdb',
    second_raw_data='path/to/pocket2.pdb', 
    first_format="pdb", 
    second_format="pdb", 
)
print(html)
```

### Example 5: Molecule viewer

```python
from deeporigin_molstar.src.viewers.molecule_viewer import MoleculeViewer

molecule_viewer = MoleculeViewer(data='path/to/ligand.mol2', format='mol2')
html_content = molecule_viewer.render_ligand()
print(html_content)
```


### Example 6: Docking viewer

```python
from deeporigin_molstar.src.viewers.docking_viewer import DockingViewer

docking_viewer = DockingViewer()
html_content = docking_viewer.render_merged_structures(
    protein_data='path/to/protein.pdb',
    protein_format='pdb',
    ligand_data='path/to/ligand.mol2',
    ligand_format='mol2',
)
print(html_content)
```

## Contributing

We welcome contributions! Please open an issue or submit a pull request on GitHub.




```mermaid
graph TD
    A[Start] --> B[Download Protein 1EBY]
    B --> C[Prepare Protein Structure]
    C --> D[Find Pockets]
    D --> E[Visualize Pockets]
end
```
