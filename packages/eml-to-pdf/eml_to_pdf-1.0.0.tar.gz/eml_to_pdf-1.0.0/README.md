# EML to PDF Converter

A professional Python package for converting EML email files to PDF format with HTML rendering support for better email appearance.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Features

- **HTML Rendering**: Preserves original email formatting and styling
- **Modern Appearance**: Clean, professional PDF layout similar to modern email clients
- **Batch Processing**: Convert multiple EML files at once
- **PDF Merging**: Combine multiple PDFs into a single document
- **Error Handling**: Robust error handling with detailed logging
- **Easy to Use**: Simple command-line interface and Python API

## Installation

### Using pip

```bash
pip install eml-to-pdf
```

### From source

```bash
git clone https://github.com/AlienZaki/eml-to-pdf.git
cd eml-to-pdf
pip install -e .
```

## Quick Start

### Command Line Usage

Convert all EML files in a directory to PDF:

```bash
eml-to-pdf convert /path/to/eml/files --output /path/to/output
```

Merge multiple PDFs into one file:

```bash
eml-to-pdf merge /path/to/pdf/files --output merged.pdf
```

### Python API Usage

```python
from eml_to_pdf import EMLToPDFConverter, PDFMerger

# Convert EML files to PDF
converter = EMLToPDFConverter(output_dir="pdf_output")
stats = converter.convert_directory("eml_files")
print(f"Converted {stats['successful']}/{stats['total']} files")

# Merge PDFs
merger = PDFMerger("merged_emails.pdf")
merger.merge_directory("pdf_output")
```

## Requirements

- Python 3.8+
- WeasyPrint (for HTML to PDF conversion)
- PyPDF2 (for PDF merging)

## Dependencies

The package requires the following system dependencies:

### Ubuntu/Debian
```bash
sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```

### macOS
```bash
brew install pango
```

### Windows
WeasyPrint should work out of the box on Windows.

## Usage Examples

### Basic Conversion

```python
from eml_to_pdf import EMLToPDFConverter

# Initialize converter
converter = EMLToPDFConverter(output_dir="converted_pdfs")

# Convert single file
success = converter.convert_single_file("email.eml")

# Convert all files in directory
stats = converter.convert_directory("eml_files")
print(f"Successfully converted {stats['successful']} files")
```

### Advanced Usage

```python
from eml_to_pdf import EMLToPDFConverter, PDFMerger
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Convert with custom settings
converter = EMLToPDFConverter(output_dir="custom_output")
stats = converter.convert_directory("eml_files")

# Merge with custom output name
merger = PDFMerger("my_emails.pdf")
success = merger.merge_directory("custom_output")

if success:
    size = merger.get_file_size()
    print(f"Created merged PDF: {size} bytes")
```

### Command Line Examples

```bash
# Convert EML files
eml-to-pdf convert ./emails --output ./pdfs

# Merge PDFs
eml-to-pdf merge ./pdfs --output all_emails.pdf

# Convert and merge in one go
eml-to-pdf convert ./emails --output ./pdfs && eml-to-pdf merge ./pdfs --output all_emails.pdf
```

## Project Structure

```
eml-to-pdf/
├── src/
│   └── eml_to_pdf/
│       ├── __init__.py
│       ├── converter.py      # EML to PDF conversion
│       └── merger.py         # PDF merging functionality
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── tests/
│   ├── test_converter.py
│   └── test_merger.py
├── docs/
│   └── api.md
├── README.md
├── setup.py
├── requirements.txt
└── LICENSE
```

## API Reference

### EMLToPDFConverter

#### `__init__(output_dir: str = "pdf_output")`
Initialize the converter with output directory.

#### `convert_single_file(eml_file_path: str) -> bool`
Convert a single EML file to PDF.

#### `convert_directory(input_dir: str) -> Dict[str, int]`
Convert all EML files in a directory.

### PDFMerger

#### `__init__(output_file: str = "merged.pdf")`
Initialize the merger with output file path.

#### `merge_files(pdf_files: List[str]) -> bool`
Merge a list of PDF files.

#### `merge_directory(input_dir: str, pattern: str = "*.pdf") -> bool`
Merge all PDF files in a directory.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/AlienZaki/eml-to-pdf.git
cd eml-to-pdf

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
black src/ tests/
flake8 src/ tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0
- Initial release
- EML to PDF conversion with HTML rendering
- PDF merging functionality
- Command-line interface
- Python API

## Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/yourusername/eml-to-pdf/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## Acknowledgments

- [WeasyPrint](https://weasyprint.org/) for HTML to PDF conversion
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF manipulation
- The Python community for excellent libraries and tools
