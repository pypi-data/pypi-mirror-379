# =============================================================================
# filex/core.py
# =============================================================================

"""
Module principal de FileX contenant les classes File et Dir
"""

import shutil
import os
import zipfile
import datetime
from pathlib import Path
from typing import List, Optional, Union, Pattern
import fnmatch
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib

from .exceptions import (
    FileXError, 
    FileNotFoundError as FileXFileNotFoundError,
    DirectoryNotFoundError,
    PermissionError as FileXPermissionError,
    InvalidPathError
)


class File:
    """
    Classe pour la gestion intelligente des fichiers.
    
    Exemple:
        >>> f = File("data.txt")
        >>> f.write("Hello World!")
        >>> print(f.read())
        Hello World!
        >>> f.copy("backup/")
    """
    
    def __init__(self, path: Union[str, Path]):
        """
        Initialise un objet File.
        
        Args:
            path: Chemin vers le fichier
        """
        self.path = Path(path).resolve()
        self._validate_path()
    
    def _validate_path(self):
        """Valide le chemin du fichier"""
        if not self.path.name:
            raise InvalidPathError(f"Chemin invalide: {self.path}")
    
    def exists(self) -> bool:
        """Vérifie si le fichier existe."""
        return self.path.exists() and self.path.is_file()
    
    def read(self, encoding: str = "utf-8") -> str:
        """
        Lit le contenu du fichier.
        
        Args:
            encoding: Encodage du fichier (défaut: utf-8)
            
        Returns:
            Contenu du fichier
            
        Raises:
            FileNotFoundError: Si le fichier n'existe pas
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        try:
            return self.path.read_text(encoding=encoding)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def read_bytes(self) -> bytes:
        """
        Lit le contenu binaire du fichier.
        
        Returns:
            Contenu binaire du fichier
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        try:
            return self.path.read_bytes()
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def read_lines(self, encoding: str = "utf-8") -> List[str]:
        """
        Lit le fichier ligne par ligne.
        
        Args:
            encoding: Encodage du fichier
            
        Returns:
            Liste des lignes
        """
        content = self.read(encoding)
        return content.splitlines()
    
    def write(self, content: str, encoding: str = "utf-8", create_dirs: bool = True) -> 'File':
        """
        Écrit du contenu dans le fichier.
        
        Args:
            content: Contenu à écrire
            encoding: Encodage du fichier
            create_dirs: Créer les dossiers parents si nécessaire
            
        Returns:
            Self pour chaînage
        """
        if create_dirs:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            self.path.write_text(content, encoding=encoding)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
        
        return self
    
    def write_bytes(self, content: bytes, create_dirs: bool = True) -> 'File':
        """
        Écrit du contenu binaire dans le fichier.
        
        Args:
            content: Contenu binaire à écrire
            create_dirs: Créer les dossiers parents si nécessaire
            
        Returns:
            Self pour chaînage
        """
        if create_dirs:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            self.path.write_bytes(content)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
        
        return self
    
    def append(self, content: str, encoding: str = "utf-8") -> 'File':
        """
        Ajoute du contenu à la fin du fichier.
        
        Args:
            content: Contenu à ajouter
            encoding: Encodage du fichier
            
        Returns:
            Self pour chaînage
        """
        try:
            with open(self.path, 'a', encoding=encoding) as f:
                f.write(content)
        except FileNotFoundError as e:
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}") from e
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
        
        return self
    
    def copy(self, dest: Union[str, Path], overwrite: bool = False) -> 'File':
        """
        Copie le fichier vers une destination.
        
        Args:
            dest: Destination (fichier ou dossier)
            overwrite: Écraser si existe déjà
            
        Returns:
            Nouvel objet File pour le fichier copié
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier source non trouvé: {self.path}")
        
        dest_path = Path(dest)
        
        # Si la destination est un dossier, garder le nom du fichier
        if dest_path.is_dir():
            dest_path = dest_path / self.path.name
        
        # Créer les dossiers parents si nécessaire
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Vérifier l'écrasement
        if dest_path.exists() and not overwrite:
            raise FileXError(f"Le fichier destination existe déjà: {dest_path}")
        
        try:
            shutil.copy2(str(self.path), str(dest_path))
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la copie") from e
        
        return File(dest_path)
    
    def move(self, dest: Union[str, Path], overwrite: bool = False) -> 'File':
        """
        Déplace le fichier vers une destination.
        
        Args:
            dest: Destination
            overwrite: Écraser si existe déjà
            
        Returns:
            Self avec le nouveau chemin
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier source non trouvé: {self.path}")
        
        dest_path = Path(dest)
        
        if dest_path.is_dir():
            dest_path = dest_path / self.path.name
        
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        if dest_path.exists() and not overwrite:
            raise FileXError(f"Le fichier destination existe déjà: {dest_path}")
        
        try:
            shutil.move(str(self.path), str(dest_path))
            self.path = dest_path.resolve()
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors du déplacement") from e
        
        return self
    
    def rename(self, new_name: str) -> 'File':
        """
        Renomme le fichier.
        
        Args:
            new_name: Nouveau nom
            
        Returns:
            Self avec le nouveau nom
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        new_path = self.path.parent / new_name
        
        if new_path.exists():
            raise FileXError(f"Un fichier avec ce nom existe déjà: {new_name}")
        
        try:
            self.path.rename(new_path)
            self.path = new_path
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors du renommage") from e
        
        return self
    
    def delete(self) -> bool:
        """
        Supprime le fichier.
        
        Returns:
            True si supprimé avec succès
        """
        if not self.exists():
            return False
        
        try:
            self.path.unlink()
            return True
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la suppression") from e
    
    def size(self) -> int:
        """
        Retourne la taille du fichier en octets.
        
        Returns:
            Taille en octets
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        return self.path.stat().st_size
    
    def size_human(self) -> str:
        """
        Retourne la taille du fichier en format lisible.
        
        Returns:
            Taille formatée (ex: "1.5 MB")
        """
        size = self.size()
        
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        
        return f"{size:.1f} PB"
    
    def extension(self) -> str:
        """
        Retourne l'extension du fichier.
        
        Returns:
            Extension (sans le point)
        """
        return self.path.suffix.lstrip('.')
    
    def name(self) -> str:
        """Retourne le nom du fichier sans l'extension."""
        return self.path.stem
    
    def full_name(self) -> str:
        """Retourne le nom complet du fichier."""
        return self.path.name
    
    def created_at(self) -> datetime.datetime:
        """
        Retourne la date de création du fichier.
        
        Returns:
            Date de création
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        timestamp = self.path.stat().st_ctime
        return datetime.datetime.fromtimestamp(timestamp)
    
    def modified_at(self) -> datetime.datetime:
        """
        Retourne la date de modification du fichier.
        
        Returns:
            Date de modification
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        timestamp = self.path.stat().st_mtime
        return datetime.datetime.fromtimestamp(timestamp)
    
    def hash_md5(self) -> str:
        """
        Calcule le hash MD5 du fichier.
        
        Returns:
            Hash MD5 en hexadécimal
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        hash_md5 = hashlib.md5()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        
        return hash_md5.hexdigest()
    
    def hash_sha256(self) -> str:
        """
        Calcule le hash SHA256 du fichier.
        
        Returns:
            Hash SHA256 en hexadécimal
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        hash_sha256 = hashlib.sha256()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        
        return hash_sha256.hexdigest()
    
    def zip(self, archive_name: Union[str, Path], compression_level: int = 6) -> 'File':
        """
        Ajoute le fichier à une archive ZIP.
        
        Args:
            archive_name: Nom de l'archive
            compression_level: Niveau de compression (0-9)
            
        Returns:
            Objet File pour l'archive créée
        """
        if not self.exists():
            raise FileXFileNotFoundError(f"Fichier non trouvé: {self.path}")
        
        archive_path = Path(archive_name)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with zipfile.ZipFile(archive_path, 'a', 
                               compression=zipfile.ZIP_DEFLATED,
                               compresslevel=compression_level) as zf:
                zf.write(self.path, arcname=self.path.name)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la compression") from e
        
        return File(archive_path)
    
    def __str__(self) -> str:
        return str(self.path)
    
    def __repr__(self) -> str:
        return f"File('{self.path}')"


class Dir:
    """
    Classe pour la gestion intelligente des dossiers.
    
    Exemple:
        >>> d = Dir("my_folder")
        >>> d.create()
        >>> files = d.list_files()
        >>> d.zip("backup.zip")
    """
    
    def __init__(self, path: Union[str, Path]):
        """
        Initialise un objet Dir.
        
        Args:
            path: Chemin vers le dossier
        """
        self.path = Path(path).resolve()
    
    def exists(self) -> bool:
        """Vérifie si le dossier existe."""
        return self.path.exists() and self.path.is_dir()
    
    def create(self, parents: bool = True) -> 'Dir':
        """
        Crée le dossier.
        
        Args:
            parents: Créer les dossiers parents si nécessaire
            
        Returns:
            Self pour chaînage
        """
        try:
            self.path.mkdir(parents=parents, exist_ok=True)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
        
        return self
    
    def list(self, pattern: Optional[str] = None) -> List[str]:
        """
        Liste le contenu du dossier.
        
        Args:
            pattern: Pattern de filtrage (ex: "*.txt")
            
        Returns:
            Liste des noms de fichiers/dossiers
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            items = [p.name for p in self.path.iterdir()]
            
            if pattern:
                items = [item for item in items if fnmatch.fnmatch(item, pattern)]
            
            return sorted(items)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def list_files(self, pattern: Optional[str] = None, recursive: bool = False) -> List[str]:
        """
        Liste uniquement les fichiers.
        
        Args:
            pattern: Pattern de filtrage
            recursive: Recherche récursive
            
        Returns:
            Liste des noms de fichiers
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            if recursive:
                files = [str(p.relative_to(self.path)) for p in self.path.rglob('*') if p.is_file()]
            else:
                files = [p.name for p in self.path.iterdir() if p.is_file()]
            
            if pattern:
                files = [f for f in files if fnmatch.fnmatch(f, pattern)]
            
            return sorted(files)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def list_dirs(self, recursive: bool = False) -> List[str]:
        """
        Liste uniquement les dossiers.
        
        Args:
            recursive: Recherche récursive
            
        Returns:
            Liste des noms de dossiers
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            if recursive:
                dirs = [str(p.relative_to(self.path)) for p in self.path.rglob('*') if p.is_dir()]
            else:
                dirs = [p.name for p in self.path.iterdir() if p.is_dir()]
            
            return sorted(dirs)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def size(self, human_readable: bool = False) -> Union[int, str]:
        """
        Calcule la taille totale du dossier.
        
        Args:
            human_readable: Retourner en format lisible
            
        Returns:
            Taille en octets ou formatée
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            total_size = sum(f.stat().st_size for f in self.path.rglob('*') if f.is_file())
            
            if human_readable:
                for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                    if total_size < 1024.0:
                        return f"{total_size:.1f} {unit}"
                    total_size /= 1024.0
                return f"{total_size:.1f} PB"
            
            return total_size
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def count_files(self, recursive: bool = True) -> int:
        """
        Compte le nombre de fichiers.
        
        Args:
            recursive: Recherche récursive
            
        Returns:
            Nombre de fichiers
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            if recursive:
                return sum(1 for p in self.path.rglob('*') if p.is_file())
            else:
                return sum(1 for p in self.path.iterdir() if p.is_file())
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def count_dirs(self, recursive: bool = True) -> int:
        """
        Compte le nombre de dossiers.
        
        Args:
            recursive: Recherche récursive
            
        Returns:
            Nombre de dossiers
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            if recursive:
                return sum(1 for p in self.path.rglob('*') if p.is_dir())
            else:
                return sum(1 for p in self.path.iterdir() if p.is_dir())
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def copy(self, dest: Union[str, Path], exclude: Optional[List[str]] = None, 
             overwrite: bool = False, parallel: bool = False) -> 'Dir':
        """
        Copie le dossier vers une destination.
        
        Args:
            dest: Destination
            exclude: Patterns à exclure
            overwrite: Écraser si existe
            parallel: Copie en parallèle
            
        Returns:
            Nouvel objet Dir
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier source non trouvé: {self.path}")
        
        dest_path = Path(dest)
        exclude = exclude or []
        
        def should_exclude(file_path: Path) -> bool:
            for pattern in exclude:
                if fnmatch.fnmatch(str(file_path.relative_to(self.path)), pattern):
                    return True
            return False
        
        def copy_file(src_file: Path, dst_file: Path):
            if should_exclude(src_file):
                return
            
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            
            if dst_file.exists() and not overwrite:
                return
            
            shutil.copy2(str(src_file), str(dst_file))
        
        try:
            if parallel:
                with ThreadPoolExecutor() as executor:
                    futures = []
                    for src_file in self.path.rglob('*'):
                        if src_file.is_file():
                            rel_path = src_file.relative_to(self.path)
                            dst_file = dest_path / rel_path
                            futures.append(executor.submit(copy_file, src_file, dst_file))
                    
                    # Attendre que tous les threads se terminent
                    for future in futures:
                        future.result()
            else:
                for src_file in self.path.rglob('*'):
                    if src_file.is_file():
                        rel_path = src_file.relative_to(self.path)
                        dst_file = dest_path / rel_path
                        copy_file(src_file, dst_file)
        
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la copie") from e
        
        return Dir(dest_path)
    
    def move(self, dest: Union[str, Path], overwrite: bool = False) -> 'Dir':
        """
        Déplace le dossier vers une destination.
        
        Args:
            dest: Destination
            overwrite: Écraser si existe
            
        Returns:
            Self avec le nouveau chemin
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier source non trouvé: {self.path}")
        
        dest_path = Path(dest)
        
        if dest_path.exists() and not overwrite:
            raise FileXError(f"Le dossier destination existe déjà: {dest_path}")
        
        try:
            shutil.move(str(self.path), str(dest_path))
            self.path = dest_path.resolve()
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors du déplacement") from e
        
        return self
    
    def rename(self, new_name: str) -> 'Dir':
        """
        Renomme le dossier.
        
        Args:
            new_name: Nouveau nom
            
        Returns:
            Self avec le nouveau nom
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        new_path = self.path.parent / new_name
        
        if new_path.exists():
            raise FileXError(f"Un dossier avec ce nom existe déjà: {new_name}")
        
        try:
            self.path.rename(new_path)
            self.path = new_path
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors du renommage") from e
        
        return self
    
    def delete(self, force: bool = False) -> bool:
        """
        Supprime le dossier.
        
        Args:
            force: Suppression forcée (même si non vide)
            
        Returns:
            True si supprimé avec succès
        """
        if not self.exists():
            return False
        
        try:
            if force:
                shutil.rmtree(self.path)
            else:
                self.path.rmdir()  # Ne fonctionne que si vide
            return True
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la suppression") from e
        except OSError as e:
            raise FileXError(f"Impossible de supprimer le dossier (non vide?): {self.path}") from e
    
    def zip(self, archive_name: Union[str, Path], exclude: Optional[List[str]] = None,
            compression_level: int = 6) -> File:
        """
        Compresse le dossier en ZIP.
        
        Args:
            archive_name: Nom de l'archive
            exclude: Patterns à exclure
            compression_level: Niveau de compression
            
        Returns:
            Objet File pour l'archive
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        archive_path = Path(archive_name)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        exclude = exclude or []
        
        def should_exclude(file_path: Path) -> bool:
            for pattern in exclude:
                if fnmatch.fnmatch(str(file_path.relative_to(self.path)), pattern):
                    return True
            return False
        
        try:
            with zipfile.ZipFile(archive_path, 'w', 
                               compression=zipfile.ZIP_DEFLATED,
                               compresslevel=compression_level) as zf:
                for file_path in self.path.rglob('*'):
                    if file_path.is_file() and not should_exclude(file_path):
                        arc_name = file_path.relative_to(self.path)
                        zf.write(file_path, arcname=arc_name)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors de la compression") from e
        
        return File(archive_path)
    
    def empty(self) -> bool:
        """
        Vérifie si le dossier est vide.
        
        Returns:
            True si vide
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            return not any(self.path.iterdir())
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée: {self.path}") from e
    
    def clear(self) -> 'Dir':
        """
        Vide le dossier (supprime tout son contenu).
        
        Returns:
            Self pour chaînage
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        try:
            for item in self.path.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
        except PermissionError as e:
            raise FileXPermissionError(f"Permission refusée lors du nettoyage") from e
        
        return self
    
    def created_at(self) -> datetime.datetime:
        """
        Retourne la date de création du dossier.
        
        Returns:
            Date de création
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        timestamp = self.path.stat().st_ctime
        return datetime.datetime.fromtimestamp(timestamp)
    
    def modified_at(self) -> datetime.datetime:
        """
        Retourne la date de modification du dossier.
        
        Returns:
            Date de modification
        """
        if not self.exists():
            raise DirectoryNotFoundError(f"Dossier non trouvé: {self.path}")
        
        timestamp = self.path.stat().st_mtime
        return datetime.datetime.fromtimestamp(timestamp)
    
    def __str__(self) -> str:
        return str(self.path)
    
    def __repr__(self) -> str:
        return f"Dir('{self.path}')"


# Fonctions utilitaires
def find_files(directory: Union[str, Path], pattern: str, recursive: bool = True) -> List[File]:
    """
    Trouve des fichiers selon un pattern.
    
    Args:
        directory: Dossier de recherche
        pattern: Pattern de recherche (ex: "*.py")
        recursive: Recherche récursive
        
    Returns:
        Liste d'objets File
    """
    dir_obj = Dir(directory)
    if not dir_obj.exists():
        raise DirectoryNotFoundError(f"Dossier non trouvé: {directory}")
    
    files = dir_obj.list_files(pattern, recursive)
    return [File(dir_obj.path / f) for f in files]


def find_dirs(directory: Union[str, Path], pattern: str = "*", recursive: bool = True) -> List[Dir]:
    """
    Trouve des dossiers selon un pattern.
    
    Args:
        directory: Dossier de recherche
        pattern: Pattern de recherche
        recursive: Recherche récursive
        
    Returns:
        Liste d'objets Dir
    """
    dir_obj = Dir(directory)
    if not dir_obj.exists():
        raise DirectoryNotFoundError(f"Dossier non trouvé: {directory}")
    
    dirs = dir_obj.list_dirs(recursive)
    if pattern != "*":
        dirs = [d for d in dirs if fnmatch.fnmatch(d, pattern)]
    
    return [Dir(dir_obj.path / d) for d in dirs]


def cleanup_empty_dirs(directory: Union[str, Path]) -> int:
    """
    Supprime récursivement les dossiers vides.
    
    Args:
        directory: Dossier racine
        
    Returns:
        Nombre de dossiers supprimés
    """
    dir_obj = Dir(directory)
    if not dir_obj.exists():
        raise DirectoryNotFoundError(f"Dossier non trouvé: {directory}")
    
    count = 0
    # Parcourir en ordre inverse pour supprimer les sous-dossiers avant les parents
    for dirpath in sorted(dir_obj.path.rglob('*'), key=lambda x: str(x), reverse=True):
        if dirpath.is_dir():
            try:
                dirpath.rmdir()  # Ne fonctionne que si vide
                count += 1
            except OSError:
                pass  # Dossier non vide, on continue
    
    return count