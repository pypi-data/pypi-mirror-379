# =============================================================================
# tests/test_utils.py
# =============================================================================

import pytest
import tempfile
import shutil
from pathlib import Path

from filex import find_files, find_dirs, cleanup_empty_dirs, Dir


class TestUtils:
    
    def setup_method(self):
        """Préparation"""
        self.temp_dir = Path(tempfile.mkdtemp())
        
    def teardown_method(self):
        """Nettoyage"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def test_find_files(self):
        """Test recherche de fichiers"""
        # Créer structure test
        test_dir = self.temp_dir / "search_test"
        test_dir.mkdir()
        
        (test_dir / "file1.py").write_text("python")
        (test_dir / "file2.txt").write_text("text")
        (test_dir / "subdir").mkdir()
        (test_dir / "subdir" / "file3.py").write_text("python")
        
        # Recherche
        py_files = find_files(test_dir, "*.py")
        
        assert len(py_files) == 2
        names = [f.full_name() for f in py_files]
        assert "file1.py" in names
        assert "file3.py" in names
    
    def test_find_dirs(self):
        """Test recherche de dossiers"""
        # Créer structure
        test_dir = self.temp_dir / "search_test"
        test_dir.mkdir()
        
        (test_dir / "dir1").mkdir()
        (test_dir / "dir2").mkdir() 
        (test_dir / "dir1" / "subdir").mkdir()
        
        # Recherche
        dirs = find_dirs(test_dir)
        
        assert len(dirs) >= 2  # Au moins dir1 et dir2
    
    def test_cleanup_empty_dirs(self):
        """Test nettoyage dossiers vides"""
        # Créer structure avec dossiers vides
        test_dir = self.temp_dir / "cleanup_test"
        test_dir.mkdir()
        
        (test_dir / "empty1").mkdir()
        (test_dir / "empty2").mkdir()
        (test_dir / "nonempty").mkdir()
        (test_dir / "nonempty" / "file.txt").write_text("content")
        
        # Nettoyage
        count = cleanup_empty_dirs(test_dir)
        
        assert count >= 2  # Au moins empty1 et empty2
        assert not (test_dir / "empty1").exists()
        assert not (test_dir / "empty2").exists()
        assert (test_dir / "nonempty").exists()  # Contient un fichier