"""Utility classes and functions for DeepOrigin Mol* Viewer."""


class NotValidPDBPath(Exception):
    """Exception raised when an invalid PDB file path is provided.

    This exception is raised when attempting to process a PDB file
    that cannot be found or is not in a valid format.
    """

    pass
