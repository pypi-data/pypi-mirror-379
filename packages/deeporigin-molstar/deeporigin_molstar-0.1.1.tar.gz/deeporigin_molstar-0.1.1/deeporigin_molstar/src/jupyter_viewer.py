"""jupyter_viewer.py for deeporigin_molstar"""

from typing import Union

from IPython.display import HTML, display

from deeporigin_molstar.src.viewers import Viewer


class JupyterViewer:
    """Jupyter notebook integration for DeepOrigin Mol* Viewer.

    Provides methods to display molecular visualizations within Jupyter notebooks
    using HTML iframes.
    """

    @classmethod
    def visualize(cls, result: Union[str, Viewer]):
        """Display molecular visualization in Jupyter notebook.

        Args:
            result (Union[str, Viewer]): Either an HTML string or a Viewer object containing the visualization.

        Returns:
            IPython.display.HTML or None: HTML iframe display object if result contains valid HTML, None otherwise.
        """
        html = result
        if isinstance(result, Viewer):
            html = result.html

        if html:
            iframe_code = f"""
                <iframe srcdoc="{html.replace('"', "&quot;")}" 
                        style="width:100%; height:600px; border:0;">
                </iframe>
            """
            return display(HTML(iframe_code))
        else:
            return None
