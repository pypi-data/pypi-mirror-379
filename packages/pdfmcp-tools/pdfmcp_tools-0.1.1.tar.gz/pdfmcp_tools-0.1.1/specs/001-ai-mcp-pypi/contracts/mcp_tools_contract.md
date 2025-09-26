# MCP Tools Contract Specification

## Overview
This document defines the interface contracts for all 18 PDF processing tools that MUST be preserved during refactoring. Any changes to these interfaces will break existing MCP client integrations.

## Tool Categories

### 📖 Text Processing Tools (5 tools)

#### read_pdf
**Purpose**: Extract text from PDF with intelligent page handling and chunking
```python
async def read_pdf(
    file_path: str,
    pages: str = None,
    chunk_size: int = 1000,
    chunk_overlap: int = 100
) -> str
```
**Contract Requirements**:
- Returns JSON string with extracted text and metadata
- Must support page range syntax: "1,3,5-10,-1"
- Must preserve chunking behavior exactly
- Error format: `{'success': False, 'error': str, 'extraction_method': 'text_extraction'}`

#### extract_page_text
**Purpose**: Extract text from a specific PDF page with various extraction options
```python
async def extract_page_text(
    file_path: str,
    page_number: int,
    extraction_mode: str = "default"
) -> str
```
**Contract Requirements**:
- page_number is 1-based indexing
- extraction_mode values: "default", "layout", "simple"
- Returns JSON with text and statistics

#### search_pdf_text
**Purpose**: Search for text content across PDF pages with detailed match information
```python
async def search_pdf_text(
    file_path: str,
    query: str,
    pages: str = None,
    case_sensitive: bool = False,
    regex_search: bool = False,
    context_chars: int = 100,
    max_matches: int = 100
) -> str
```
**Contract Requirements**:
- Supports regex patterns when regex_search=True
- Returns matches with context and location information
- Must limit results to max_matches

#### find_and_highlight_text  
**Purpose**: Find text and return information for highlighting matches
```python
async def find_and_highlight_text(
    file_path: str,
    query: str,
    pages: str = None,
    case_sensitive: bool = False
) -> str
```
**Contract Requirements**:
- Returns page highlights and position information
- Compatible with PDF viewer highlight systems

#### get_pdf_metadata
**Purpose**: Read PDF metadata including standard fields and optionally XMP metadata
```python
async def get_pdf_metadata(
    file_path: str,
    include_xmp: bool = False
) -> str
```
**Contract Requirements**:
- Standard metadata always included
- XMP metadata only when include_xmp=True
- Returns comprehensive metadata information

### 📄 Document Operations Tools (5 tools)

#### split_pdf
**Purpose**: Split PDF into multiple files based on page ranges
```python
async def split_pdf(
    file_path: str,
    split_ranges: List[str],
    output_dir: str = None,
    prefix: str = None
) -> str
```
**Contract Requirements**:
- split_ranges format: ["1-5", "6-10", "11-15"]
- Default output_dir: source file directory
- Default prefix: source filename
- Returns file paths and operation results

#### extract_pages
**Purpose**: Extract specific pages from PDF to a new file
```python
async def extract_pages(
    file_path: str,
    pages: str,
    output_file: str = None,
    output_dir: str = None
) -> str
```
**Contract Requirements**:
- pages syntax: "1,3,5-7" 
- Auto-generates output_file if not provided
- Returns extraction results and output file info

#### merge_pdfs
**Purpose**: Merge multiple PDF files into a single file
```python
async def merge_pdfs(
    file_paths: List[str],
    output_file: str = None,
    output_dir: str = None
) -> str
```
**Contract Requirements**:
- Preserves page order from file_paths list
- Auto-generates output_file if not provided
- Default output_dir: first file's directory

#### set_pdf_metadata
**Purpose**: Write or update PDF metadata fields
```python
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
) -> str
```
**Contract Requirements**:
- preserve_existing=True preserves unspecified fields
- Can overwrite source file if output_file=None
- Returns operation results

#### remove_pdf_metadata
**Purpose**: Remove specific metadata fields or all metadata from PDF
```python
async def remove_pdf_metadata(
    file_path: str,
    output_file: str = None,
    fields_to_remove: List[str] = None,
    remove_all: bool = False
) -> str
```
**Contract Requirements**:
- fields_to_remove: specific field names
- remove_all=True removes all metadata
- Mutually exclusive: fields_to_remove OR remove_all

### 🔍 OCR Processing Tool (1 tool)

#### ocr_pdf
**Purpose**: Perform OCR on PDF pages using Tesseract for scanned documents
```python
async def ocr_pdf(
    file_path: str,
    pages: str = None,
    language: str = 'chi_sim',
    chunk_size: int = 1000,
    chunk_overlap: int = 100,
    dpi: int = 200
) -> str
```
**Contract Requirements**:
- Default language: 'chi_sim' (simplified Chinese)
- Must support all Tesseract language codes
- Returns OCR results with confidence scoring
- DPI affects quality and processing time

### 🖼️ Image Conversion Tools (3 tools)

#### pdf_to_images
**Purpose**: Convert PDF pages to images
```python
async def pdf_to_images(
    file_path: str,
    pages: str = None,
    dpi: int = 200,
    image_format: str = 'PNG',
    output_dir: str = None,
    save_to_disk: bool = True
) -> str
```
**Contract Requirements**:
- Supports PNG, JPEG formats
- save_to_disk=False keeps images in memory
- Returns conversion results and file paths

#### images_to_pdf
**Purpose**: Convert multiple images to a single PDF
```python
async def images_to_pdf(
    image_paths: List[str],
    output_file: str,
    page_size: str = "A4",
    quality: int = 95,
    title: str = None,
    author: str = None
) -> str
```
**Contract Requirements**:
- page_size options: "A4", "Letter", "Legal", "auto"
- quality range: 1-100
- Preserves image order in PDF

#### extract_pdf_images
**Purpose**: Extract images from PDF pages
```python
async def extract_pdf_images(
    file_path: str,
    pages: str = None,
    min_size: str = "100x100",
    output_dir: str = None
) -> str
```
**Contract Requirements**:
- min_size format: "WIDTHxHEIGHT"
- Filters images smaller than min_size
- Returns extracted image file paths

### 🎯 Optimization Tools (4 tools)

#### optimize_pdf
**Purpose**: Optimize PDF file using various compression techniques
```python
async def optimize_pdf(
    file_path: str,
    output_file: str = None,
    optimization_level: str = 'medium'
) -> str
```
**Contract Requirements**:
- optimization_level: 'light', 'medium', 'heavy', 'maximum'
- Returns file size statistics and compression ratio

#### compress_pdf_images
**Purpose**: Compress images in PDF while preserving document structure
```python
async def compress_pdf_images(
    file_path: str,
    output_file: str = None,
    quality: int = 80
) -> str
```
**Contract Requirements**:
- quality range: 1-100 (100=best quality)
- Preserves all non-image content exactly

#### remove_pdf_content
**Purpose**: Remove specific content from PDF to reduce file size
```python
async def remove_pdf_content(
    file_path: str,
    output_file: str = None,
    remove_images: bool = False,
    remove_annotations: bool = False,
    compress_streams: bool = True
) -> str
```
**Contract Requirements**:
- Selective content removal options
- compress_streams=True by default for size reduction

#### analyze_pdf_size
**Purpose**: Analyze PDF file to identify optimization opportunities
```python
async def analyze_pdf_size(
    file_path: str
) -> str
```
**Contract Requirements**:
- Read-only analysis, no file modification
- Returns optimization recommendations
- Includes size breakdown by content type

## Global Contract Requirements

### Error Handling
All tools must return consistent error format:
```json
{
    "success": false,
    "error": "Descriptive error message",
    "operation": "tool_name"
}
```

### Page Range Syntax
All tools accepting `pages` parameter must support:
- Single pages: "1", "5", "10"
- Multiple pages: "1,3,5"
- Ranges: "1-10", "5-15"
- Negative indexing: "-1" (last page), "-2" (second to last)
- Combined: "1,3,5-10,-1"

### Output Format
- All tools return JSON strings (not objects)
- Success responses include metadata
- File operations include file paths and sizes
- Processing time included where relevant

### Async Compatibility
- All tools are async functions
- Must be awaitable
- Exception handling must be internal (no unhandled exceptions)

## Testing Requirements

Each tool must have:
1. **Contract tests**: Verify function signatures and parameter types
2. **Success path tests**: Valid inputs produce expected outputs  
3. **Error path tests**: Invalid inputs produce proper error responses
4. **Edge case tests**: Boundary conditions and special cases

## Breaking Changes (Forbidden)
- Changing function signatures
- Changing parameter names or types
- Changing return value format
- Removing tools
- Changing error response format
- Changing page range syntax behavior
