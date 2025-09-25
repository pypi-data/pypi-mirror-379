"""
PDF and Image conversion tool with comprehensive image processing capabilities.

This module provides bidirectional conversion between PDF and images:
- Convert PDF pages to high-quality images (PNG, JPEG) with configurable DPI
- Convert multiple images to single PDF document with quality control
- Extract existing embedded images from PDF pages with size filtering
- Memory vs disk storage options for performance optimization
- Intelligent file naming and directory management
- Cross-platform compatibility with robust error handling

Based on Context7 example code patterns for pdf2image, Pillow, and PyPDF.
"""

import asyncio
import tempfile
import os
from pathlib import Path
from typing import List, Optional, Dict, Any, Union, Tuple
import json

try:
    # PDF to image conversion
    from pdf2image import convert_from_path, convert_from_bytes
    from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
    )
    # Image processing and PDF creation
    from PIL import Image
    # PDF image extraction
    from pypdf import PdfReader
except ImportError:
    convert_from_path = None
    convert_from_bytes = None
    Image = None
    PdfReader = None

from ..utils.file_handler import FileHandler
from ..utils.cache import PDFCache


class PDFImageConverter:
    """
    PDF and Image conversion tool supporting:
    - PDF pages to images (PNG, JPG, etc.)
    - Multiple images to single PDF
    - Extract images from PDF pages
    
    Based on Context7 best practice examples.
    """
    
    def __init__(self):
        """Initialize the PDF-Image converter with cache."""
        self.cache = PDFCache(max_entries=30, max_age_seconds=1800)  # 30 minutes
        self.file_handler = FileHandler()
        
        # Supported image formats for conversion
        self.supported_formats = ['PNG', 'JPEG', 'JPG', 'TIFF', 'BMP', 'WEBP']
        
        # Default settings based on Context7 examples
        self.default_dpi = 200
        self.default_format = 'PNG'
    
    async def pdf_to_images(
        self,
        file_path: Union[str, Path],
        pages: Optional[str] = None,
        dpi: int = 200,
        image_format: str = 'PNG',
        output_dir: Optional[str] = None,
        save_to_disk: bool = True
    ) -> str:
        """
        Convert PDF pages to images using pdf2image.
        
        Based on Context7 example: convert_from_path with output_folder optimization.
        
        Args:
            file_path: Path to PDF file
            pages: Page range string (e.g., "1,3,5-10,-1")
            dpi: Resolution for image conversion (default: 200)
            image_format: Output format ('PNG', 'JPEG', etc.)
            output_dir: Directory to save images (default: temp directory)
            save_to_disk: Whether to save images to disk or return in-memory
            
        Returns:
            JSON string with conversion results and file paths
        """
        
        if not convert_from_path:
            return self._error_response("pdf2image library not available. Install with: pip install pdf2image")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Generate cache key  
            cache_key = f"pdf_to_images_{pdf_path.name}_{pages}_{dpi}_{image_format}"
            cached_result = self.cache.get(cache_key, str(pdf_path))
            if cached_result:
                return cached_result
            
            # Parse page range
            page_numbers = None
            if pages:
                # Use temporary conversion to get total pages for range parsing
                try:
                    temp_images = convert_from_path(str(pdf_path), dpi=150, first_page=1, last_page=1)
                    total_pages = len(convert_from_path(str(pdf_path), dpi=150))
                    page_numbers = self.file_handler.parse_page_range(pages, total_pages)
                except Exception as e:
                    return self._error_response(f"Failed to parse page range: {str(e)}")
            
            # Simplified approach to avoid path issues
            try:
                # Convert PDF to images directly
                if page_numbers:
                    # Convert specific pages
                    images = []
                    for page_num in page_numbers:
                        page_images = convert_from_path(
                            str(pdf_path),  # Ensure string path
                            dpi=dpi,
                            first_page=page_num,
                            last_page=page_num,
                            fmt=image_format
                        )
                        images.extend(page_images)
                else:
                    # Convert all pages
                    images = convert_from_path(
                        str(pdf_path),  # Ensure string path
                        dpi=dpi,
                        fmt=image_format
                    )
            except Exception as conv_error:
                return self._error_response(f"PDF conversion failed: {str(conv_error)}")
            
            # Context7 pattern: Use temporary directory for file operations
            with tempfile.TemporaryDirectory() as temp_dir:
                output_path = Path(output_dir) if output_dir else Path(temp_dir)
                
                # Process results
                image_info = []
                final_output_path = Path(output_dir) if output_dir else Path.cwd() / "pdf_images"
                final_output_path.mkdir(exist_ok=True)
                
                for i, img in enumerate(images):
                    page_num = page_numbers[i] if page_numbers else i + 1
                    filename = f"{pdf_path.stem}_page_{page_num:03d}.{image_format.lower()}"
                    
                    if save_to_disk:
                        # Save to final location
                        final_path = final_output_path / filename
                        img.save(final_path, format=image_format)
                        
                        image_info.append({
                            'page': page_num,
                            'filename': filename,
                            'path': str(final_path),
                            'size': list(img.size),  # Convert tuple to list for JSON
                            'format': image_format,
                            'dpi': dpi
                        })
                    else:
                        # Keep in memory
                        image_info.append({
                            'page': page_num,
                            'size': list(img.size),  # Convert tuple to list for JSON
                            'format': image_format,
                            'dpi': dpi,
                            'in_memory': True
                        })
            
            result = {
                'success': True,
                'operation': 'pdf_to_images',
                'source_pdf': str(pdf_path),
                'total_images': len(images),
                'dpi': dpi,
                'format': image_format,
                'output_directory': str(final_output_path) if save_to_disk else None,
                'images': image_info,
                'processing_info': {
                    'pages_processed': len(images),
                    'page_range': pages if pages else 'all',
                    'memory_optimized': save_to_disk
                }
            }
            
            # Ensure all Path objects are converted to strings before JSON serialization
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            try:
                result_json = json.dumps(result, ensure_ascii=False, indent=2, default=str)
                self.cache.set(cache_key, result_json, str(pdf_path))
                return result_json
            except TypeError as e:
                return self._error_response(f"JSON serialization error: {str(e)}")
            
        except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
            return self._error_response(f"PDF conversion error: {str(e)}")
        except Exception as e:
            return self._error_response(f"Unexpected error during PDF to images conversion: {str(e)}")
    
    async def images_to_pdf(
        self,
        image_paths: List[str],
        output_file: str,
        page_size: str = "A4",
        quality: int = 95,
        title: Optional[str] = None,
        author: Optional[str] = None
    ) -> str:
        """
        Convert multiple images to a single PDF.
        
        Based on Context7 Pillow example: save with append_images parameter.
        
        Args:
            image_paths: List of image file paths
            output_file: Output PDF file path
            page_size: Page size ("A4", "Letter", "Legal", or "auto")
            quality: JPEG quality for compression (1-100)
            title: PDF document title
            author: PDF document author
            
        Returns:
            JSON string with conversion results
        """
        
        if not Image:
            return self._error_response("Pillow library not available. Install with: pip install pillow")
        
        try:
            if not image_paths:
                return self._error_response("No image paths provided")
            
            # Validate image files
            valid_images = []
            for img_path in image_paths:
                path = Path(img_path)
                if not path.exists():
                    continue
                if path.suffix.upper()[1:] in self.supported_formats:
                    valid_images.append(path)
            
            if not valid_images:
                return self._error_response("No valid image files found")
            
            # Context7 pattern: Open and prepare images
            processed_images = []
            image_info = []
            
            for img_path in valid_images:
                try:
                    img = Image.open(img_path)
                    
                    # Convert to RGB if needed (for PDF compatibility)
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Handle page sizing
                    if page_size != "auto":
                        img = self._resize_to_page_size(img, page_size)
                    
                    processed_images.append(img)
                    image_info.append({
                        'path': str(img_path),
                        'size': list(img.size),  # Convert tuple to list for JSON
                        'mode': img.mode,
                        'format': str(img.format) if img.format else 'unknown'
                    })
                    
                except Exception as e:
                    # Skip problematic images
                    continue
            
            if not processed_images:
                return self._error_response("No images could be processed")
            
            # Context7 Pillow pattern: Save first image with append_images
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Prepare save parameters based on Context7 examples
            save_params = {
                'format': 'PDF',
                'save_all': True,
                'quality': quality,
                'resolution': 200.0  # DPI
            }
            
            # Add additional images to append
            if len(processed_images) > 1:
                save_params['append_images'] = processed_images[1:]
            
            # Add metadata if provided
            if title:
                save_params['title'] = title
            if author:
                save_params['author'] = author
            
            # Execute conversion using Context7 pattern
            processed_images[0].save(str(output_path), **save_params)
            
            result = {
                'success': True,
                'operation': 'images_to_pdf',
                'output_pdf': str(output_path),
                'total_images': len(processed_images),
                'page_size': page_size,
                'quality': quality,
                'file_size': output_path.stat().st_size,
                'images_processed': image_info,
                'metadata': {
                    'title': title,
                    'author': author
                }
            }
            
            # Ensure all Path objects are converted to strings
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error converting images to PDF: {str(e)}")
    
    async def extract_pdf_images(
        self,
        file_path: Union[str, Path],
        pages: Optional[str] = None,
        min_size: Tuple[int, int] = (100, 100),
        output_dir: Optional[str] = None
    ) -> str:
        """
        Extract images from PDF pages.
        
        Based on Context7 PyPDF example: page.images iteration pattern.
        
        Args:
            file_path: Path to PDF file
            pages: Page range string (default: all pages)
            min_size: Minimum image size to extract (width, height)
            output_dir: Directory to save extracted images
            
        Returns:
            JSON string with extraction results
        """
        
        if not PdfReader:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Context7 pattern: Initialize PdfReader
            reader = PdfReader(str(pdf_path))
            total_pages = len(reader.pages)
            
            # Parse page range
            page_numbers = self.file_handler.parse_page_range(pages, total_pages) if pages else list(range(1, total_pages + 1))
            
            if not page_numbers:
                return self._error_response("No valid pages specified")
            
            # Setup output directory
            if output_dir:
                output_path = Path(output_dir)
            else:
                output_path = Path.cwd() / f"{pdf_path.stem}_extracted_images"
            output_path.mkdir(exist_ok=True, parents=True)
            
            # Context7 PyPDF pattern: Extract images from pages
            extracted_images = []
            total_extracted = 0
            
            for page_num in page_numbers:
                page = reader.pages[page_num - 1]  # 0-based indexing
                
                if hasattr(page, 'images'):
                    # Context7 pattern: Enumerate through page images
                    for count, image_file_object in enumerate(page.images):
                        try:
                            # Get image data
                            image_data = image_file_object.data
                            image_name = image_file_object.name
                            
                            # Create filename
                            filename = f"{pdf_path.stem}_page_{page_num:03d}_img_{count:03d}{image_name}"
                            output_file = output_path / filename
                            
                            # Save image using Context7 pattern
                            with open(output_file, "wb") as fp:
                                fp.write(image_data)
                            
                            # Check image size if PIL is available
                            try:
                                if Image:
                                    with Image.open(output_file) as img:
                                        if img.size[0] >= min_size[0] and img.size[1] >= min_size[1]:
                                            extracted_images.append({
                                                'page': page_num,
                                                'filename': filename,
                                                'path': str(output_file),
                                                'size': list(img.size),  # Convert tuple to list for JSON
                                                'format': str(img.format) if img.format else 'unknown',
                                                'mode': img.mode,
                                                'file_size': len(image_data)
                                            })
                                            total_extracted += 1
                                        else:
                                            # Remove small images
                                            output_file.unlink()
                                else:
                                    # No size checking without PIL
                                    extracted_images.append({
                                        'page': page_num,
                                        'filename': filename,
                                        'path': str(output_file),
                                        'file_size': len(image_data)
                                    })
                                    total_extracted += 1
                            except Exception:
                                # Keep image even if size check fails
                                extracted_images.append({
                                    'page': page_num,
                                    'filename': filename,
                                    'path': str(output_file),
                                    'file_size': len(image_data)
                                })
                                total_extracted += 1
                                
                        except Exception as e:
                            # Skip problematic images
                            continue
            
            result = {
                'success': True,
                'operation': 'extract_pdf_images',
                'source_pdf': str(pdf_path),
                'total_pages_processed': len(page_numbers),
                'total_images_extracted': total_extracted,
                'min_size_filter': list(min_size),  # Convert tuple to list for JSON
                'output_directory': str(output_path),
                'extracted_images': extracted_images,
                'processing_info': {
                    'pages_processed': page_numbers,
                    'page_range': pages if pages else 'all'
                }
            }
            
            # Ensure all Path objects are converted to strings
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error extracting images from PDF: {str(e)}")
    
    def _resize_to_page_size(self, img: Image.Image, page_size: str) -> Image.Image:
        """Resize image to fit standard page sizes."""
        
        # Standard page sizes in points (72 DPI)
        page_sizes = {
            'A4': (595, 842),
            'Letter': (612, 792), 
            'Legal': (612, 1008)
        }
        
        if page_size not in page_sizes:
            return img
        
        target_size = page_sizes[page_size]
        
        # Calculate scaling factor to fit within page
        scale_x = target_size[0] / img.width
        scale_y = target_size[1] / img.height
        scale = min(scale_x, scale_y)
        
        new_size = (int(img.width * scale), int(img.height * scale))
        
        return img.resize(new_size, Image.Resampling.LANCZOS)
    
    def _error_response(self, message: str) -> str:
        """Generate standardized error response."""
        import json
        return json.dumps({
            'success': False,
            'error': str(message),
            'operation': 'pdf_image_conversion'
        }, ensure_ascii=False, indent=2, default=str)
