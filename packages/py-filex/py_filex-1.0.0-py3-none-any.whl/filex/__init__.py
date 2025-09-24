# =============================================================================
# filex/__init__.py
# =============================================================================

"""
FileX - Gestion intelligente des fichiers et dossiers
====================================================

FileX simplifie la manipulation des fichiers et dossiers en Python avec une API
fluide et intuitive.

Classes principales:
- File: Gestion des fichiers
- Dir: Gestion des dossiers

Exemple d'utilisation:
    >>> from filex import File, Dir
    >>> f = File("data.txt")
    >>> f.write("Hello World!")
    >>> f.exists()
    True
    >>> f.copy("backup/")
"""

from .core import File, Dir
from .exceptions import FileXError, FileNotFoundError, DirectoryNotFoundError

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "File",
    "Dir", 
    "FileXError",
    "FileNotFoundError",
    "DirectoryNotFoundError",
]
