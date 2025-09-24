"""
EML to PDF Converter

A professional Python package for converting EML email files to PDF format
with HTML rendering support for better email appearance.
"""

__version__ = "1.0.0"
__author__ = "Abdullah Zaki"
__email__ = "zakiapdu10@gmail.com"

from .converter import EMLToPDFConverter
from .merger import PDFMerger

__all__ = ["EMLToPDFConverter", "PDFMerger"]
