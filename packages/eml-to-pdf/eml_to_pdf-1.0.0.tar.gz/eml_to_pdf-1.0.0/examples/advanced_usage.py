"""
Advanced usage examples for EML to PDF Converter
"""

import logging
from pathlib import Path
from eml_to_pdf import EMLToPDFConverter, PDFMerger


def setup_logging():
    """Setup advanced logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('eml_to_pdf.log'),
            logging.StreamHandler()
        ]
    )


def batch_processing_with_error_handling():
    """Advanced batch processing with comprehensive error handling."""
    print("=== Advanced Batch Processing ===")
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Initialize converter with custom output directory
    converter = EMLToPDFConverter(output_dir="advanced_pdfs")
    
    try:
        # Convert with detailed statistics
        stats = converter.convert_directory("eml_files")
        
        # Detailed reporting
        logger.info(f"Batch processing complete!")
        logger.info(f"Total files processed: {stats['total']}")
        logger.info(f"Successfully converted: {stats['successful']}")
        logger.info(f"Failed conversions: {stats['failed']}")
        
        # Calculate success rate
        if stats['total'] > 0:
            success_rate = (stats['successful'] / stats['total']) * 100
            logger.info(f"Success rate: {success_rate:.1f}%")
        
        return stats
        
    except Exception as e:
        logger.error(f"Batch processing failed: {str(e)}")
        return None


def selective_conversion():
    """Convert only specific EML files based on criteria."""
    print("\n=== Selective Conversion ===")
    
    converter = EMLToPDFConverter(output_dir="selective_pdfs")
    
    # Find specific EML files (example: only files with "interview" in name)
    eml_dir = Path("eml_files")
    interview_files = list(eml_dir.glob("*interview*.eml"))
    
    print(f"Found {len(interview_files)} interview-related emails")
    
    successful = 0
    for eml_file in interview_files:
        if converter.convert_single_file(str(eml_file)):
            successful += 1
            print(f"✅ Converted: {eml_file.name}")
        else:
            print(f"❌ Failed: {eml_file.name}")
    
    print(f"Selective conversion complete: {successful}/{len(interview_files)} files")


def custom_merging_strategy():
    """Custom PDF merging with specific ordering."""
    print("\n=== Custom Merging Strategy ===")
    
    # Create merger
    merger = PDFMerger("custom_merged.pdf")
    
    # Get all PDF files and sort them by modification time (newest first)
    pdf_dir = Path("advanced_pdfs")
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    # Sort by modification time (newest first)
    pdf_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    print(f"Found {len(pdf_files)} PDF files")
    print("Merging in chronological order (newest first)...")
    
    # Convert to string paths for merging
    pdf_paths = [str(f) for f in pdf_files]
    
    success = merger.merge_files(pdf_paths)
    
    if success:
        size = merger.get_file_size()
        print(f"✅ Custom merge complete!")
        print(f"📄 Output: custom_merged.pdf")
        print(f"📊 Size: {size / (1024 * 1024):.1f} MB")
    else:
        print("❌ Custom merge failed!")


def file_management():
    """Advanced file management and cleanup."""
    print("\n=== File Management ===")
    
    # Create different output directories for different purposes
    directories = {
        "interviews": "interview_emails",
        "rejections": "rejection_emails", 
        "confirmations": "confirmation_emails",
        "others": "other_emails"
    }
    
    converter = EMLToPDFConverter()
    
    for category, output_dir in directories.items():
        print(f"Processing {category} emails...")
        converter.output_dir = Path(output_dir)
        converter.output_dir.mkdir(exist_ok=True)
        
        # This is a simplified example - in reality you'd filter files by category
        stats = converter.convert_directory("eml_files")
        print(f"  Converted {stats['successful']} files to {output_dir}/")


def performance_monitoring():
    """Monitor conversion performance."""
    print("\n=== Performance Monitoring ===")
    
    import time
    
    converter = EMLToPDFConverter(output_dir="performance_pdfs")
    
    # Time the conversion process
    start_time = time.time()
    stats = converter.convert_directory("eml_files")
    end_time = time.time()
    
    duration = end_time - start_time
    
    print(f"Performance metrics:")
    print(f"  Total time: {duration:.2f} seconds")
    print(f"  Files processed: {stats['total']}")
    print(f"  Average time per file: {duration/stats['total']:.2f} seconds")
    print(f"  Files per minute: {(stats['total'] / duration) * 60:.1f}")


def main():
    """Run all advanced examples."""
    print("EML to PDF Converter - Advanced Usage Examples")
    print("=" * 50)
    
    # Run examples
    batch_processing_with_error_handling()
    selective_conversion()
    custom_merging_strategy()
    file_management()
    performance_monitoring()
    
    print("\n✅ All advanced examples completed!")


if __name__ == "__main__":
    main()
