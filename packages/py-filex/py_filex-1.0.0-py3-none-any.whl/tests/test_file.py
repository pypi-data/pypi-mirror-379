# =============================================================================
# tests/test_file.py
# =============================================================================

import pytest
import tempfile
import shutil
from pathlib import Path
import zipfile

from filex import File, FileNotFoundError, PermissionError


class TestFile:
    
    def setup_method(self):
        """Préparation avant chaque test"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_file = self.temp_dir / "test.txt"
        self.test_content = "Hello FileX!"
        
    def teardown_method(self):
        """Nettoyage après chaque test"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def test_file_creation(self):
        """Test création d'un objet File"""
        f = File(self.test_file)
        assert str(f.path) == str(self.test_file)
        
    def test_write_and_read(self):
        """Test écriture et lecture"""
        f = File(self.test_file)
        
        # Écriture
        f.write(self.test_content)
        assert f.exists()
        
        # Lecture
        content = f.read()
        assert content == self.test_content
    
    def test_read_nonexistent_file(self):
        """Test lecture d'un fichier inexistant"""
        f = File(self.temp_dir / "nonexistent.txt")
        
        with pytest.raises(FileNotFoundError):
            f.read()
    
    def test_append(self):
        """Test ajout de contenu"""
        f = File(self.test_file)
        f.write("Hello")
        f.append(" World!")
        
        assert f.read() == "Hello World!"
    
    def test_copy(self):
        """Test copie de fichier"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        # Copie vers un nouveau fichier
        dest = self.temp_dir / "copy.txt"
        copied = f.copy(dest)
        
        assert copied.exists()
        assert copied.read() == self.test_content
        assert f.exists()  # Original toujours là
    
    def test_move(self):
        """Test déplacement de fichier"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        # Déplacement
        dest = self.temp_dir / "moved.txt"
        f.move(dest)
        
        assert f.path == dest
        assert f.exists()
        assert not self.test_file.exists()
    
    def test_rename(self):
        """Test renommage"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        f.rename("renamed.txt")
        
        assert f.path.name == "renamed.txt"
        assert f.exists()
        assert not self.test_file.exists()
    
    def test_delete(self):
        """Test suppression"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        assert f.exists()
        result = f.delete()
        
        assert result is True
        assert not f.exists()
    
    def test_size(self):
        """Test calcul de taille"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        size = f.size()
        assert size == len(self.test_content.encode())
        
        # Test format lisible
        human_size = f.size_human()
        assert "B" in human_size
    
    def test_extension(self):
        """Test récupération d'extension"""
        f = File(self.temp_dir / "test.py")
        assert f.extension() == "py"
        
        f2 = File(self.temp_dir / "noext")
        assert f2.extension() == ""
    
    def test_zip(self):
        """Test compression ZIP"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        archive = self.temp_dir / "test.zip"
        zip_file = f.zip(archive)
        
        assert zip_file.exists()
        
        # Vérifier le contenu de l'archive
        with zipfile.ZipFile(archive, 'r') as zf:
            files = zf.namelist()
            assert "test.txt" in files
    
    def test_hash(self):
        """Test calcul de hash"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        md5_hash = f.hash_md5()
        sha256_hash = f.hash_sha256()
        
        assert len(md5_hash) == 32
        assert len(sha256_hash) == 64
        
        # Même contenu = même hash
        f2 = File(self.temp_dir / "test2.txt")
        f2.write(self.test_content)
        
        assert f.hash_md5() == f2.hash_md5()
    
    def test_dates(self):
        """Test récupération des dates"""
        f = File(self.test_file)
        f.write(self.test_content)
        
        created = f.created_at()
        modified = f.modified_at()
        
        assert created is not None
        assert modified is not None
    
    def test_chaining(self):
        """Test chaînage d'opérations"""
        f = File(self.test_file)
        
        # Chaînage fluide
        result = f.write("Test").append(" Chain")
        
        assert result == f  # Retourne self
        assert f.read() == "Test Chain"