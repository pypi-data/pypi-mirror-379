"""
PDF metadata management tool for reading and writing PDF document metadata.

This module provides comprehensive metadata management capabilities:
- Read standard PDF metadata fields (title, author, subject, creator, producer)
- Read advanced XMP metadata when available for detailed document information
- Write and update metadata fields with selective preservation options
- Remove specific metadata fields or completely clear all metadata
- Intelligent field validation and type conversion
- Backward compatibility with various PDF metadata formats

Based on Context7 example code patterns for PyPDF metadata operations.
"""

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, Union
import json

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import create_string_object, ByteStringObject, NameObject, NumberObject
except ImportError:
    PdfReader = None
    PdfWriter = None

from ..utils.file_handler import FileHandler
from ..utils.cache import PDFCache


class PDFMetadataManager:
    """
    PDF metadata management tool supporting:
    - Read standard metadata (title, author, subject, dates, etc.)
    - Write/update metadata fields
    - Remove metadata
    - Handle XMP metadata (advanced)
    
    Based on Context7 PyPDF best practice examples.
    """
    
    def __init__(self):
        """Initialize the PDF metadata manager with cache."""
        self.cache = PDFCache(max_entries=20, max_age_seconds=1800)  # 30 minutes
        self.file_handler = FileHandler()
        
        # Standard metadata fields based on Context7 examples
        self.standard_fields = {
            'title': '/Title',
            'author': '/Author', 
            'subject': '/Subject',
            'creator': '/Creator',
            'producer': '/Producer',
            'creation_date': '/CreationDate',
            'modification_date': '/ModDate',
            'keywords': '/Keywords'
        }
        
        # XMP metadata fields for advanced metadata
        self.xmp_fields = [
            'dc_title', 'dc_description', 'dc_creator', 'dc_subject',
            'xmp_create_date', 'xmp_modify_date', 'xmp_creator_tool'
        ]
    
    async def get_pdf_metadata(
        self,
        file_path: Union[str, Path],
        include_xmp: bool = False
    ) -> str:
        """
        Read PDF metadata including standard and optionally XMP fields.
        
        Based on Context7 example: reader.metadata and reader.xmp_metadata.
        
        Args:
            file_path: Path to PDF file
            include_xmp: Whether to include XMP metadata (default: False)
            
        Returns:
            JSON string with metadata information
        """
        
        if not PdfReader:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Generate cache key
            cache_key = f"pdf_metadata_{pdf_path.name}_{include_xmp}"
            cached_result = self.cache.get(cache_key, str(pdf_path))
            if cached_result:
                return cached_result
            
            # Context7 pattern: Read PDF metadata
            reader = PdfReader(str(pdf_path))
            
            # Standard metadata extraction based on Context7 example
            standard_metadata = {}
            if reader.metadata:
                meta = reader.metadata
                
                # Context7 pattern: All fields could be None, handle gracefully
                standard_metadata = {
                    'title': str(meta.title) if meta.title else None,
                    'author': str(meta.author) if meta.author else None,
                    'subject': str(meta.subject) if meta.subject else None,
                    'creator': str(meta.creator) if meta.creator else None,
                    'producer': str(meta.producer) if meta.producer else None,
                    'creation_date': str(meta.creation_date) if meta.creation_date else None,
                    'modification_date': str(meta.modification_date) if meta.modification_date else None,
                }
                
                # Handle additional fields that might exist
                raw_metadata = {}
                for key, value in meta.items():
                    if isinstance(key, str) and key.startswith('/'):
                        field_name = key.lower().replace('/', '')
                        raw_metadata[field_name] = str(value) if value else None
                
                standard_metadata['raw_fields'] = raw_metadata
            
            # XMP metadata extraction based on Context7 example
            xmp_metadata = {}
            if include_xmp and reader.xmp_metadata:
                try:
                    xmp_meta = reader.xmp_metadata
                    xmp_metadata = {
                        'dc_title': str(xmp_meta.dc_title) if hasattr(xmp_meta, 'dc_title') and xmp_meta.dc_title else None,
                        'dc_description': str(xmp_meta.dc_description) if hasattr(xmp_meta, 'dc_description') and xmp_meta.dc_description else None,
                        'dc_creator': str(xmp_meta.dc_creator) if hasattr(xmp_meta, 'dc_creator') and xmp_meta.dc_creator else None,
                        'xmp_create_date': str(xmp_meta.xmp_create_date) if hasattr(xmp_meta, 'xmp_create_date') and xmp_meta.xmp_create_date else None,
                        'xmp_modify_date': str(xmp_meta.xmp_modify_date) if hasattr(xmp_meta, 'xmp_modify_date') and xmp_meta.xmp_modify_date else None,
                    }
                except Exception:
                    xmp_metadata = {'error': 'Could not read XMP metadata'}
            
            # File information
            file_stats = pdf_path.stat()
            file_info = {
                'file_size': file_stats.st_size,
                'file_creation_time': datetime.fromtimestamp(file_stats.st_ctime).isoformat(),
                'file_modification_time': datetime.fromtimestamp(file_stats.st_mtime).isoformat(),
                'total_pages': len(reader.pages)
            }
            
            result = {
                'success': True,
                'operation': 'get_pdf_metadata',
                'source_pdf': str(pdf_path),
                'metadata': standard_metadata,
                'file_info': file_info
            }
            
            if include_xmp:
                result['xmp_metadata'] = xmp_metadata
            
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
            result_json = json.dumps(result, ensure_ascii=False, indent=2, default=str)
            self.cache.set(cache_key, result_json, str(pdf_path))
            return result_json
            
        except Exception as e:
            return self._error_response(f"Error reading PDF metadata: {str(e)}")
    
    async def set_pdf_metadata(
        self,
        file_path: Union[str, Path],
        output_file: Optional[str] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        subject: Optional[str] = None,
        creator: Optional[str] = None,
        producer: Optional[str] = None,
        keywords: Optional[str] = None,
        custom_fields: Optional[Dict[str, str]] = None,
        preserve_existing: bool = True
    ) -> str:
        """
        Write/update PDF metadata fields.
        
        Based on Context7 example: writer.add_metadata() with datetime formatting.
        
        Args:
            file_path: Path to source PDF file
            output_file: Output PDF file path (default: overwrite source)
            title: Document title
            author: Document author
            subject: Document subject
            creator: Creator application
            producer: Producer application  
            keywords: Keywords/tags
            custom_fields: Dictionary of custom metadata fields
            preserve_existing: Whether to preserve existing metadata
            
        Returns:
            JSON string with operation results
        """
        
        if not PdfWriter:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Determine output path
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = pdf_path
            
            # Context7 pattern: Create writer from existing PDF
            reader = PdfReader(str(pdf_path))
            writer = PdfWriter()
            
            # Add all pages to the writer
            for page in reader.pages:
                writer.add_page(page)
            
            # Context7 pattern: Preserve existing metadata if requested
            if preserve_existing and reader.metadata is not None:
                writer.add_metadata(reader.metadata)
            
            # Context7 pattern: Format current time for metadata
            utc_time = "+00'00'"  # UTC timezone
            current_time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
            
            # Prepare new metadata based on Context7 example
            new_metadata = {}
            
            if title is not None:
                new_metadata['/Title'] = title
            if author is not None:
                new_metadata['/Author'] = author
            if subject is not None:
                new_metadata['/Subject'] = subject
            if creator is not None:
                new_metadata['/Creator'] = creator
            if producer is not None:
                new_metadata['/Producer'] = producer
            if keywords is not None:
                new_metadata['/Keywords'] = keywords
            
            # Always update modification date
            new_metadata['/ModDate'] = current_time
            
            # Set creation date if not preserving existing
            if not preserve_existing or not (reader.metadata and reader.metadata.creation_date):
                new_metadata['/CreationDate'] = current_time
            
            # Add custom fields
            if custom_fields:
                for key, value in custom_fields.items():
                    # Ensure key starts with /
                    field_key = key if key.startswith('/') else f'/{key}'
                    new_metadata[field_key] = str(value)
            
            # Context7 pattern: Add the new metadata
            if new_metadata:
                writer.add_metadata(new_metadata)
            
            # Save the updated PDF
            with open(str(output_path), "wb") as f:
                writer.write(f)
            
            # Prepare result
            result = {
                'success': True,
                'operation': 'set_pdf_metadata',
                'source_pdf': str(pdf_path),
                'output_pdf': str(output_path),
                'updated_fields': list(new_metadata.keys()),
                'preserve_existing': preserve_existing,
                'file_size': output_path.stat().st_size,
                'metadata_applied': {k.replace('/', ''): v for k, v in new_metadata.items()}
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
            return self._error_response(f"Error setting PDF metadata: {str(e)}")
    
    async def remove_pdf_metadata(
        self,
        file_path: Union[str, Path],
        output_file: Optional[str] = None,
        fields_to_remove: Optional[list] = None,
        remove_all: bool = False
    ) -> str:
        """
        Remove specific metadata fields or all metadata from PDF.
        
        Based on Context7 example: writer.metadata = None for complete removal.
        
        Args:
            file_path: Path to source PDF file
            output_file: Output PDF file path (default: overwrite source)
            fields_to_remove: List of specific fields to remove (e.g., ['title', 'author'])
            remove_all: Remove all metadata (default: False)
            
        Returns:
            JSON string with operation results
        """
        
        if not PdfWriter:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Determine output path
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = pdf_path
            
            # Context7 pattern: Create writer from existing PDF
            writer = PdfWriter(clone_from=str(pdf_path))
            
            if remove_all:
                # Context7 pattern: Remove all metadata
                writer.metadata = None
                removed_fields = ['all_metadata']
            else:
                # Remove specific fields
                if not fields_to_remove:
                    return self._error_response("No fields specified for removal")
                
                current_metadata = dict(writer.metadata) if writer.metadata else {}
                removed_fields = []
                
                for field in fields_to_remove:
                    field_key = self.standard_fields.get(field, f'/{field}')
                    if field_key in current_metadata:
                        del current_metadata[field_key]
                        removed_fields.append(field)
                
                writer.metadata = current_metadata
            
            # Save the updated PDF
            with open(str(output_path), "wb") as f:
                writer.write(f)
            
            result = {
                'success': True,
                'operation': 'remove_pdf_metadata',
                'source_pdf': str(pdf_path),
                'output_pdf': str(output_path),
                'removed_fields': removed_fields,
                'remove_all': remove_all,
                'file_size': output_path.stat().st_size
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
            return self._error_response(f"Error removing PDF metadata: {str(e)}")
    
    def _error_response(self, message: str) -> str:
        """Generate standardized error response."""
        return json.dumps({
            'success': False,
            'error': str(message),
            'operation': 'pdf_metadata_management'
        }, ensure_ascii=False, indent=2, default=str)
