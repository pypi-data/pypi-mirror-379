# =============================================================================
# README.md
# =============================================================================

# Py-FileX - Gestion intelligente des fichiers 📂

[![PyPI version](https://badge.fury.io/py/py-filex.svg)](https://badge.fury.io/py/py-filex)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Py-FileX simplifie la manipulation des fichiers et dossiers en Python avec une API fluide et intuitive. Fini le jonglage entre `os`, `shutil`, `pathlib` et `zipfile` !

## 🚀 Installation

```bash
pip install py-filex
```

## ✨ Fonctionnalités

### 📄 Gestion des fichiers
- ✅ Lecture/écriture simplifiée
- 📁 Copie/déplacement/renommage
- 🗜️ Compression ZIP
- 📊 Informations détaillées (taille, dates, hash)
- 🔗 API fluide et chaînable

### 📂 Gestion des dossiers
- 📋 Listing intelligent avec filtres
- 📊 Analyse (taille, nombre de fichiers)
- 📁 Copie/déplacement avec options avancées
- 🗜️ Compression complète
- 🧹 Nettoyage et maintenance

## 🎯 Exemples d'utilisation

### Fichiers

```python
from filex import File

# Création et manipulation
f = File("data.txt")
f.write("Hello World!")
print(f.read())  # Hello World!

# Copie avec chaînage
f.copy("backup/").zip("archive.zip")

# Informations
print(f.size_human())  # 12 B
print(f.hash_md5())    # a1b2c3...
print(f.created_at())  # 2025-01-15 10:30:45
```

### Dossiers

```python
from filex import Dir

# Création et analyse
d = Dir("my_project")
d.create()

print(d.count_files())     # 42
print(d.size(human_readable=True))  # 1.5 MB

# Listage avec filtres
python_files = d.list_files("*.py", recursive=True)
print(python_files)

# Compression avec exclusions
d.zip("backup.zip", exclude=["*.tmp", "__pycache__", ".git"])

# Copie parallèle
d.copy("backup/", parallel=True, exclude=["node_modules"])
```

### Recherche avancée

```python
from filex import find_files, find_dirs, cleanup_empty_dirs

# Trouver tous les fichiers Python
py_files = find_files("/project", "*.py", recursive=True)

# Nettoyer les dossiers vides
deleted_count = cleanup_empty_dirs("/project")
print(f"{deleted_count} dossiers vides supprimés")
```

## 🎨 API fluide

FileX permet le chaînage d'opérations :

```python
from filex import File, Dir

# Chaînage de fichiers
File("source.txt")\
    .copy("temp.txt")\
    .write("Modified content")\
    .zip("final.zip")

# Chaînage de dossiers  
Dir("project")\
    .create()\
    .copy("backup/")\
    .zip("archive.zip")
```

## 🛡️ Gestion d'erreurs

FileX utilise des exceptions claires et spécifiques :

```python
from filex import File, FileNotFoundError, PermissionError

try:
    f = File("missing.txt")
    content = f.read()
except FileNotFoundError:
    print("Fichier non trouvé !")
except PermissionError:
    print("Permissions insuffisantes !")
```

## 🔧 Fonctionnalités avancées

### Copie parallèle
```python
# Copie rapide de gros dossiers
Dir("large_folder").copy("backup/", parallel=True)
```

### Exclusion de fichiers
```python
# Ignorer certains patterns
Dir("project").zip("clean.zip", exclude=[
    "*.tmp", 
    "__pycache__", 
    "node_modules",
    ".git"
])
```

### Hash et vérification
```python
f = File("important.pdf")
checksum = f.hash_sha256()

# Vérifier l'intégrité plus tard
if f.hash_sha256() == checksum:
    print("Fichier intact !")
```

## 📊 Comparaison

### Avant (Python standard)
```python
import os
import shutil
from pathlib import Path
import zipfile

# Code verbeux et répétitif
if os.path.exists("file.txt"):
    shutil.copy("file.txt", "backup/")
    
with zipfile.ZipFile("archive.zip", 'w') as zf:
    zf.write("file.txt")

# Taille du dossier
total = 0
for root, dirs, files in os.walk("folder"):
    for file in files:
        total += os.path.getsize(os.path.join(root, file))
```

### Après (FileX)
```python
from filex import File, Dir

# Code simple et expressif
File("file.txt").copy("backup/").zip("archive.zip")

# Taille en une ligne
size = Dir("folder").size(human_readable=True)
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez le [guide de contribution](CONTRIBUTING.md).

## 📝 Licence

MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🔗 Liens

- [Documentation complète](https://github.com/Moesthetics-code/py-filex#readme)
- [Issues](https://github.com/Moesthetics-code/py-filex/issues)
- [PyPI](https://pypi.org/project/py-filex/)

---

**Py-FileX** - Parce que manipuler des fichiers devrait être simple ! 🎯
