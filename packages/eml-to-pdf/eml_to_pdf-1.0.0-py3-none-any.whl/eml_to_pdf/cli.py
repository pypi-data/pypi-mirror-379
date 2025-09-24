"""
Command Line Interface for EML to PDF Converter
"""

import argparse
import sys
import logging
from pathlib import Path
from typing import Any

from .converter import EMLToPDFConverter
from .merger import PDFMerger

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def convert_command(args: argparse.Namespace) -> bool:
    """Handle the convert command."""
    try:
        converter = EMLToPDFConverter(output_dir=args.output)
        stats = converter.convert_directory(args.input_dir)

        print(f"\n✅ Conversion complete!")
        print(f"📊 Statistics:")
        print(f"   Total files: {stats['total']}")
        print(f"   Successful: {stats['successful']}")
        print(f"   Failed: {stats['failed']}")
        print(f"📁 Output directory: {args.output}")

        return stats["failed"] == 0

    except Exception as e:
        logger.error(f"Conversion failed: {str(e)}")
        return False


def merge_command(args: argparse.Namespace) -> bool:
    """Handle the merge command."""
    try:
        merger = PDFMerger(output_file=args.output)
        success = merger.merge_directory(args.input_dir)

        if success:
            size = merger.get_file_size()
            size_mb = size / (1024 * 1024) if size else 0
            print(f"\n✅ Merge complete!")
            print(f"📄 Output file: {args.output}")
            print(f"📊 File size: {size_mb:.1f} MB")
        else:
            print(f"\n❌ Merge failed!")

        return success

    except Exception as e:
        logger.error(f"Merge failed: {str(e)}")
        return False


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="EML to PDF Converter - Convert EML email files to PDF format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  eml-to-pdf convert ./emails --output ./pdfs
  eml-to-pdf merge ./pdfs --output all_emails.pdf
  eml-to-pdf convert ./emails --output ./pdfs && eml-to-pdf merge ./pdfs --output all_emails.pdf
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Convert command
    convert_parser = subparsers.add_parser("convert", help="Convert EML files to PDF")
    convert_parser.add_argument("input_dir", help="Directory containing EML files")
    convert_parser.add_argument(
        "--output",
        "-o",
        default="pdf_output",
        help="Output directory for PDF files (default: pdf_output)",
    )

    # Merge command
    merge_parser = subparsers.add_parser(
        "merge", help="Merge PDF files into one document"
    )
    merge_parser.add_argument("input_dir", help="Directory containing PDF files")
    merge_parser.add_argument(
        "--output",
        "-o",
        default="merged.pdf",
        help="Output PDF file (default: merged.pdf)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Validate input directory
    input_path = Path(args.input_dir)
    if not input_path.exists():
        logger.error(f"Input directory does not exist: {args.input_dir}")
        return 1

    if not input_path.is_dir():
        logger.error(f"Input path is not a directory: {args.input_dir}")
        return 1

    # Execute command
    if args.command == "convert":
        success = convert_command(args)
    elif args.command == "merge":
        success = merge_command(args)
    else:
        logger.error(f"Unknown command: {args.command}")
        return 1

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
