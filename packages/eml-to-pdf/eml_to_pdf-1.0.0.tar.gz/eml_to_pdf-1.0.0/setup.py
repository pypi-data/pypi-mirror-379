"""
Setup script for EML to PDF Converter
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements
requirements = []
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="eml-to-pdf",
    version="1.0.0",
    author="Abdullah Zaki",
    author_email="zakiapdu10@gmail.com",
    description="A professional Python package for converting EML email files to PDF format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlienZaki/eml-to-pdf",
    project_urls={
        "Bug Reports": "https://github.com/AlienZaki/eml-to-pdf/issues",
        "Source": "https://github.com/AlienZaki/eml-to-pdf",
        "Documentation": "https://github.com/AlienZaki/eml-to-pdf#readme",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Email",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.900",
            "pre-commit>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "eml-to-pdf=eml_to_pdf.cli:main",
        ],
    },
    keywords="eml email pdf conversion html weasyprint",
    include_package_data=True,
    zip_safe=False,
)
