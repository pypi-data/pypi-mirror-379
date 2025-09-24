# =============================================================================
# setup.py
# =============================================================================

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-filex",
    version="1.0.0",
    author="Mohamed Ndiaye",
    author_email="mintok2000@gmail.com",
    description="Gestion intelligente des fichiers et dossiers en Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moesthetics-code/py-filex",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Filesystems",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    keywords="file management, directory, filesystem, utility",
    project_urls={
        "Bug Reports": "https://github.com/Moesthetics-code/py-filex/issues",
        "Source": "https://github.com/Moesthetics-code/py-filex",
        "Documentation": "https://github.com/Moesthetics-code/py-filex#readme",
    },
)