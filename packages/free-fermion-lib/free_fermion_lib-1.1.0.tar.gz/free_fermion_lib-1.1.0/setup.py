"""
Setup script for the Free Fermion Library package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A Python package for free fermion systems"

# Read requirements from requirements.txt
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="free-fermion-lib",
    version="1.1.0",
    author="James D. Whitfield",
    author_email="James.D.Whitfield@dartmouth.edu",
    description="A comprehensive Python library for free fermion systems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/jdwhitfield/free-fermion-lib",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "nbsphinx>=0.8",
        ],
    },
    keywords=[
        "quantum physics",
        "free fermions",
        "combinatorics",
        "graph theory",
        "pfaffian",
        "quantum computing",
        "linear algebra",
        "symplectic",
    ],
    project_urls={
        "Bug Reports": "https://github.com/jdwhitfield/free-fermion-lib/issues",
        "Source": "https://github.com/jdwhitfield/free-fermion-lib",
        "Documentation": "https://free-fermion-lib.readthedocs.io/",
    },
    include_package_data=True,
    zip_safe=False,
)