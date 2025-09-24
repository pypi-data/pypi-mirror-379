"""display.py for deeporigin_molstar"""

import argparse
import os

from .utils import NotValidPDBPath

JS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gallery.js")


IFRAME_PREFIX = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mol* visualization</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        iframe {
            border: none;
            width: 50%;
            height: 100px; /* Adjust the height as needed */
        }
    </style>
</head>
<body>
    <h1>Mol* visualization</h1>
    <iframe title="Mol* visualizer"
            width="600"
            height="600"
            srcdoc="
"""


IFRAME_SUFFIX = """">
    </iframe>
</body>
</html>
"""


MOLSTAR_PREFIX = """
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
        <title>Mol* Gallery</title>
    </head>
    <body>
        <script type="text/javascript">
"""

JS_PART = """
        async function init() {
          const viewer = new deepOriginMolstar.Viewer('DeepOriginViewer');
          const Renderer = await deepOriginMolstar.Renderer(viewer);
"""


MOLSTARBODY = """
    var structureFormat = 'pdb'.trim();
    var pocketFormat = 'pdb'.trim();
    var ligandFormat = 'mol2'.trim();
"""

MOLSTARSUFFIX = """
        var ligand_type = `ball-and-stick`.trim();
        await molstarGallery.loadStructureExplicitly(plugin, structureData, structureFormat, 'protein', 'cartoon', 0, 0, false, ligand_type);
      } 

      init();
      </script>
  </body>
</html>
"""

IFRAME_V2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mol* visualization</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        iframe {
            border: none;
            width: 100%;
            height: 500px; /* Adjust the height as needed */
        }
    </style>
</head>
<body>
    <h1>Mol* visualization</h1>
    <iframe src="./temp.html"></iframe>
</body>
</html>
"""


def construct_protein_view(protein_path: str):
    """Construct HTML view for protein visualization.

    Args:
        protein_path (str): Path to the protein PDB file.

    Returns:
        str: Complete HTML string for protein visualization.

    Raises:
        FileNotFoundError: If the protein file does not exist.
    """
    if not os.path.isfile(protein_path):
        raise

    with open(protein_path, "r") as e:
        protein = e.read()

    protein = protein.replace("\n", "\\n")
    protein_data = f"var structureData = `{protein}`.trim();"

    with open(JS_PATH, "r") as file:
        js_data = file.read()

    updated_html = (
        MOLSTAR_PREFIX
        + "\n"
        + js_data
        + "\n"
        + JS_PART
        + "\n"
        + MOLSTARBODY
        + "\n"
        + protein_data
        + "\n"
        + MOLSTARSUFFIX
    )

    return updated_html


def display(protein_path: str, save_path: str, embed_path: str) -> str:
    """Construct and display PDB file using Mol* visualization.

    Args:
        protein_path (str): Path to the PDB file to visualize.
        save_path (str): Path where to save the core Mol* visualization HTML.
        embed_path (str): Relative path for the HTML iframe. Can be the same as `save_path`.
            In Jupyter notebook for showing iframes, you need to specify the
            source file from current directory to make a valid visualization.

    Returns:
        str: HTML string containing the iframe for visualization.

    Raises:
        NotValidPDBPath: If the visualization fails due to invalid PDB path or processing error.
    """
    try:
        html_code = construct_protein_view(protein_path)

        with open(save_path, "w") as file:
            file.write(html_code)

        iframe = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Mol* visualization</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                        }}
                        iframe {{
                            border: none;
                            width: 50%;
                            height: 500px; /* Adjust the height as needed */
                        }}
                    </style>
                </head>
                <body>
                    <h1>Mol* visualization</h1>
                    <iframe src="{embed_path}"></iframe>
                </body>
                </html>
            """
        return iframe
    except Exception as e:
        raise NotValidPDBPath(f"The visualization has failed - {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display protein wirh MolStar")
    parser.add_argument("--protein_path", help="Path to the protein PDB file")

    args = parser.parse_args()
    html_code = construct_protein_view(args.protein_path)
    print(html_code)
