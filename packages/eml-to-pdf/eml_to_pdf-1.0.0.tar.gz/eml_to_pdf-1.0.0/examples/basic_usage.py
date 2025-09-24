"""
Basic usage examples for EML to PDF Converter
"""

from eml_to_pdf import EMLToPDFConverter, PDFMerger


def basic_conversion():
    """Basic EML to PDF conversion example."""
    print("=== Basic EML to PDF Conversion ===")
    
    # Initialize converter
    converter = EMLToPDFConverter(output_dir="converted_pdfs")
    
    # Convert all EML files in a directory
    stats = converter.convert_directory("eml_files")
    
    print(f"Conversion complete!")
    print(f"Total files: {stats['total']}")
    print(f"Successful: {stats['successful']}")
    print(f"Failed: {stats['failed']}")


def single_file_conversion():
    """Single file conversion example."""
    print("\n=== Single File Conversion ===")
    
    converter = EMLToPDFConverter(output_dir="single_pdf")
    
    # Convert a single EML file
    success = converter.convert_single_file("eml_files/example.eml")
    
    if success:
        print("✅ File converted successfully!")
    else:
        print("❌ File conversion failed!")


def pdf_merging():
    """PDF merging example."""
    print("\n=== PDF Merging ===")
    
    # Initialize merger
    merger = PDFMerger("all_emails.pdf")
    
    # Merge all PDFs in a directory
    success = merger.merge_directory("converted_pdfs")
    
    if success:
        size = merger.get_file_size()
        print(f"✅ PDFs merged successfully!")
        print(f"📄 Output file: all_emails.pdf")
        print(f"📊 File size: {size / (1024 * 1024):.1f} MB")
    else:
        print("❌ PDF merging failed!")


def complete_workflow():
    """Complete workflow: convert EMLs and merge PDFs."""
    print("\n=== Complete Workflow ===")
    
    # Step 1: Convert EML files to PDF
    print("Step 1: Converting EML files to PDF...")
    converter = EMLToPDFConverter(output_dir="workflow_pdfs")
    stats = converter.convert_directory("eml_files")
    
    if stats['successful'] == 0:
        print("❌ No files converted successfully!")
        return
    
    print(f"✅ Converted {stats['successful']} files")
    
    # Step 2: Merge PDFs
    print("Step 2: Merging PDFs...")
    merger = PDFMerger("complete_workflow.pdf")
    success = merger.merge_directory("workflow_pdfs")
    
    if success:
        size = merger.get_file_size()
        print(f"✅ Complete workflow finished!")
        print(f"📄 Final file: complete_workflow.pdf")
        print(f"📊 File size: {size / (1024 * 1024):.1f} MB")
    else:
        print("❌ PDF merging failed!")


if __name__ == "__main__":
    # Run examples
    basic_conversion()
    single_file_conversion()
    pdf_merging()
    complete_workflow()
