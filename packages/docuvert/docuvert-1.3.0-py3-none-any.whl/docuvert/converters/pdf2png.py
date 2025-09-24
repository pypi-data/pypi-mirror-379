"""
PDF to PNG converter with high-quality rendering.
"""

import sys
import os
from io import BytesIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from core.exceptions import ConversionError, DependencyError

try:
    import fitz  # PyMuPDF
except ImportError as e:
    raise DependencyError(
        "PyMuPDF is required for PDF to image conversion",
        missing_dependency="pymupdf"
    ) from e

try:
    from PIL import Image
except ImportError as e:
    raise DependencyError(
        "Pillow is required for image processing",
        missing_dependency="pillow"
    ) from e


class Pdf2PngConverter:
    """Convert PDF to PNG format (first page by default)."""

    def parse_pdf2ast(self, input_path: str):
        """Parse PDF to AST representation (placeholder)."""
        return None

    def ast2png(self, ast_root, output_path: str):
        """Convert AST to PNG (placeholder)."""
        pass

    def convert(self, input_path: str, output_path: str, page_number: int = 0) -> None:
        """Convert PDF to PNG image.

        Args:
            input_path: Path to input PDF file
            output_path: Path to output PNG file
            page_number: Page number to convert (0-indexed, default is first page)
        """

        if not os.path.exists(input_path):
            raise ConversionError(f"Input file not found: {input_path}")

        if not output_path.lower().endswith(".png"):
            output_path += ".png"

        try:
            # Open PDF document
            pdf_document = fitz.open(input_path)

            # Check if page number is valid
            if page_number >= len(pdf_document):
                raise ConversionError(
                    f"Page {page_number} does not exist in PDF (total pages: {len(pdf_document)})",
                    source_format="pdf",
                    target_format="png"
                )

            # Get the page
            page = pdf_document[page_number]

            # Render page to image with high DPI for quality
            mat = fitz.Matrix(3.0, 3.0)  # 3x zoom for 216 DPI (72 * 3)
            pix = page.get_pixmap(matrix=mat)

            # Convert to PIL Image for better processing
            img_data = pix.tobytes("png")
            img = Image.open(BytesIO(img_data))

            # Save as PNG with optimization
            img.save(output_path, "PNG", optimize=True)

            # Clean up
            pdf_document.close()

            print(f"Successfully converted PDF page {page_number} to '{output_path}'")

        except Exception as e:
            if isinstance(e, ConversionError):
                raise
            raise ConversionError(
                f"PDF to PNG conversion failed: {e}",
                source_format="pdf",
                target_format="png",
                suggestions=[
                    "Ensure PDF is not corrupted or password-protected",
                    "Check if page number exists in the PDF"
                ]
            )