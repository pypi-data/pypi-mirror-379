"""
PDF OCR tool using Tesseract for scanned documents and image-based PDFs.

This module provides advanced OCR capabilities for PDF documents:
- Tesseract OCR integration with multi-language support
- Optimized PDF to image conversion with configurable DPI
- Confidence scoring and quality assessment  
- Text chunking with overlap preservation
- Performance caching and error resilience
- Chinese language optimization (default: simplified Chinese)
"""

import asyncio
import json
import tempfile
from pathlib import Path
from typing import List, Optional, Dict, Any, Union, TypedDict

try:
    import pytesseract
    from PIL import Image
    import pdf2image
    from pdf2image.exceptions import PDFInfoNotInstalledError
except ImportError:
    pytesseract = None
    Image = None
    pdf2image = None
    PDFInfoNotInstalledError = None

from ..utils.file_handler import FileHandler
from ..utils.chunker import TextChunker, TextChunk
from ..utils.cache import PDFCache


class OCRResult(TypedDict):
    """Type definition for OCR processing results."""
    success: bool
    text: str
    confidence: float
    language: str
    page_number: int
    metadata: Dict[str, Any]


class PDFOCRTool:
    """
    PDF OCR tool using Tesseract for text extraction from scanned documents
    and image-based PDFs with Chinese language support.
    """
    
    def __init__(self):
        """Initialize the PDF OCR tool with cache."""
        self.cache = PDFCache(max_entries=20, max_age_seconds=3600)  # 1 hour
        self.file_handler = FileHandler()
        
        # Supported languages (default Chinese)
        self.supported_languages = {
            'chi_sim': '简体中文',
            'chi_tra': '繁体中文', 
            'eng': 'English',
            'chi_sim+eng': '中英混合'
        }
        
        # Default configuration for better Chinese OCR
        self.default_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ，。、；：？！""''（）【】《》·—…'
    
    async def perform_ocr(
        self,
        file_path: Union[str, Path],
        pages: Optional[str] = None,
        language: str = 'chi_sim',
        chunk_size: int = 1000,
        chunk_overlap: int = 100,
        dpi: int = 200
    ) -> str:
        """
        Perform OCR on PDF pages using Tesseract.
        
        Args:
            file_path: Path to PDF file
            pages: Page range string (e.g., "1,3,5-10,-1")
            language: OCR language code (default: 'chi_sim' for simplified Chinese)
            chunk_size: Maximum size of text chunks
            chunk_overlap: Overlap between chunks
            dpi: DPI for PDF to image conversion
            
        Returns:
            JSON string with OCR results and metadata
        """
        # Check dependencies
        if not self._check_dependencies():
            return self._error_response("Missing dependencies. Please install: pip install pytesseract pillow pdf2image")
        
        try:
            # Validate file path
            pdf_path = self.file_handler.validate_pdf_path(file_path)
            
            # Validate language
            if language not in self.supported_languages:
                language = 'chi_sim'  # Default to Chinese
            
            # Check cache
            cache_key_params = {
                'pages': pages,
                'language': language,
                'chunk_size': chunk_size,
                'chunk_overlap': chunk_overlap,
                'dpi': dpi
            }
            cached_result = self.cache.get(str(pdf_path), 'ocr', **cache_key_params)
            if cached_result:
                return cached_result
            
            # Perform OCR
            result = await self._ocr_pdf_pages(
                pdf_path, pages, language, chunk_size, chunk_overlap, dpi
            )
            
            # Cache the result
            self.cache.set(str(pdf_path), 'ocr', result, **cache_key_params)
            
            return result
            
        except Exception as e:
            return self._error_response(f"OCR processing failed: {str(e)}")
    
    async def _ocr_pdf_pages(
        self,
        pdf_path: Path,
        pages_str: Optional[str],
        language: str,
        chunk_size: int,
        chunk_overlap: int,
        dpi: int
    ) -> str:
        """Perform OCR on PDF pages."""
        
        try:
            # Convert PDF to images
            pages_images = pdf2image.convert_from_path(
                pdf_path,
                dpi=dpi,
                fmt='PNG',
                thread_count=2
            )
            
            total_pages = len(pages_images)
            page_numbers = self.file_handler.parse_page_range(pages_str, total_pages)
            
            if not page_numbers:
                return self._error_response("No valid pages specified")
            
            # Perform OCR on specified pages
            pages_content = []
            
            for page_num in page_numbers:
                if page_num >= total_pages:
                    continue
                    
                page_image = pages_images[page_num]
                
                # Perform OCR on the image
                try:
                    # Use custom config for better Chinese recognition
                    ocr_config = r'--oem 3 --psm 6'
                    
                    text = pytesseract.image_to_string(
                        page_image,
                        lang=language,
                        config=ocr_config
                    )
                    
                    # Get confidence data for quality assessment
                    data = pytesseract.image_to_data(
                        page_image,
                        lang=language,
                        config=ocr_config,
                        output_type=pytesseract.Output.DICT
                    )
                    
                    # Calculate average confidence
                    confidences = [int(conf) for conf in data['conf'] if int(conf) > 0]
                    avg_confidence = sum(confidences) / len(confidences) if confidences else 0
                    
                    page_data = {
                        'text': text.strip(),
                        'page_number': page_num + 1,  # Convert to 1-indexed
                        'metadata': {
                            'ocr_confidence': avg_confidence / 100.0,  # Normalize to 0-1
                            'word_count': len(text.split()),
                            'char_count': len(text),
                            'language': language,
                            'dpi': dpi
                        }
                    }
                    
                    pages_content.append(page_data)
                    
                except Exception as e:
                    # If OCR fails for this page, add empty content
                    page_data = {
                        'text': '',
                        'page_number': page_num + 1,
                        'metadata': {
                            'ocr_confidence': 0.0,
                            'word_count': 0,
                            'char_count': 0,
                            'language': language,
                            'error': f"OCR failed: {str(e)}"
                        }
                    }
                    pages_content.append(page_data)
            
            # Chunk the text
            chunker = TextChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = chunker.chunk_pages(pages_content)
            
            # Prepare result
            result = {
                'success': True,
                'file_path': str(pdf_path),
                'total_pages': total_pages,
                'processed_pages': [p + 1 for p in page_numbers],  # Convert to 1-indexed
                'chunks': [
                    {
                        'content': chunk.content,
                        'page_number': chunk.page_number,
                        'chunk_index': chunk.chunk_index,
                        'metadata': chunk.metadata
                    }
                    for chunk in chunks
                ],
                'summary': chunker.get_chunks_summary(chunks),
                'extraction_method': 'tesseract_ocr',
                'ocr_language': language,
                'ocr_language_name': self.supported_languages.get(language, language)
            }
            
            return self._format_result(result)
            
        except Exception as e:
            return self._error_response(f"OCR processing failed: {str(e)}")
    
    def _check_dependencies(self) -> bool:
        """Check if required dependencies are available."""
        return all([pytesseract, Image, pdf2image])
    
    def get_available_languages(self) -> List[str]:
        """Get list of available OCR languages."""
        if not self._check_dependencies():
            return []
        
        try:
            available = pytesseract.get_languages(config='')
            # Filter to supported languages
            return [lang for lang in available if lang in self.supported_languages]
        except Exception:
            return list(self.supported_languages.keys())
    
    def _format_result(self, result: Dict[str, Any]) -> str:
        """Format result as JSON string."""
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    def _error_response(self, message: str) -> str:
        """
        Format standardized error response for OCR operations.
        
        Args:
            message: Error message to include in response
            
        Returns:
            JSON string with error information and OCR extraction method
        """
        return json.dumps({
            'success': False,
            'error': str(message),
            'extraction_method': 'tesseract_ocr'
        }, ensure_ascii=False, indent=2)
