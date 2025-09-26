"""
MCP Server for PDF processing with comprehensive tool support.

Provides 18 PDF processing tools through FastMCP interface:
- Text extraction and search
- Document operations (split, merge, extract) 
- OCR processing with Tesseract
- Image conversion and extraction
- Metadata management
- PDF optimization and compression
"""

import json
from typing import Any, List, Optional
from mcp.server.fastmcp import FastMCP
from .tools.pdf_reader import PDFReader
from .tools.pdf_operations import PDFOperations
from .tools.pdf_ocr import PDFOCRTool
from .tools.pdf_image_converter import PDFImageConverter
from .tools.pdf_metadata import PDFMetadataManager
from .tools.pdf_text_search import PDFTextSearcher
from .tools.pdf_optimizer import PDFOptimizer

# Create FastMCP app
app = FastMCP("PDF Reader MCP Server")

# Initialize PDF processing tools
pdf_reader = PDFReader()
pdf_operations = PDFOperations()
pdf_ocr = PDFOCRTool()
pdf_image_converter = PDFImageConverter()
pdf_metadata_manager = PDFMetadataManager()
pdf_text_searcher = PDFTextSearcher()
pdf_optimizer = PDFOptimizer()


def _standardize_error_response(result: str, operation_name: str) -> str:
    """
    Standardize error responses from underlying tools to ensure consistent operation names.
    
    Args:
        result: JSON string result from underlying tool
        operation_name: Correct operation name for this server-level tool
        
    Returns:
        JSON string with standardized operation field
    """
    try:
        parsed_result = json.loads(result)
        if not parsed_result.get('success', True):
            # Add or override the operation field with correct tool name
            parsed_result['operation'] = operation_name
            return json.dumps(parsed_result, ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        pass
    
    return result


@app.tool()
async def read_pdf(
    file_path: str,
    pages: str = None,
    chunk_size: int = 1000,
    chunk_overlap: int = 100
) -> str:
    """Extract text from PDF files with intelligent page handling and chunking.
    
    Args:
        file_path: Path to the PDF file
        pages: Page range (e.g., '1,3,5-10,-1' for pages 1, 3, 5 to 10, and last page)
        chunk_size: Maximum size of text chunks
        chunk_overlap: Overlap between chunks to preserve context
        
    Returns:
        JSON string with extracted text and metadata
    """
    try:
        result = await pdf_reader.extract_text(
            file_path=file_path,
            pages=pages,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return result
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF text extraction failed: {str(e)}',
            'operation': 'read_pdf'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def split_pdf(
    file_path: str,
    split_ranges: List[str],
    output_dir: str = None,
    prefix: str = None
) -> str:
    """Split PDF into multiple files based on page ranges.
    
    Args:
        file_path: Path to the source PDF file
        split_ranges: List of page ranges (e.g., ["1-5", "6-10", "11-15"])
        output_dir: Output directory (defaults to source file directory)
        prefix: Output file prefix (defaults to source filename)
        
    Returns:
        JSON string with split operation results and output file information
    """
    try:
        result = await pdf_operations.split_pdf(
            file_path=file_path,
            split_ranges=split_ranges,
            output_dir=output_dir,
            prefix=prefix
        )
        
        return _standardize_error_response(result, 'split_pdf')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF split failed: {str(e)}',
            'operation': 'split_pdf'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def extract_pages(
    file_path: str,
    pages: str,
    output_file: str = None,
    output_dir: str = None
) -> str:
    """Extract specific pages from PDF to a new file.
    
    Args:
        file_path: Path to the source PDF file
        pages: Page range (e.g., "1,3,5-7" for pages 1, 3, and 5 to 7)
        output_file: Output filename (optional, auto-generated if not provided)
        output_dir: Output directory (defaults to source file directory)
        
    Returns:
        JSON string with extraction results and output file information
    """
    try:
        result = await pdf_operations.extract_pages(
            file_path=file_path,
            pages=pages,
            output_file=output_file,
            output_dir=output_dir
        )
        
        return _standardize_error_response(result, 'extract_pages')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'Page extraction failed: {str(e)}',
            'operation': 'extract_pages'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def merge_pdfs(
    file_paths: List[str],
    output_file: str = None,
    output_dir: str = None
) -> str:
    """Merge multiple PDF files into a single file.
    
    Pages are processed in the order specified in the file_paths list,
    preserving the original page sequence in the merged document.
    
    Args:
        file_paths: List of PDF file paths to merge
        output_file: Output filename (optional, auto-generated if not provided)
        output_dir: Output directory (defaults to first file's directory)
        
    Returns:
        JSON string with merge results and output file information
    """
    try:
        result = await pdf_operations.merge_pdfs(
            file_paths=file_paths,
            output_file=output_file,
            output_dir=output_dir
        )
        
        return _standardize_error_response(result, 'merge_pdfs')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF merge failed: {str(e)}',
            'operation': 'merge_pdfs'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def ocr_pdf(
    file_path: str,
    pages: str = None,
    language: str = 'chi_sim',
    chunk_size: int = 1000,
    chunk_overlap: int = 100,
    dpi: int = 200
) -> str:
    """Perform OCR on PDF pages using Tesseract for scanned documents.
    
    Args:
        file_path: Path to the PDF file
        pages: Page range (e.g., '1,3,5-10,-1' for pages 1, 3, 5 to 10, and last page)
        language: OCR language code (default: 'chi_sim' for simplified Chinese)
        chunk_size: Maximum size of text chunks
        chunk_overlap: Overlap between chunks to preserve context
        dpi: DPI for PDF to image conversion (higher = better quality, slower)
        
    Returns:
        JSON string with OCR results and metadata
    """
    try:
        result = await pdf_ocr.perform_ocr(
            file_path=file_path,
            pages=pages,
            language=language,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            dpi=dpi
        )
        return _standardize_error_response(result, 'ocr_pdf')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF OCR failed: {str(e)}',
            'operation': 'ocr_pdf'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def pdf_to_images(
    file_path: str,
    pages: str = None,
    dpi: int = 200,
    image_format: str = 'PNG',
    output_dir: str = None,
    save_to_disk: bool = True
) -> str:
    """Convert PDF pages to images.
    
    Args:
        file_path: Path to PDF file
        pages: Page range (e.g., '1,3,5-10,-1' for pages 1, 3, 5 to 10, and last page)
        dpi: Resolution for image conversion (default: 200)
        image_format: Output format ('PNG', 'JPEG', etc.)
        output_dir: Directory to save images (default: auto-generated)
        save_to_disk: Whether to save images to disk or keep in memory
        
    Returns:
        JSON string with conversion results and file paths
    """
    try:
        result = await pdf_image_converter.pdf_to_images(
            file_path=file_path,
            pages=pages,
            dpi=dpi,
            image_format=image_format,
            output_dir=output_dir,
            save_to_disk=save_to_disk
        )
        return _standardize_error_response(result, 'pdf_to_images')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF to images conversion failed: {str(e)}',
            'operation': 'pdf_to_images'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def images_to_pdf(
    image_paths: List[str],
    output_file: str,
    page_size: str = "A4",
    quality: int = 95,
    title: str = None,
    author: str = None
) -> str:
    """Convert multiple images to a single PDF.
    
    Images are processed in the order specified in the image_paths list,
    preserving their sequence in the final PDF document.
    
    Args:
        image_paths: List of image file paths to convert
        output_file: Output PDF file path
        page_size: Page size ('A4', 'Letter', 'Legal', or 'auto')
        quality: JPEG quality for compression (1-100)
        title: PDF document title (optional)
        author: PDF document author (optional)
        
    Returns:
        JSON string with conversion results
    """
    try:
        result = await pdf_image_converter.images_to_pdf(
            image_paths=image_paths,
            output_file=output_file,
            page_size=page_size,
            quality=quality,
            title=title,
            author=author
        )
        return _standardize_error_response(result, 'images_to_pdf')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'Images to PDF conversion failed: {str(e)}',
            'operation': 'images_to_pdf'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def extract_pdf_images(
    file_path: str,
    pages: str = None,
    min_size: str = "100x100",
    output_dir: str = None
) -> str:
    """Extract images from PDF pages.
    
    Args:
        file_path: Path to PDF file
        pages: Page range (e.g., '1,3,5-10,-1' for specific pages)
        min_size: Minimum image size to extract (format: 'WIDTHxHEIGHT', e.g., '100x100')
        output_dir: Directory to save extracted images (default: auto-generated)
        
    Returns:
        JSON string with extraction results and file paths
    """
    try:
        # Parse min_size string to tuple
        if 'x' in min_size:
            width, height = map(int, min_size.split('x'))
            min_size_tuple = (width, height)
        else:
            min_size_tuple = (100, 100)  # default
            
        result = await pdf_image_converter.extract_pdf_images(
            file_path=file_path,
            pages=pages,
            min_size=min_size_tuple,
            output_dir=output_dir
        )
        return _standardize_error_response(result, 'extract_pdf_images')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF image extraction failed: {str(e)}',
            'operation': 'extract_pdf_images'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def get_pdf_metadata(
    file_path: str,
    include_xmp: bool = False
) -> str:
    """Read PDF metadata including standard fields and optionally XMP metadata.
    
    Args:
        file_path: Path to PDF file
        include_xmp: Whether to include advanced XMP metadata (default: False)
        
    Returns:
        JSON string with comprehensive metadata information
    """
    try:
        result = await pdf_metadata_manager.get_pdf_metadata(
            file_path=file_path,
            include_xmp=include_xmp
        )
        return _standardize_error_response(result, 'get_pdf_metadata')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF metadata reading failed: {str(e)}',
            'operation': 'get_pdf_metadata'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def set_pdf_metadata(
    file_path: str,
    output_file: str = None,
    title: str = None,
    author: str = None,
    subject: str = None,
    creator: str = None,
    producer: str = None,
    keywords: str = None,
    preserve_existing: bool = True
) -> str:
    """Write or update PDF metadata fields.
    
    Args:
        file_path: Path to source PDF file
        output_file: Output PDF file path (optional, defaults to overwrite source)
        title: Document title
        author: Document author
        subject: Document subject  
        creator: Creator application name
        producer: Producer application name
        keywords: Keywords or tags (comma-separated)
        preserve_existing: Whether to preserve existing metadata (default: True)
        
    Returns:
        JSON string with operation results
    """
    try:
        result = await pdf_metadata_manager.set_pdf_metadata(
            file_path=file_path,
            output_file=output_file,
            title=title,
            author=author,
            subject=subject,
            creator=creator,
            producer=producer,
            keywords=keywords,
            preserve_existing=preserve_existing
        )
        return _standardize_error_response(result, 'set_pdf_metadata')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF metadata writing failed: {str(e)}',
            'operation': 'set_pdf_metadata'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def remove_pdf_metadata(
    file_path: str,
    output_file: str = None,
    fields_to_remove: List[str] = None,
    remove_all: bool = False
) -> str:
    """Remove specific metadata fields or all metadata from PDF.
    
    The fields_to_remove and remove_all parameters are mutually exclusive:
    use either fields_to_remove for selective removal OR remove_all for complete removal.
    
    Args:
        file_path: Path to source PDF file
        output_file: Output PDF file path (optional, defaults to overwrite source)
        fields_to_remove: List of specific fields to remove (e.g., ['title', 'author'])
        remove_all: Remove all metadata if True (default: False)
        
    Returns:
        JSON string with operation results
    """
    try:
        result = await pdf_metadata_manager.remove_pdf_metadata(
            file_path=file_path,
            output_file=output_file,
            fields_to_remove=fields_to_remove,
            remove_all=remove_all
        )
        return _standardize_error_response(result, 'remove_pdf_metadata')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF metadata removal failed: {str(e)}',
            'operation': 'remove_pdf_metadata'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def search_pdf_text(
    file_path: str,
    query: str,
    pages: str = None,
    case_sensitive: bool = False,
    regex_search: bool = False,
    context_chars: int = 100,
    max_matches: int = 100
) -> str:
    """Search for text content across PDF pages with detailed match information.
    
    Args:
        file_path: Path to PDF file
        query: Text to search for (or regex pattern if regex_search=True)
        pages: Page range (e.g., '1,3,5-10,-1') or None for all pages
        case_sensitive: Whether search is case-sensitive (default: False)
        regex_search: Whether to treat query as regex pattern (default: False)
        context_chars: Number of characters to show around matches (default: 100)
        max_matches: Maximum number of matches to return (default: 100)
        
    Returns:
        JSON string with search results, match locations, and context
    """
    try:
        result = await pdf_text_searcher.search_pdf_text(
            file_path=file_path,
            query=query,
            pages=pages,
            case_sensitive=case_sensitive,
            regex_search=regex_search,
            context_chars=context_chars,
            max_matches=max_matches
        )
        
        return _standardize_error_response(result, 'search_pdf_text')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF text search failed: {str(e)}',
            'operation': 'search_pdf_text'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def extract_page_text(
    file_path: str,
    page_number: int,
    extraction_mode: str = "default"
) -> str:
    """Extract text from a specific PDF page with various extraction options.
    
    Args:
        file_path: Path to PDF file
        page_number: Page number to extract (1-based)
        extraction_mode: Text extraction mode ('default', 'layout', 'simple')
        
    Returns:
        JSON string with extracted text and statistics
    """
    try:
        result = await pdf_text_searcher.extract_page_text(
            file_path=file_path,
            page_number=page_number,
            extraction_mode=extraction_mode
        )
        
        return _standardize_error_response(result, 'extract_page_text')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'Page text extraction failed: {str(e)}',
            'operation': 'extract_page_text'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def find_and_highlight_text(
    file_path: str,
    query: str,
    pages: str = None,
    case_sensitive: bool = False
) -> str:
    """Find text and return information for highlighting matches.
    
    Args:
        file_path: Path to PDF file
        query: Text to search for
        pages: Page range (e.g., '1,3,5-10,-1') or None for all pages
        case_sensitive: Whether search is case-sensitive (default: False)
        
    Returns:
        JSON string with page highlights and position information
    """
    try:
        result = await pdf_text_searcher.find_and_highlight_text(
            file_path=file_path,
            query=query,
            pages=pages,
            case_sensitive=case_sensitive
        )
        
        return _standardize_error_response(result, 'find_and_highlight_text')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'Text highlighting search failed: {str(e)}',
            'operation': 'find_and_highlight_text'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def optimize_pdf(
    file_path: str,
    output_file: str = None,
    optimization_level: str = 'medium'
) -> str:
    """Optimize PDF file using various compression techniques.
    
    Args:
        file_path: Path to source PDF file
        output_file: Output PDF file path (optional, defaults to '_optimized' suffix)
        optimization_level: Optimization preset ('light', 'medium', 'heavy', 'maximum')
        
    Returns:
        JSON string with optimization results and file size statistics
    """
    try:
        result = await pdf_optimizer.optimize_pdf(
            file_path=file_path,
            output_file=output_file,
            optimization_level=optimization_level
        )
        return _standardize_error_response(result, 'optimize_pdf')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF optimization failed: {str(e)}',
            'operation': 'optimize_pdf'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def compress_pdf_images(
    file_path: str,
    output_file: str = None,
    quality: int = 80
) -> str:
    """Compress images in PDF while preserving document structure.
    
    Args:
        file_path: Path to source PDF file
        output_file: Output PDF file path (optional, auto-generated)
        quality: Image compression quality (1-100, where 100=best quality)
        
    Returns:
        JSON string with compression results and statistics
    """
    try:
        result = await pdf_optimizer.compress_pdf_images(
            file_path=file_path,
            output_file=output_file,
            quality=quality
        )
        return _standardize_error_response(result, 'compress_pdf_images')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF image compression failed: {str(e)}',
            'operation': 'compress_pdf_images'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def remove_pdf_content(
    file_path: str,
    output_file: str = None,
    remove_images: bool = False,
    remove_annotations: bool = False,
    compress_streams: bool = True
) -> str:
    """Remove specific content from PDF to reduce file size.
    
    Args:
        file_path: Path to source PDF file
        output_file: Output PDF file path (optional, auto-generated)
        remove_images: Whether to remove all images
        remove_annotations: Whether to remove annotations
        compress_streams: Whether to compress content streams
        
    Returns:
        JSON string with content removal results and statistics
    """
    try:
        result = await pdf_optimizer.remove_pdf_content(
            file_path=file_path,
            output_file=output_file,
            remove_images=remove_images,
            remove_annotations=remove_annotations,
            compress_streams=compress_streams
        )
        return _standardize_error_response(result, 'remove_pdf_content')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF content removal failed: {str(e)}',
            'operation': 'remove_pdf_content'
        }, ensure_ascii=False, indent=2)


@app.tool()
async def analyze_pdf_size(
    file_path: str
) -> str:
    """Analyze PDF file to identify optimization opportunities.
    
    Provides detailed size breakdown by content type (text, images, metadata, etc.)
    and recommends specific optimization strategies for file size reduction.
    
    Args:
        file_path: Path to PDF file to analyze
        
    Returns:
        JSON string with size analysis breakdown and optimization recommendations
    """
    try:
        result = await pdf_optimizer.analyze_pdf_size(
            file_path=file_path
        )
        return _standardize_error_response(result, 'analyze_pdf_size')
    except Exception as e:
        return json.dumps({
            'success': False,
            'error': f'PDF size analysis failed: {str(e)}',
            'operation': 'analyze_pdf_size'
        }, ensure_ascii=False, indent=2)
