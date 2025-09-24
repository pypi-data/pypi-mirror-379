"""
PDF Merger

A professional PDF merger for combining multiple PDF files into one document.
"""

import os
import logging
from pathlib import Path
from typing import List, Optional

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    raise ImportError("PyPDF2 is required. Install with: pip install PyPDF2")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFMerger:
    """
    A professional PDF merger for combining multiple PDF files.

    This class handles the merging of multiple PDF files into a single document
    with proper error handling and progress tracking.
    """

    def __init__(self, output_file: str = "merged.pdf"):
        """
        Initialize the PDF merger.

        Args:
            output_file (str): Path for the output merged PDF file
        """
        self.output_file = Path(output_file)

    def merge_files(self, pdf_files: List[str]) -> bool:
        """
        Merge multiple PDF files into one document.

        Args:
            pdf_files: List of paths to PDF files to merge

        Returns:
            True if merging successful, False otherwise
        """
        if not pdf_files:
            logger.warning("No PDF files provided for merging")
            return False

        # Sort files for consistent ordering
        pdf_files.sort()

        logger.info(f"Found {len(pdf_files)} PDF files to merge...")

        try:
            # Create PDF writer
            writer = PdfWriter()

            # Add each PDF file
            for i, pdf_path in enumerate(pdf_files, 1):
                filename = Path(pdf_path).name
                logger.info(f"Adding {i}/{len(pdf_files)}: {filename}")

                try:
                    reader = PdfReader(pdf_path)

                    # Add all pages from the current PDF
                    for page in reader.pages:
                        writer.add_page(page)

                except Exception as e:
                    logger.error(f"Error processing {filename}: {str(e)}")
                    continue

            # Write the merged PDF
            logger.info(f"Writing merged PDF to {self.output_file}...")
            with open(self.output_file, "wb") as output_file:
                writer.write(output_file)

            logger.info(
                f"✅ Successfully merged {len(pdf_files)} PDFs into {self.output_file}"
            )
            return True

        except Exception as e:
            logger.error(f"Error during merging: {str(e)}")
            return False

    def merge_directory(self, input_dir: str, pattern: str = "*.pdf") -> bool:
        """
        Merge all PDF files in a directory.

        Args:
            input_dir: Directory containing PDF files
            pattern: File pattern to match (default: "*.pdf")

        Returns:
            True if merging successful, False otherwise
        """
        input_path = Path(input_dir)
        if not input_path.exists():
            raise FileNotFoundError(f"Directory {input_dir} does not exist")

        # Find all PDF files
        pdf_files = list(input_path.glob(pattern))

        if not pdf_files:
            logger.warning(f"No PDF files found in {input_dir}")
            return False

        return self.merge_files([str(f) for f in pdf_files])

    def get_file_size(self) -> Optional[int]:
        """
        Get the size of the merged PDF file in bytes.

        Returns:
            File size in bytes or None if file doesn't exist
        """
        if self.output_file.exists():
            return self.output_file.stat().st_size
        return None
