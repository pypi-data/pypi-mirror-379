"""
Tests for EML to PDF Converter
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from eml_to_pdf.converter import EMLToPDFConverter


class TestEMLToPDFConverter:
    """Test cases for EMLToPDFConverter class."""

    def setup_method(self):
        """Setup test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.converter = EMLToPDFConverter(output_dir=self.temp_dir)

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init(self):
        """Test converter initialization."""
        assert self.converter.output_dir == Path(self.temp_dir)
        assert self.converter.output_dir.exists()

    def test_decode_mime_header(self):
        """Test MIME header decoding."""
        # Test normal header
        result = self.converter.decode_mime_header("Test Subject")
        assert result == "Test Subject"

        # Test None input
        result = self.converter.decode_mime_header(None)
        assert result == ""

        # Test encoded header
        encoded_header = "=?utf-8?B?VGVzdCBTdWJqZWN0?="
        result = self.converter.decode_mime_header(encoded_header)
        assert "Test Subject" in result

    def test_clean_html_for_pdf(self):
        """Test HTML cleaning functionality."""
        html_with_tracking = """
        <p>Hello World</p>
        <img src="tracking.png" style="display: none; width: 1px; height: 1px;">
        <img src="normal.png" alt="Normal image">
        """

        cleaned = self.converter.clean_html_for_pdf(html_with_tracking)

        # Should remove tracking images
        assert "display: none" not in cleaned
        assert "width: 1px" not in cleaned
        assert "height: 1px" not in cleaned
        # Should keep normal images
        assert "normal.png" in cleaned

    @patch("email.message_from_bytes")
    def test_extract_email_content_success(self, mock_message_from_bytes):
        """Test successful email content extraction."""
        # Mock email message
        mock_msg = MagicMock()
        mock_msg.get.side_effect = lambda key, default: {
            "Subject": "Test Subject",
            "From": "test@example.com",
            "To": "recipient@example.com",
            "Date": "Mon, 1 Jan 2024 12:00:00 +0000",
        }.get(key, default)

        mock_msg.is_multipart.return_value = False
        mock_msg.get_content_type.return_value = "text/plain"
        mock_msg.get_payload.return_value = b"Test email body"

        mock_message_from_bytes.return_value = mock_msg

        # Create a temporary EML file
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".eml", delete=False) as f:
            f.write(b"Mock EML content")
            eml_path = f.name

        try:
            result = self.converter.extract_email_content(eml_path)

            assert result is not None
            assert result["subject"] == "Test Subject"
            assert result["from"] == "test@example.com"
            assert result["to"] == "recipient@example.com"
            assert "Test email body" in result["body"]
        finally:
            os.unlink(eml_path)

    def test_extract_email_content_file_not_found(self):
        """Test email extraction with non-existent file."""
        result = self.converter.extract_email_content("nonexistent.eml")
        assert result is None

    def test_create_html_template(self):
        """Test HTML template creation."""
        email_data = {
            "subject": "Test Subject",
            "from": "sender@example.com",
            "to": "recipient@example.com",
            "date": "Mon, 1 Jan 2024 12:00:00 +0000",
            "body": "<p>Test email body</p>",
        }

        html = self.converter.create_html_template(email_data)

        assert "Test Subject" in html
        assert "sender@example.com" in html
        assert "recipient@example.com" in html
        assert "Test email body" in html
        assert "<!DOCTYPE html>" in html
        assert '<html lang="en">' in html

    @patch("eml_to_pdf.converter.HTML")
    def test_convert_single_file_success(self, mock_html):
        """Test successful single file conversion."""
        # Mock WeasyPrint HTML
        mock_html_instance = MagicMock()
        mock_html.return_value = mock_html_instance

        # Mock email data
        with patch.object(self.converter, "extract_email_content") as mock_extract:
            mock_extract.return_value = {
                "subject": "Test Subject",
                "from": "sender@example.com",
                "to": "recipient@example.com",
                "date": "Mon, 1 Jan 2024 12:00:00 +0000",
                "body": "<p>Test email body</p>",
            }

            # Create a temporary EML file
            with tempfile.NamedTemporaryFile(
                mode="wb", suffix=".eml", delete=False
            ) as f:
                f.write(b"Mock EML content")
                eml_path = f.name

            try:
                result = self.converter.convert_single_file(eml_path)
                assert result is True
                mock_html_instance.write_pdf.assert_called_once()
            finally:
                os.unlink(eml_path)

    def test_convert_single_file_extraction_fails(self):
        """Test single file conversion when extraction fails."""
        with patch.object(self.converter, "extract_email_content") as mock_extract:
            mock_extract.return_value = None

            result = self.converter.convert_single_file("test.eml")
            assert result is False

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.exists")
    def test_convert_directory_no_files(self, mock_exists, mock_glob):
        """Test directory conversion with no EML files."""
        mock_exists.return_value = True
        mock_glob.return_value = []

        stats = self.converter.convert_directory("empty_dir")

        assert stats["total"] == 0
        assert stats["successful"] == 0
        assert stats["failed"] == 0

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.exists")
    @patch.object(EMLToPDFConverter, "convert_single_file")
    def test_convert_directory_with_files(self, mock_convert, mock_exists, mock_glob):
        """Test directory conversion with EML files."""
        mock_exists.return_value = True
        # Mock glob to return some EML files
        mock_files = [Path("file1.eml"), Path("file2.eml"), Path("file3.eml")]
        mock_glob.return_value = mock_files

        # Mock convert_single_file to return different results
        mock_convert.side_effect = [True, False, True]

        stats = self.converter.convert_directory("test_dir")

        assert stats["total"] == 3
        assert stats["successful"] == 2
        assert stats["failed"] == 1
        assert mock_convert.call_count == 3
