# =============================================================================
# CHANGELOG.md
# =============================================================================

# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-15

### Ajouté
- Classe `File` pour la gestion intelligente des fichiers
  - Lecture/écriture avec encodage configurable
  - Copie/déplacement/renommage avec gestion d'erreurs
  - Compression ZIP individuelle
  - Calcul de hash (MD5, SHA256)
  - Informations détaillées (taille, dates, extension)
  
- Classe `Dir` pour la gestion intelligente des dossiers
  - Création et manipulation de dossiers
  - Listage avec filtres et recherche récursive
  - Analyse (taille totale, nombre de fichiers/dossiers)
  - Copie avec exclusions et parallélisation
  - Compression ZIP complète avec filtres
  - Nettoyage et maintenance
  
- Fonctions utilitaires
  - `find_files()` : recherche avancée de fichiers
  - `find_dirs()` : recherche de dossiers
  - `cleanup_empty_dirs()` : nettoyage automatique
  
- API fluide avec chaînage d'opérations
- Gestion d'erreurs avec exceptions spécifiques
- Support complet Python 3.7+
- Tests unitaires complets (>95% couverture)
- Documentation et exemples détaillés

### Fonctionnalités techniques
- Compatible Windows/Linux/macOS via pathlib
- Gestion des permissions et erreurs d'accès
- Support de la copie parallèle pour les gros volumes
- Compression ZIP avec niveaux configurables
- Hash cryptographiques pour vérification d'intégrité
- Formats de taille lisibles (KB, MB, GB, etc.)

## [Unreleased]

### Prévu pour v1.1.0
- Support du cloud (S3, Google Drive, Dropbox)
- Interface en ligne de commande (CLI)
- Plugin system pour extensions
- Monitoring et callbacks de progression
- Support des liens symboliques
- Synchronisation bidirectionnelle