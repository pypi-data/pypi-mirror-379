"""molecule_viewer.py for deeporigin_molstar"""

from deeporigin_molstar.src.viewers.viewer import Viewer


class LigandConfig:
    """Configuration class for ligand visualization settings."""

    def __init__(
        self,
        data_label="docked_ligand",
        style_type="ball-and-stick",
        surface_alpha=0,
        label_alpha=0,
    ):
        """Initialize ligand configuration.

        Args:
            data_label (str, optional): Label for the ligand data. Defaults to "docked_ligand".
            style_type (str, optional): Style type for ligand representation. Defaults to "ball-and-stick".
            surface_alpha (int, optional): Alpha value for surface rendering. Defaults to 0.
            label_alpha (int, optional): Alpha value for label rendering. Defaults to 0.
        """
        self.data_label = data_label
        self.style_type = style_type
        self.surface_alpha = surface_alpha
        self.label_alpha = label_alpha
        self.validate_attributes()

    def validate_attributes(self):
        """Validate the attributes of the ligand configuration.

        Raises:
            ValueError: If the protein representation type is unknown.
            ValueError: If the ligand representation type is unknown.
            ValueError: If the label alpha is not between 0 and 1.
            ValueError: If the surface alpha is not between 0 and 1.
        """
        allowed_styles = [
            "cartoon",
            "backbone",
            "gaussian-surface",
            "line",
            "label",
            "molecular-surface",
            "ball-and-stick",
            "orientation",
        ]
        if self.style_type not in allowed_styles:
            raise ValueError(f"Unknown protein representation type: {self.style_type}")
        if not (0 <= self.label_alpha <= 1):
            raise ValueError("Label alpha must be between 0 and 1.")
        if not (0 <= self.surface_alpha <= 1):
            raise ValueError("Surface alpha must be between 0 and 1.")


DEFAULT_LIGAND_CONFIG = LigandConfig()


class MoleculeViewer(Viewer):
    """Molecule viewer class for rendering molecular structures using Mol*."""

    def __init__(self, data: str, format: str, html: str = ""):
        """Initialize molecule viewer.

        Args:
            data (str): The molecular data to be loaded into the viewer.
            format (str): The format of the molecular data.
            html (str, optional): Additional HTML content. Defaults to "".

        Raises:
            ValueError: If the molecule format is not supported.
        """
        super().__init__(data, format, html)
        if format not in ["pdb", "pdbqt", "mol2", "sdf", "mol"]:
            raise ValueError("Unsupported molecule format: {}".format(format))

    def get_ligand_visualization_config(self):
        """Get the configuration for ligand visualization.

        Returns:
            LigandConfig: The configuration object for ligand visualization.
        """
        return LigandConfig()

    def render_ligand(self, ligand_config: LigandConfig = None, finalize: bool = True):
        """Render the ligand using the provided data and format.

        Args:
            ligand_config (LigandConfig, optional): The configuration for ligand visualization.
            finalize (bool, optional): Indicates whether to finalize the rendering. Defaults to True.

        Returns:
            str: The HTML representation of the rendered ligand.
        """
        if ligand_config is None:
            ligand_config = self.get_ligand_visualization_config()

        js_code = f"""
            const moleculeData = `{self.data}`;
            const ligandFormat = `{self.format}`;
            await Renderer.renderLigand(moleculeData, ligandFormat);
        """
        self.add_component(js_code)
        if finalize:
            self.add_suffix()

        return self.html
