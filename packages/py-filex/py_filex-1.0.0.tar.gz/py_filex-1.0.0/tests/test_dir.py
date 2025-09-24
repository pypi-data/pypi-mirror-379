# =============================================================================
# tests/test_dir.py  
# =============================================================================

import pytest
import tempfile
import shutil
from pathlib import Path

from filex import Dir, DirectoryNotFoundError, PermissionError


class TestDir:
    
    def setup_method(self):
        """Préparation avant chaque test"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_dir = self.temp_dir / "test_folder"
        
    def teardown_method(self):
        """Nettoyage après chaque test"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def test_dir_creation(self):
        """Test création d'un objet Dir"""
        d = Dir(self.test_dir)
        assert str(d.path) == str(self.test_dir)
    
    def test_create_directory(self):
        """Test création de dossier"""
        d = Dir(self.test_dir)
        
        assert not d.exists()
        d.create()
        assert d.exists()
    
    def test_list_contents(self):
        """Test listage du contenu"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer des fichiers test
        (self.test_dir / "file1.txt").write_text("test1")
        (self.test_dir / "file2.py").write_text("test2")
        (self.test_dir / "subdir").mkdir()
        
        # Test listage complet
        contents = d.list()
        assert "file1.txt" in contents
        assert "file2.py" in contents
        assert "subdir" in contents
        
        # Test listage fichiers seulement
        files = d.list_files()
        assert len(files) == 2
        assert "file1.txt" in files
        assert "subdir" not in files
        
        # Test listage avec pattern
        py_files = d.list_files("*.py")
        assert py_files == ["file2.py"]
    
    def test_size_calculation(self):
        """Test calcul de taille"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer des fichiers
        (self.test_dir / "file1.txt").write_text("Hello")
        (self.test_dir / "file2.txt").write_text("World!")
        
        size = d.size()
        expected = len("Hello") + len("World!")
        assert size == expected
        
        # Test format lisible
        human_size = d.size(human_readable=True)
        assert isinstance(human_size, str)
        assert "B" in human_size
    
    def test_count_files_and_dirs(self):
        """Test comptage"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer structure test
        (self.test_dir / "file1.txt").write_text("test")
        (self.test_dir / "file2.txt").write_text("test")
        (self.test_dir / "subdir1").mkdir()
        (self.test_dir / "subdir2").mkdir()
        (self.test_dir / "subdir1" / "file3.txt").write_text("test")
        
        assert d.count_files() == 3  # Récursif par défaut
        assert d.count_files(recursive=False) == 2
        assert d.count_dirs() == 2
    
    def test_copy_directory(self):
        """Test copie de dossier"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer contenu
        (self.test_dir / "file.txt").write_text("test")
        (self.test_dir / "subdir").mkdir()
        
        # Copie
        dest = self.temp_dir / "copy_dest"
        copied = d.copy(dest)
        
        assert copied.exists()
        assert (dest / "file.txt").exists()
        assert (dest / "subdir").exists()
    
    def test_copy_with_exclude(self):
        """Test copie avec exclusions"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer fichiers
        (self.test_dir / "keep.txt").write_text("keep")
        (self.test_dir / "exclude.tmp").write_text("exclude")
        (self.test_dir / "keep.py").write_text("keep")
        
        # Copie avec exclusion
        dest = self.temp_dir / "copy_dest"
        d.copy(dest, exclude=["*.tmp"])
        
        assert (dest / "keep.txt").exists()
        assert (dest / "keep.py").exists()
        assert not (dest / "exclude.tmp").exists()
    
    def test_move_directory(self):
        """Test déplacement de dossier"""
        d = Dir(self.test_dir)
        d.create()
        (self.test_dir / "file.txt").write_text("test")
        
        dest = self.temp_dir / "moved"
        d.move(dest)
        
        assert d.path == dest
        assert d.exists()
        assert not self.test_dir.exists()
    
    def test_delete_directory(self):
        """Test suppression de dossier"""
        d = Dir(self.test_dir)
        d.create()
        
        # Test suppression dossier vide
        assert d.delete() is True
        assert not d.exists()
        
        # Test suppression dossier avec contenu
        d.create()
        (self.test_dir / "file.txt").write_text("test")
        
        # Sans force, doit échouer
        with pytest.raises(Exception):
            d.delete()
        
        # Avec force, doit réussir
        assert d.delete(force=True) is True
    
    def test_zip_directory(self):
        """Test compression ZIP"""
        d = Dir(self.test_dir)
        d.create()
        
        # Créer contenu
        (self.test_dir / "file1.txt").write_text("content1")
        (self.test_dir / "subdir").mkdir()
        (self.test_dir / "subdir" / "file2.txt").write_text("content2")
        
        # Compression
        archive = self.temp_dir / "test.zip"
        zip_file = d.zip(archive)
        
        assert zip_file.exists()
        
        # Vérifier contenu
        import zipfile
        with zipfile.ZipFile(archive, 'r') as zf:
            files = zf.namelist()
            assert "file1.txt" in files
            assert "subdir/file2.txt" in files
    
    def test_empty_and_clear(self):
        """Test vérification vide et nettoyage"""
        d = Dir(self.test_dir)
        d.create()
        
        # Dossier vide
        assert d.empty() is True
        
        # Ajouter contenu
        (self.test_dir / "file.txt").write_text("test")
        assert d.empty() is False
        
        # Nettoyer
        d.clear()
        assert d.empty() is True
        assert d.exists()  # Le dossier existe toujours