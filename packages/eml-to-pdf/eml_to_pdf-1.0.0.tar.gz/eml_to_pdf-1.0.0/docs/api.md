# API Reference

## EMLToPDFConverter

The main class for converting EML email files to PDF format.

### Constructor

```python
EMLToPDFConverter(output_dir: str = "pdf_output")
```

**Parameters:**
- `output_dir` (str): Directory to save converted PDF files

### Methods

#### `convert_single_file(eml_file_path: str) -> bool`

Convert a single EML file to PDF.

**Parameters:**
- `eml_file_path` (str): Path to the EML file

**Returns:**
- `bool`: True if conversion successful, False otherwise

**Example:**
```python
converter = EMLToPDFConverter()
success = converter.convert_single_file("email.eml")
```

#### `convert_directory(input_dir: str) -> Dict[str, int]`

Convert all EML files in a directory.

**Parameters:**
- `input_dir` (str): Directory containing EML files

**Returns:**
- `Dict[str, int]`: Dictionary with conversion statistics
  - `total`: Total number of files processed
  - `successful`: Number of successful conversions
  - `failed`: Number of failed conversions

**Example:**
```python
converter = EMLToPDFConverter()
stats = converter.convert_directory("emails/")
print(f"Converted {stats['successful']}/{stats['total']} files")
```

#### `extract_email_content(eml_file_path: str) -> Optional[Dict[str, Any]]`

Extract content from an EML file.

**Parameters:**
- `eml_file_path` (str): Path to the EML file

**Returns:**
- `Optional[Dict[str, Any]]`: Dictionary containing email data or None if extraction failed
  - `subject`: Email subject
  - `from`: Sender address
  - `to`: Recipient address
  - `date`: Email date
  - `body`: Email body (HTML)

#### `create_html_template(email_data: Dict[str, Any]) -> str`

Create HTML template with modern email styling.

**Parameters:**
- `email_data` (Dict[str, Any]): Dictionary containing email data

**Returns:**
- `str`: Complete HTML document as string

## PDFMerger

A class for merging multiple PDF files into one document.

### Constructor

```python
PDFMerger(output_file: str = "merged.pdf")
```

**Parameters:**
- `output_file` (str): Path for the output merged PDF file

### Methods

#### `merge_files(pdf_files: List[str]) -> bool`

Merge multiple PDF files into one document.

**Parameters:**
- `pdf_files` (List[str]): List of paths to PDF files to merge

**Returns:**
- `bool`: True if merging successful, False otherwise

**Example:**
```python
merger = PDFMerger("output.pdf")
success = merger.merge_files(["file1.pdf", "file2.pdf", "file3.pdf"])
```

#### `merge_directory(input_dir: str, pattern: str = "*.pdf") -> bool`

Merge all PDF files in a directory.

**Parameters:**
- `input_dir` (str): Directory containing PDF files
- `pattern` (str): File pattern to match (default: "*.pdf")

**Returns:**
- `bool`: True if merging successful, False otherwise

**Example:**
```python
merger = PDFMerger("all_emails.pdf")
success = merger.merge_directory("pdf_files/")
```

#### `get_file_size() -> Optional[int]`

Get the size of the merged PDF file in bytes.

**Returns:**
- `Optional[int]`: File size in bytes or None if file doesn't exist

**Example:**
```python
merger = PDFMerger("output.pdf")
merger.merge_files(["file1.pdf", "file2.pdf"])
size = merger.get_file_size()
if size:
    print(f"File size: {size / 1024 / 1024:.1f} MB")
```

## Command Line Interface

The package provides a command-line interface for easy usage.

### Convert Command

```bash
eml-to-pdf convert <input_dir> [--output <output_dir>]
```

**Arguments:**
- `input_dir`: Directory containing EML files
- `--output`, `-o`: Output directory for PDF files (default: pdf_output)

**Example:**
```bash
eml-to-pdf convert ./emails --output ./pdfs
```

### Merge Command

```bash
eml-to-pdf merge <input_dir> [--output <output_file>]
```

**Arguments:**
- `input_dir`: Directory containing PDF files
- `--output`, `-o`: Output PDF file (default: merged.pdf)

**Example:**
```bash
eml-to-pdf merge ./pdfs --output all_emails.pdf
```

## Error Handling

The package includes comprehensive error handling:

- **FileNotFoundError**: Raised when input directories don't exist
- **ImportError**: Raised when required dependencies are missing
- **Exception**: General exceptions are caught and logged

## Logging

The package uses Python's built-in logging module. Configure logging level:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

Available log levels:
- `DEBUG`: Detailed information for debugging
- `INFO`: General information about program execution
- `WARNING`: Warning messages for potential issues
- `ERROR`: Error messages for failed operations
- `CRITICAL`: Critical errors that may cause program termination
