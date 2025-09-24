"""Test suite for README examples.

Tests all example use cases documented in the README.md file.
"""

import os
from pathlib import Path

import pytest

from deeporigin_molstar.src.viewers.docking_viewer import DockingViewer
from deeporigin_molstar.src.viewers.molecule_viewer import MoleculeViewer
from deeporigin_molstar.src.viewers.protein_viewer import ProteinViewer

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _require(path: Path) -> str:
    """Require a fixture file to exist or skip the test.

    Args:
        path (Path): Path to the required fixture file.

    Returns:
        str: String representation of the path if it exists.

    Raises:
        pytest.skip: If the fixture file does not exist.
    """
    if not path.exists():
        pytest.skip(f"Missing fixture: {path.name}")
    return str(path)


def test_example_protein_viewer_active_site():
    """Test protein viewer active site rendering example from README."""
    pdb_path = _require(FIXTURES_DIR / "protein.pdb")
    viewer = ProteinViewer(data=pdb_path, format="pdb")
    html = viewer.render_active_site()
    assert "Renderer.renderProteinActiveSite" in html
    assert html.strip().endswith("</html>")


def test_example_viewing_trajectories(tmp_path):
    """Test trajectory viewing example from README."""
    pdb_path = _require(FIXTURES_DIR / "protein.pdb")
    xtc_path = _require(FIXTURES_DIR / "trajectory.xtc")
    viewer = ProteinViewer(data=pdb_path, format="pdb")
    html = viewer.render_trajectory(xtc_path)
    assert "renderStructureWithTrajectory" in html
    assert "trajectory" in html


def test_example_docking_viewer_basic_merge():
    """Test docking viewer basic merge example from README."""
    protein_path = _require(FIXTURES_DIR / "protein.pdb")
    ligand_path = _require(FIXTURES_DIR / "ligand.sdf")
    docking = DockingViewer()
    html = docking.render_merged_structures(
        protein_data=protein_path,
        protein_format="pdb",
        ligands_data=[ligand_path],
        ligand_format="sdf",
    )
    assert "renderWithNativeCrystalControl" in html
    assert html.strip().endswith("</html>")


def test_example_molecule_viewer_render_ligand():
    """Test molecule viewer render ligand example from README."""
    ligand_path = _require(FIXTURES_DIR / "ligand.sdf")
    viewer = MoleculeViewer(data=ligand_path, format="sdf")
    html = viewer.render_ligand()
    assert "Renderer.renderLigand" in html
    assert html.strip().endswith("</html>")


def test_example_protein_mutagens_result():
    """Test protein mutagens result example from README."""
    pdb_path = _require(FIXTURES_DIR / "protein.pdb")
    viewer = ProteinViewer(data=pdb_path, format="pdb")
    html = viewer.render_protein_mutagens_result([10, 20, 30], [15, 25, 35])
    assert "Renderer.renderProteinMutagenResult" in html
    assert "residueMutations" in html


def test_example_protein_with_pockets():
    """Test protein with pockets example from README."""
    pdb_path = _require(FIXTURES_DIR / "protein.pdb")
    pocket1 = _require(FIXTURES_DIR / "pocket1.pdb")
    pocket2 = _require(FIXTURES_DIR / "pocket2.pdb")
    viewer = ProteinViewer(data=pdb_path, format="pdb")
    html = viewer.render_protein_with_pockets(pocket_paths=[pocket1, pocket2])
    assert "renderStructureAndPockets" in html
    assert "pocketDataList" in html


def test_example_proteins_overlaying():
    """Test proteins overlaying example from README."""
    pdb1 = _require(FIXTURES_DIR / "protein.pdb")
    pdb2 = _require(FIXTURES_DIR / "protein2.pdb")
    html = ProteinViewer.render_structures_overlaying(
        first_raw_data=pdb1,
        second_raw_data=pdb2,
        first_format="pdb",
        second_format="pdb",
    )
    assert "renderStructuresOverlayingResult" in html
    assert html.strip().endswith("</html>")
