"""
PDF optimization and compression tool for reducing file size and improving performance.
Based on Context7 example code patterns for PyPDF optimization operations.
"""

import asyncio
from pathlib import Path
from typing import Optional, Dict, Any, Union, List
import json

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    PdfReader = None
    PdfWriter = None

from ..utils.file_handler import FileHandler


class PDFOptimizer:
    """
    PDF optimization tool supporting:
    - Image quality compression
    - Image removal
    - Content stream compression
    - File size reduction
    - Performance optimization
    
    Based on Context7 PyPDF compression best practices.
    """
    
    def __init__(self):
        """Initialize the PDF optimizer."""
        self.file_handler = FileHandler()
        
        # Optimization levels
        self.optimization_levels = {
            'light': {
                'image_quality': 90,
                'compress_streams': True,
                'remove_images': False,
                'description': 'Light compression with minimal quality loss'
            },
            'medium': {
                'image_quality': 75,
                'compress_streams': True,
                'remove_images': False,
                'description': 'Balanced compression with moderate quality loss'
            },
            'heavy': {
                'image_quality': 50,
                'compress_streams': True,
                'remove_images': False,
                'description': 'Heavy compression with noticeable quality loss'
            },
            'maximum': {
                'image_quality': 30,
                'compress_streams': True,
                'remove_images': True,
                'description': 'Maximum compression, images removed'
            }
        }
    
    async def optimize_pdf(
        self,
        file_path: Union[str, Path],
        output_file: Optional[str] = None,
        optimization_level: str = 'medium',
        custom_options: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Optimize PDF file using various compression techniques.
        
        Based on Context7 examples: image quality reduction, content compression, image removal.
        
        Args:
            file_path: Path to source PDF file
            output_file: Output PDF file path (default: overwrite source with '_optimized' suffix)
            optimization_level: Preset optimization level ('light', 'medium', 'heavy', 'maximum')
            custom_options: Custom optimization settings override
            
        Returns:
            JSON string with optimization results and statistics
        """
        
        if not PdfWriter:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Get original file size
            original_size = pdf_path.stat().st_size
            
            # Determine output path
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = pdf_path.parent / f"{pdf_path.stem}_optimized{pdf_path.suffix}"
            
            # Get optimization settings
            if optimization_level not in self.optimization_levels:
                return self._error_response(f"Invalid optimization level. Choose from: {list(self.optimization_levels.keys())}")
            
            settings = self.optimization_levels[optimization_level].copy()
            if custom_options:
                settings.update(custom_options)
            
            # Context7 pattern: Create writer from existing PDF
            writer = PdfWriter(clone_from=str(pdf_path))
            
            optimization_actions = []
            images_processed = 0
            pages_compressed = 0
            
            # Context7 pattern: Remove images if requested
            if settings.get('remove_images', False):
                try:
                    writer.remove_images()
                    optimization_actions.append('All images removed')
                except Exception as e:
                    optimization_actions.append(f'Image removal failed: {str(e)}')
            else:
                # Context7 pattern: Compress image quality
                image_quality = settings.get('image_quality', 80)
                if image_quality < 100:
                    try:
                        for page in writer.pages:
                            for img in page.images:
                                img.replace(img.image, quality=image_quality)
                                images_processed += 1
                        optimization_actions.append(f'Image quality reduced to {image_quality}% ({images_processed} images)')
                    except Exception as e:
                        optimization_actions.append(f'Image compression failed: {str(e)}')
            
            # Context7 pattern: Apply content stream compression
            if settings.get('compress_streams', True):
                try:
                    for page in writer.pages:
                        page.compress_content_streams()  # CPU intensive operation
                        pages_compressed += 1
                    optimization_actions.append(f'Content streams compressed ({pages_compressed} pages)')
                except Exception as e:
                    optimization_actions.append(f'Content compression failed: {str(e)}')
            
            # Save the optimized PDF
            with open(str(output_path), "wb") as f:
                writer.write(f)
            
            # Calculate compression statistics
            optimized_size = output_path.stat().st_size
            size_reduction = original_size - optimized_size
            compression_ratio = (size_reduction / original_size * 100) if original_size > 0 else 0
            
            result = {
                'success': True,
                'operation': 'optimize_pdf',
                'source_pdf': str(pdf_path),
                'output_pdf': str(output_path),
                'optimization_level': optimization_level,
                'settings_used': settings,
                'statistics': {
                    'original_size': original_size,
                    'optimized_size': optimized_size,
                    'size_reduction': size_reduction,
                    'compression_ratio': round(compression_ratio, 2),
                    'images_processed': images_processed,
                    'pages_compressed': pages_compressed
                },
                'optimization_actions': optimization_actions,
                'file_info': {
                    'original_size_mb': round(original_size / 1024 / 1024, 2),
                    'optimized_size_mb': round(optimized_size / 1024 / 1024, 2),
                    'space_saved_mb': round(size_reduction / 1024 / 1024, 2)
                }
            }
            
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error during PDF optimization: {str(e)}")
    
    async def compress_pdf_images(
        self,
        file_path: Union[str, Path],
        output_file: Optional[str] = None,
        quality: int = 80
    ) -> str:
        """
        Compress images in PDF while preserving document structure.
        
        Based on Context7 example: img.replace(img.image, quality=80).
        
        Args:
            file_path: Path to source PDF file
            output_file: Output PDF file path (default: auto-generated)
            quality: Image compression quality (1-100, where 100=best quality)
            
        Returns:
            JSON string with compression results
        """
        
        if not PdfWriter:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        if not (1 <= quality <= 100):
            return self._error_response("Quality must be between 1 and 100")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Get original file size
            original_size = pdf_path.stat().st_size
            
            # Determine output path
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = pdf_path.parent / f"{pdf_path.stem}_compressed{pdf_path.suffix}"
            
            # Context7 pattern: Compress images
            writer = PdfWriter(clone_from=str(pdf_path))
            
            images_compressed = 0
            for page in writer.pages:
                for img in page.images:
                    img.replace(img.image, quality=quality)
                    images_compressed += 1
            
            # Save the compressed PDF
            with open(str(output_path), "wb") as f:
                writer.write(f)
            
            # Calculate statistics
            compressed_size = output_path.stat().st_size
            size_reduction = original_size - compressed_size
            compression_ratio = (size_reduction / original_size * 100) if original_size > 0 else 0
            
            result = {
                'success': True,
                'operation': 'compress_pdf_images',
                'source_pdf': str(pdf_path),
                'output_pdf': str(output_path),
                'compression_settings': {
                    'image_quality': quality
                },
                'statistics': {
                    'original_size': original_size,
                    'compressed_size': compressed_size,
                    'size_reduction': size_reduction,
                    'compression_ratio': round(compression_ratio, 2),
                    'images_compressed': images_compressed
                },
                'file_info': {
                    'original_size_mb': round(original_size / 1024 / 1024, 2),
                    'compressed_size_mb': round(compressed_size / 1024 / 1024, 2),
                    'space_saved_mb': round(size_reduction / 1024 / 1024, 2)
                }
            }
            
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error compressing PDF images: {str(e)}")
    
    async def remove_pdf_content(
        self,
        file_path: Union[str, Path],
        output_file: Optional[str] = None,
        remove_images: bool = False,
        remove_annotations: bool = False,
        compress_streams: bool = True
    ) -> str:
        """
        Remove specific content from PDF to reduce file size.
        
        Based on Context7 examples: writer.remove_images() and content compression.
        
        Args:
            file_path: Path to source PDF file
            output_file: Output PDF file path (default: auto-generated)
            remove_images: Whether to remove all images
            remove_annotations: Whether to remove annotations
            compress_streams: Whether to compress content streams
            
        Returns:
            JSON string with removal results
        """
        
        if not PdfWriter:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Get original file size
            original_size = pdf_path.stat().st_size
            
            # Determine output path
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = pdf_path.parent / f"{pdf_path.stem}_cleaned{pdf_path.suffix}"
            
            # Context7 pattern: Create writer and apply removals
            writer = PdfWriter(clone_from=str(pdf_path))
            
            removal_actions = []
            
            # Context7 pattern: Remove images
            if remove_images:
                try:
                    writer.remove_images()
                    removal_actions.append('All images removed')
                except Exception as e:
                    removal_actions.append(f'Image removal failed: {str(e)}')
            
            # Remove annotations (if implemented in future versions)
            if remove_annotations:
                try:
                    # Note: This functionality may need to be implemented manually
                    # as it's not directly available in current pypdf versions
                    pages_cleaned = 0
                    for page in writer.pages:
                        if "/Annots" in page:
                            del page["/Annots"]
                            pages_cleaned += 1
                    removal_actions.append(f'Annotations removed from {pages_cleaned} pages')
                except Exception as e:
                    removal_actions.append(f'Annotation removal failed: {str(e)}')
            
            # Context7 pattern: Compress content streams
            if compress_streams:
                try:
                    pages_compressed = 0
                    for page in writer.pages:
                        page.compress_content_streams()
                        pages_compressed += 1
                    removal_actions.append(f'Content streams compressed ({pages_compressed} pages)')
                except Exception as e:
                    removal_actions.append(f'Content compression failed: {str(e)}')
            
            # Save the cleaned PDF
            with open(str(output_path), "wb") as f:
                writer.write(f)
            
            # Calculate statistics
            cleaned_size = output_path.stat().st_size
            size_reduction = original_size - cleaned_size
            compression_ratio = (size_reduction / original_size * 100) if original_size > 0 else 0
            
            result = {
                'success': True,
                'operation': 'remove_pdf_content',
                'source_pdf': str(pdf_path),
                'output_pdf': str(output_path),
                'removal_settings': {
                    'remove_images': remove_images,
                    'remove_annotations': remove_annotations,
                    'compress_streams': compress_streams
                },
                'statistics': {
                    'original_size': original_size,
                    'cleaned_size': cleaned_size,
                    'size_reduction': size_reduction,
                    'compression_ratio': round(compression_ratio, 2)
                },
                'removal_actions': removal_actions,
                'file_info': {
                    'original_size_mb': round(original_size / 1024 / 1024, 2),
                    'cleaned_size_mb': round(cleaned_size / 1024 / 1024, 2),
                    'space_saved_mb': round(size_reduction / 1024 / 1024, 2)
                }
            }
            
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error removing PDF content: {str(e)}")
    
    async def analyze_pdf_size(
        self,
        file_path: Union[str, Path]
    ) -> str:
        """
        Analyze PDF file to identify optimization opportunities.
        
        Args:
            file_path: Path to PDF file to analyze
            
        Returns:
            JSON string with size analysis and optimization recommendations
        """
        
        if not PdfReader:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Basic file information
            file_size = pdf_path.stat().st_size
            
            # Analyze PDF content
            reader = PdfReader(str(pdf_path))
            total_pages = len(reader.pages)
            
            # Count images and estimate their contribution to file size
            total_images = 0
            estimated_image_size = 0
            
            for page in reader.pages:
                if hasattr(page, 'images'):
                    page_images = len(page.images)
                    total_images += page_images
                    # Rough estimate: each image contributes ~50KB on average
                    estimated_image_size += page_images * 50 * 1024
            
            # Calculate potential optimization
            image_size_ratio = (estimated_image_size / file_size * 100) if file_size > 0 else 0
            
            # Generate recommendations
            recommendations = []
            potential_savings = []
            
            if image_size_ratio > 30:
                recommendations.append("High image content detected - consider image compression")
                potential_savings.append({"method": "image_compression", "estimated_savings": "30-60%"})
            
            if file_size > 10 * 1024 * 1024:  # 10MB
                recommendations.append("Large file size - consider content stream compression")
                potential_savings.append({"method": "content_compression", "estimated_savings": "10-25%"})
            
            if total_images > 20:
                recommendations.append("Many images present - consider removing non-essential images")
                potential_savings.append({"method": "image_removal", "estimated_savings": "50-80%"})
            
            if not recommendations:
                recommendations.append("File appears to be well-optimized")
                potential_savings.append({"method": "light_compression", "estimated_savings": "5-15%"})
            
            result = {
                'success': True,
                'operation': 'analyze_pdf_size',
                'source_pdf': str(pdf_path),
                'file_analysis': {
                    'file_size': file_size,
                    'file_size_mb': round(file_size / 1024 / 1024, 2),
                    'total_pages': total_pages,
                    'total_images': total_images,
                    'estimated_image_size': estimated_image_size,
                    'image_size_ratio': round(image_size_ratio, 2),
                    'average_page_size': round(file_size / total_pages / 1024, 2) if total_pages > 0 else 0
                },
                'optimization_recommendations': recommendations,
                'potential_savings': potential_savings,
                'suggested_optimization_level': self._suggest_optimization_level(file_size, image_size_ratio, total_images)
            }
            
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error analyzing PDF: {str(e)}")
    
    def _suggest_optimization_level(self, file_size: int, image_ratio: float, image_count: int) -> str:
        """Suggest optimization level based on file analysis."""
        
        if image_ratio > 60 or image_count > 50:
            return 'heavy'  # Lots of images, aggressive optimization needed
        elif image_ratio > 30 or file_size > 20 * 1024 * 1024:  # 20MB
            return 'medium'  # Moderate optimization needed
        elif file_size > 5 * 1024 * 1024:  # 5MB
            return 'light'   # Light optimization sufficient
        else:
            return 'light'   # Small file, minimal optimization
    
    def _error_response(self, message: str) -> str:
        """Generate standardized error response."""
        return json.dumps({
            'success': False,
            'error': str(message),
            'operation': 'pdf_optimization'
        }, ensure_ascii=False, indent=2, default=str)
