"""
EML to PDF Converter

Converts EML email files to PDF format with HTML rendering support.
"""

import os
import email
import re
import logging
from pathlib import Path
from typing import Optional, Dict, Any
from email.header import decode_header

try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except ImportError:
    raise ImportError("weasyprint is required. Install with: pip install weasyprint")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EMLToPDFConverter:
    """
    A professional EML to PDF converter with HTML rendering support.

    This class handles the conversion of EML email files to PDF format,
    preserving HTML formatting and providing a clean, modern appearance.
    """

    def __init__(self, output_dir: str = "pdf_output"):
        """
        Initialize the EML to PDF converter.

        Args:
            output_dir (str): Directory to save converted PDF files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def decode_mime_header(self, header_value: Optional[str]) -> str:
        """
        Decode MIME header values that might be encoded.

        Args:
            header_value: The header value to decode

        Returns:
            Decoded header value as string
        """
        if header_value is None:
            return ""

        decoded_parts = decode_header(header_value)
        decoded_string = ""

        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                if encoding:
                    try:
                        decoded_string += part.decode(encoding)
                    except (UnicodeDecodeError, LookupError):
                        decoded_string += part.decode("utf-8", errors="ignore")
                else:
                    decoded_string += part.decode("utf-8", errors="ignore")
            else:
                decoded_string += str(part)

        return decoded_string

    def clean_html_for_pdf(self, html_content: str) -> str:
        """
        Clean HTML content to make it PDF-safe.

        Args:
            html_content: Raw HTML content

        Returns:
            Cleaned HTML content
        """
        # Remove problematic elements that might cause issues
        html_content = re.sub(
            r'<img[^>]*style="[^"]*display:\s*none[^"]*"[^>]*>',
            "",
            html_content,
            flags=re.IGNORECASE,
        )
        html_content = re.sub(
            r'<img[^>]*height="1"[^>]*>', "", html_content, flags=re.IGNORECASE
        )
        html_content = re.sub(
            r'<img[^>]*width="1"[^>]*>', "", html_content, flags=re.IGNORECASE
        )

        return html_content

    def extract_email_content(self, eml_file_path: str) -> Optional[Dict[str, Any]]:
        """
        Extract content from an EML file.

        Args:
            eml_file_path: Path to the EML file

        Returns:
            Dictionary containing email data or None if extraction failed
        """
        try:
            with open(eml_file_path, "rb") as f:
                msg = email.message_from_bytes(f.read())

            # Extract headers
            subject = self.decode_mime_header(msg.get("Subject", "No Subject"))
            from_addr = self.decode_mime_header(msg.get("From", "Unknown Sender"))
            to_addr = self.decode_mime_header(msg.get("To", "Unknown Recipient"))
            date = msg.get("Date", "Unknown Date")

            # Extract body content - prioritize HTML over plain text
            html_body = ""
            plain_body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/html":
                        payload = part.get_payload(decode=True)
                        if payload:
                            try:
                                if isinstance(payload, bytes):
                                    html_body = payload.decode("utf-8", errors="ignore")
                                else:
                                    html_body = str(payload)
                            except:
                                html_body = str(payload)
                    elif content_type == "text/plain":
                        payload = part.get_payload(decode=True)
                        if payload:
                            try:
                                if isinstance(payload, bytes):
                                    plain_body = payload.decode(
                                        "utf-8", errors="ignore"
                                    )
                                else:
                                    plain_body = str(payload)
                            except:
                                plain_body = str(payload)
            else:
                payload = msg.get_payload(decode=True)
                if payload:
                    try:
                        if isinstance(payload, bytes):
                            content = payload.decode("utf-8", errors="ignore")
                        else:
                            content = str(payload)
                        if msg.get_content_type() == "text/html":
                            html_body = content
                        else:
                            plain_body = content
                    except:
                        content = str(payload)
                        if msg.get_content_type() == "text/html":
                            html_body = content
                        else:
                            plain_body = content

            # Use HTML if available, otherwise convert plain text to HTML
            if html_body:
                body = self.clean_html_for_pdf(html_body)
            else:
                # Convert plain text to HTML
                body = plain_body.replace("\n", "<br>")
                body = f'<div style="font-family: Arial, sans-serif; line-height: 1.6;">{body}</div>'

            return {
                "subject": subject,
                "from": from_addr,
                "to": to_addr,
                "date": date,
                "body": body,
            }

        except Exception as e:
            logger.error(f"Error processing {eml_file_path}: {str(e)}")
            return None

    def create_html_template(self, email_data: Dict[str, Any]) -> str:
        """
        Create HTML template with modern email styling.

        Args:
            email_data: Dictionary containing email data

        Returns:
            Complete HTML document as string
        """
        body_html = email_data["body"]

        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{email_data['subject']}</title>
            <style>
                @page {{
                    margin: 0.5in;
                    size: A4;
                }}
                
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    font-size: 14px;
                    line-height: 1.6;
                    color: #202124;
                    background-color: #ffffff;
                    margin: 0;
                    padding: 20px;
                }}
                
                .email-container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background: #ffffff;
                    border: 1px solid #dadce0;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 1px 3px rgba(60,64,67,0.3);
                }}
                
                .email-header {{
                    background: #f8f9fa;
                    border-bottom: 1px solid #dadce0;
                    padding: 16px 20px;
                }}
                
                .email-subject {{
                    font-size: 18px;
                    font-weight: 600;
                    color: #202124;
                    margin: 0 0 8px 0;
                    word-wrap: break-word;
                }}
                
                .email-meta {{
                    font-size: 13px;
                    color: #5f6368;
                    margin: 0;
                }}
                
                .email-meta div {{
                    margin: 2px 0;
                }}
                
                .email-meta strong {{
                    color: #202124;
                    font-weight: 500;
                }}
                
                .email-body {{
                    padding: 20px;
                    background: #ffffff;
                }}
                
                .email-body * {{
                    max-width: 100%;
                    word-wrap: break-word;
                }}
                
                .email-body p {{
                    margin: 0 0 16px 0;
                    line-height: 1.6;
                }}
                
                .email-body p:last-child {{
                    margin-bottom: 0;
                }}
                
                .email-body a {{
                    color: #1a73e8;
                    text-decoration: none;
                }}
                
                .email-body a:hover {{
                    text-decoration: underline;
                }}
                
                .email-body ul, .email-body ol {{
                    margin: 16px 0;
                    padding-left: 24px;
                }}
                
                .email-body li {{
                    margin: 4px 0;
                }}
                
                .email-body blockquote {{
                    margin: 16px 0;
                    padding-left: 16px;
                    border-left: 3px solid #dadce0;
                    color: #5f6368;
                }}
                
                .email-body table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 16px 0;
                }}
                
                .email-body th, .email-body td {{
                    border: 1px solid #dadce0;
                    padding: 8px 12px;
                    text-align: left;
                }}
                
                .email-body th {{
                    background-color: #f8f9fa;
                    font-weight: 600;
                }}
                
                .email-body img {{
                    max-width: 100%;
                    height: auto;
                    display: block;
                    margin: 16px 0;
                }}
                
                .email-body hr {{
                    border: none;
                    border-top: 1px solid #dadce0;
                    margin: 24px 0;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="email-header">
                    <div class="email-subject">{email_data['subject']}</div>
                    <div class="email-meta">
                        <div><strong>From:</strong> {email_data['from']}</div>
                        <div><strong>To:</strong> {email_data['to']}</div>
                        <div><strong>Date:</strong> {email_data['date']}</div>
                    </div>
                </div>
                <div class="email-body">
                    {body_html}
                </div>
            </div>
        </body>
        </html>
        """

        return html_template

    def convert_single_file(self, eml_file_path: str) -> bool:
        """
        Convert a single EML file to PDF.

        Args:
            eml_file_path: Path to the EML file

        Returns:
            True if conversion successful, False otherwise
        """
        try:
            # Extract email content
            email_data = self.extract_email_content(eml_file_path)
            if not email_data:
                return False

            # Create output filename
            eml_filename = Path(eml_file_path).stem
            pdf_filename = f"{eml_filename}.pdf"
            pdf_path = self.output_dir / pdf_filename

            # Create HTML template
            html_content = self.create_html_template(email_data)

            # Convert HTML to PDF using WeasyPrint
            font_config = FontConfiguration()
            HTML(string=html_content).write_pdf(
                str(pdf_path),
                font_config=font_config,
                stylesheets=[
                    CSS(
                        string="""
                    @page {
                        margin: 0.5in;
                    }
                """
                    )
                ],
            )

            logger.info(f"✓ Converted: {eml_filename}.eml -> {pdf_filename}")
            return True

        except Exception as e:
            logger.error(f"✗ Error converting {eml_file_path}: {str(e)}")
            return False

    def convert_directory(self, input_dir: str) -> Dict[str, int]:
        """
        Convert all EML files in a directory.

        Args:
            input_dir: Directory containing EML files

        Returns:
            Dictionary with conversion statistics
        """
        input_path = Path(input_dir)
        if not input_path.exists():
            raise FileNotFoundError(f"Directory {input_dir} does not exist")

        # Find all EML files
        eml_files = list(input_path.glob("*.eml"))

        if not eml_files:
            logger.warning(f"No EML files found in {input_dir}")
            return {"total": 0, "successful": 0, "failed": 0}

        logger.info(f"Found {len(eml_files)} EML files to convert...")
        logger.info(f"Output directory: {self.output_dir}")

        successful = 0
        failed = 0

        for eml_file in eml_files:
            if self.convert_single_file(str(eml_file)):
                successful += 1
            else:
                failed += 1

        stats = {"total": len(eml_files), "successful": successful, "failed": failed}

        logger.info(
            f"Conversion complete! {successful}/{len(eml_files)} files converted successfully."
        )
        return stats
