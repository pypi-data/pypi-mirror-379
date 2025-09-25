# Data Model: PDF Reader MCP Refactoring

## Core Entities

### PDFDocument
**Purpose**: Represents a PDF file being processed
**Fields**:
- `file_path: str` - Path to PDF file
- `pages: Optional[str]` - Page range specification
- `metadata: dict` - Document metadata
- `page_count: int` - Total number of pages
- `file_size: int` - File size in bytes
- `last_modified: datetime` - File modification time

**Validation Rules**:
- file_path must exist and be readable
- pages must follow valid range syntax (e.g., "1,3,5-10,-1")
- metadata must be valid JSON serializable dict

### ToolResult
**Purpose**: Standardized response format for all PDF tools
**Fields**:
- `success: bool` - Operation success status
- `data: dict` - Tool-specific result data
- `metadata: dict` - Operation metadata
- `error: Optional[str]` - Error message if failed
- `execution_time: float` - Processing duration

**Validation Rules**:
- success must be boolean
- error required when success=False
- data must be JSON serializable

### CacheEntry
**Purpose**: File-based caching system for processed results
**Fields**:
- `cache_key: str` - Unique identifier for cached data
- `file_hash: str` - Hash of source file for invalidation
- `cached_data: dict` - Cached processing results
- `created_at: datetime` - Cache creation time
- `access_count: int` - Usage frequency counter

**Validation Rules**:
- cache_key must be unique
- file_hash must match source file
- cached_data must be JSON serializable

### TextChunk
**Purpose**: Segmented text data with metadata
**Fields**:
- `text: str` - Extracted text content
- `chunk_index: int` - Position in document
- `page_number: int` - Source page number
- `start_offset: int` - Character offset in original text
- `end_offset: int` - End character offset
- `metadata: dict` - Chunk-specific metadata

**Validation Rules**:
- text must not be empty
- chunk_index must be sequential
- offsets must be valid within source text

### OCRResult
**Purpose**: OCR processing results with confidence scoring
**Fields**:
- `text: str` - Recognized text
- `confidence: float` - OCR confidence score (0-100)
- `language: str` - Detected/specified language
- `page_number: int` - Source page
- `bounding_boxes: List[dict]` - Character/word positions
- `processing_time: float` - OCR duration

**Validation Rules**:
- confidence must be 0-100 range
- language must be valid Tesseract language code
- bounding_boxes must have valid coordinates

## Entity Relationships

### Document Processing Flow
```
PDFDocument → [Tool Processing] → ToolResult
     ↓
  CacheEntry ← [Cache Check] → TextChunk/OCRResult
```

### Tool Categories
- **Text Processing**: PDFDocument → TextChunk → ToolResult
- **OCR Processing**: PDFDocument → OCRResult → ToolResult  
- **Document Operations**: PDFDocument → PDFDocument → ToolResult
- **Image Conversion**: PDFDocument → ImageFiles → ToolResult
- **Metadata Management**: PDFDocument → MetadataDict → ToolResult

## State Transitions

### Document Processing States
1. **Initial**: File path provided
2. **Validated**: File exists and accessible
3. **Loaded**: PDF document opened
4. **Processed**: Tool operation completed
5. **Cached**: Results stored for reuse
6. **Returned**: ToolResult generated

### Cache Lifecycle
1. **Miss**: No cached data found
2. **Hit**: Valid cached data retrieved
3. **Invalid**: Cache outdated (file modified)
4. **Refresh**: New data cached
5. **Cleanup**: Old entries removed

## Configuration Entities

### ServerConfig
**Purpose**: MCP server configuration
**Fields**:
- `server_name: str` - MCP server identifier
- `tools_enabled: List[str]` - Active tool list
- `cache_config: dict` - Caching preferences
- `ocr_config: dict` - OCR engine settings

### ToolConfig
**Purpose**: Individual tool configuration
**Fields**:
- `tool_name: str` - Tool identifier
- `default_params: dict` - Default parameters
- `validation_rules: dict` - Parameter validation
- `timeout_seconds: int` - Processing timeout

## Data Validation Requirements

### File Path Validation
- Must be absolute or relative path
- File must exist and be readable
- Must have .pdf extension
- Size limits may apply per tool

### Page Range Validation
- Support comma-separated pages: "1,3,5"
- Support ranges: "1-10"
- Support negative indexing: "-1" (last page)
- Support combined syntax: "1,3,5-10,-1"

### Output Validation
- All tool results must be JSON serializable
- Error messages must be descriptive
- Success/failure status must be consistent
- Metadata must include processing information

## Persistence Strategy

### File-Based Caching
- Cache directory: `/tmp/pdfreadermcp_cache/` or configurable
- Cache keys: MD5 hash of file path + parameters
- Automatic cleanup of stale entries
- Configurable retention policies

### No Database Required
- All state maintained in memory during processing
- Configuration loaded from pyproject.toml
- No persistent storage beyond caching

## Performance Considerations

### Memory Management
- Stream large files rather than loading entirely
- Chunk text processing for large documents
- Cache cleanup to prevent memory leaks

### I/O Optimization  
- Batch operations where possible
- Reuse PDF file handles within tool execution
- Async processing for independent operations
