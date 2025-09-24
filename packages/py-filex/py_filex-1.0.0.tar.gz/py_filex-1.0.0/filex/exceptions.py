# =============================================================================
# filex/exceptions.py
# =============================================================================

"""Exceptions personnalisées pour FileX"""


class FileXError(Exception):
    """Exception de base pour FileX"""
    pass


class FileNotFoundError(FileXError):
    """Fichier non trouvé"""
    pass


class DirectoryNotFoundError(FileXError):
    """Dossier non trouvé"""
    pass


class PermissionError(FileXError):
    """Permissions insuffisantes"""
    pass


class InvalidPathError(FileXError):
    """Chemin invalide"""
    pass