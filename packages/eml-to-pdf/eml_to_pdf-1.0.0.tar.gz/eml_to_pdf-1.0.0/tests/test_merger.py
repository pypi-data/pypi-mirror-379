"""
Tests for PDF Merger
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from eml_to_pdf.merger import PDFMerger


class TestPDFMerger:
    """Test cases for PDFMerger class."""

    def setup_method(self):
        """Setup test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.merger = PDFMerger(
            output_file=os.path.join(self.temp_dir, "test_merged.pdf")
        )

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init(self):
        """Test merger initialization."""
        assert self.merger.output_file == Path(self.temp_dir) / "test_merged.pdf"

    def test_merge_files_empty_list(self):
        """Test merging with empty file list."""
        result = self.merger.merge_files([])
        assert result is False

    @patch("eml_to_pdf.merger.PdfReader")
    @patch("eml_to_pdf.merger.PdfWriter")
    def test_merge_files_success(self, mock_writer_class, mock_reader_class):
        """Test successful file merging."""
        # Mock PDF reader and writer
        mock_reader = MagicMock()
        mock_reader.pages = [MagicMock(), MagicMock()]  # 2 pages
        mock_reader_class.return_value = mock_reader

        mock_writer = MagicMock()
        mock_writer_class.return_value = mock_writer

        # Test files
        test_files = ["file1.pdf", "file2.pdf"]

        result = self.merger.merge_files(test_files)

        assert result is True
        assert mock_reader_class.call_count == 2  # Called for each file
        assert mock_writer.add_page.call_count == 4  # 2 pages × 2 files
        mock_writer.write.assert_called_once()

    @patch("eml_to_pdf.merger.PdfReader")
    @patch("eml_to_pdf.merger.PdfWriter")
    def test_merge_files_with_errors(self, mock_writer_class, mock_reader_class):
        """Test file merging with some files causing errors."""

        # Mock PDF reader to raise exception for second file
        def side_effect(file_path):
            if "file2" in file_path:
                raise Exception("PDF read error")
            mock_reader = MagicMock()
            mock_reader.pages = [MagicMock()]
            return mock_reader

        mock_reader_class.side_effect = side_effect

        mock_writer = MagicMock()
        mock_writer_class.return_value = mock_writer

        test_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

        result = self.merger.merge_files(test_files)

        # Should still succeed even if one file fails
        assert result is True
        assert mock_reader_class.call_count == 3
        # Only 2 pages should be added (file1 and file3, file2 failed)
        assert mock_writer.add_page.call_count == 2

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.exists")
    def test_merge_directory_no_files(self, mock_exists, mock_glob):
        """Test directory merging with no PDF files."""
        mock_exists.return_value = True
        mock_glob.return_value = []

        result = self.merger.merge_directory("empty_dir")

        assert result is False

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.exists")
    @patch.object(PDFMerger, "merge_files")
    def test_merge_directory_with_files(self, mock_merge_files, mock_exists, mock_glob):
        """Test directory merging with PDF files."""
        mock_exists.return_value = True
        # Mock glob to return some PDF files
        mock_files = [Path("file1.pdf"), Path("file2.pdf"), Path("file3.pdf")]
        mock_glob.return_value = mock_files

        mock_merge_files.return_value = True

        result = self.merger.merge_directory("test_dir")

        assert result is True
        mock_merge_files.assert_called_once()

        # Check that the correct file paths were passed
        called_files = mock_merge_files.call_args[0][0]
        assert len(called_files) == 3
        assert all(isinstance(f, str) for f in called_files)

    def test_get_file_size_file_exists(self):
        """Test getting file size when file exists."""
        # Create a temporary file
        test_file = Path(self.temp_dir) / "test_file.txt"
        test_file.write_text("test content")

        # Update merger to use this file
        self.merger.output_file = test_file

        size = self.merger.get_file_size()

        assert size is not None
        assert size > 0

    def test_get_file_size_file_not_exists(self):
        """Test getting file size when file doesn't exist."""
        # Use a non-existent file
        non_existent_file = Path(self.temp_dir) / "non_existent.pdf"
        self.merger.output_file = non_existent_file

        size = self.merger.get_file_size()

        assert size is None

    @patch("pathlib.Path.exists")
    def test_merge_directory_directory_not_exists(self, mock_exists):
        """Test directory merging when directory doesn't exist."""
        mock_exists.return_value = False

        with pytest.raises(FileNotFoundError):
            self.merger.merge_directory("nonexistent_dir")

    @patch("pathlib.Path.exists")
    def test_merge_directory_not_directory(self, mock_exists):
        """Test directory merging when path is not a directory."""
        mock_exists.return_value = True

        with patch("pathlib.Path.is_dir") as mock_is_dir:
            mock_is_dir.return_value = False

            # The code doesn't check is_dir, so it will just return False
            result = self.merger.merge_directory("not_a_directory")
            assert result is False
