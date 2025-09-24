from pathlib import Path

import pytest

import deeporigin_molstar
from deeporigin_molstar.src.viewers import (
    DockingViewer,
    LigandConfig,
    ProteinConfig,
    ProteinViewer,
)


@pytest.fixture
def path():
    return Path(__file__).parent.parent


@pytest.fixture
def viewer():
    return DockingViewer()


def test_render_merged_structures_with_default_configs(path, viewer):
    protein_data = f"{path}/examples/1eby.pdb"
    protein_format = "pdb"
    ligands_data = [f"{path}/examples/molecule.mol2"]
    ligand_format = "mol2"

    result = viewer.render_merged_structures(
        protein_data, protein_format, ligands_data, ligand_format
    )
    with open(f"{path}/tests/static/render_docking_default.html", "r") as fd:
        fixture = fd.read()

    assert fixture == result


def test_render_merged_structures_with_custom_configs(path, viewer):
    protein_data = f"{path}/examples/1eby.pdb"
    protein_format = "pdb"
    ligands_data = [f"{path}/examples/molecule.mol2"]
    ligand_format = "mol2"
    protein_config = ProteinConfig(style_type="molecular-surface", surface_alpha=0.5)
    ligand_config = LigandConfig(style_type="ball-and-stick", surface_alpha=0.8)

    result = viewer.render_merged_structures(
        protein_data,
        protein_format,
        ligands_data,
        ligand_format,
        protein_config=protein_config,
        ligand_config=ligand_config,
    )
    with open(f"{path}/tests/static/render_docking_custom_config.html", "r") as fd:
        fixture = fd.read()

    assert fixture == result


def test_render_merged_structures_with_pocket(path, viewer):
    protein_data = f"{path}/examples/1eby.pdb"
    protein_format = "pdb"
    ligands_data = [f"{path}/examples/molecule.mol2"]
    ligand_format = "mol2"
    protein_config = ProteinConfig(style_type="molecular-surface", surface_alpha=0)
    ligand_config = LigandConfig(style_type="ball-and-stick", surface_alpha=0.8)

    result = viewer.render_merged_structures(
        protein_data,
        protein_format,
        ligands_data,
        ligand_format,
        protein_config=protein_config,
        ligand_config=ligand_config,
        finalize=False,
    )

    protein_viewer = ProteinViewer(data="", format="pdb", html=result)
    pocket_config = protein_viewer.get_pocket_visualization_config()
    pocket_config.style_type = "molecular-surface"
    pocket_config.surface_alpha = 0.5

    result = protein_viewer.render_protein_with_pockets(
        pocket_paths=[f"{path}/examples/pockets/1EBY_red_pocket.pdb"],
        pocket_config=pocket_config,
    )

    with open(
        f"{path}/tests/static/render_docking_with_pocket_custom_config.html",
        "r",
    ) as fd:
        fixture = fd.read()

    assert fixture == result
