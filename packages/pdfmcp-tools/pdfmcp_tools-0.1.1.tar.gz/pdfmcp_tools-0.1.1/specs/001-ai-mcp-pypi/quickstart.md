# Quickstart: PDF Reader MCP Refactoring Validation

## Overview
This quickstart guide validates that the refactored MCP server maintains all functionality while supporting the new PyPI + uvx installation workflow.

## Prerequisites
- Python 3.11+
- uv package manager installed
- Tesseract OCR engine installed
- Sample PDF files for testing

## Validation Workflow

### Phase 1: Local Development Validation
**Goal**: Verify refactored code works in development environment

#### Step 1: Environment Setup
```bash
# Clean existing environment
rm -rf .venv
rm -f uv.lock

# Fresh installation
uv sync
```

#### Step 2: Server Startup Test  
```bash
# Start MCP server
uv run pdfreadermcp

# Expected: Server starts without errors
# Expected: No import failures or dependency issues  
# Expected: All 18 tools registered successfully
```

#### Step 3: Tool Functionality Validation
Test each tool category to ensure refactoring preserved functionality:

**Text Processing Tools Test**:
```bash
# Create test script or use MCP client to test:
# - read_pdf with sample document
# - extract_page_text from specific page
# - search_pdf_text for known content
# - find_and_highlight_text with search term
# - get_pdf_metadata to verify document info

# Expected: All tools return expected JSON format
# Expected: No changes to tool behavior
# Expected: Error handling works correctly
```

**Document Operations Test**:
```bash
# Test document manipulation:
# - split_pdf into multiple files
# - extract_pages to new document  
# - merge_pdfs back together
# - set_pdf_metadata with new values
# - remove_pdf_metadata selectively

# Expected: Files created/modified correctly
# Expected: Operation results match contract
# Expected: Default output directories work
```

**OCR Processing Test**:
```bash
# Test OCR functionality:
# - ocr_pdf with scanned document
# - Test Chinese and English content
# - Verify confidence scoring

# Expected: OCR results with proper formatting
# Expected: Language detection works
# Expected: Performance acceptable
```

**Image Conversion Test**:
```bash
# Test image conversion:
# - pdf_to_images with various formats
# - images_to_pdf reconstruction  
# - extract_pdf_images from document

# Expected: Images created with correct formats
# Expected: Quality settings respected
# Expected: File paths returned correctly
```

**Optimization Tools Test**:
```bash
# Test PDF optimization:
# - optimize_pdf with different levels
# - compress_pdf_images quality control
# - remove_pdf_content selective removal
# - analyze_pdf_size recommendations

# Expected: File sizes reduced appropriately
# Expected: Content preserved correctly
# Expected: Analysis provides useful insights
```

### Phase 2: PyPI Package Validation  
**Goal**: Verify package builds and publishes correctly

#### Step 4: Package Building
```bash
# Build package
uv build

# Expected: Wheel and source distributions created
# Expected: No build errors or warnings
# Expected: Package metadata correct
```

#### Step 5: Local Package Installation
```bash
# Test local installation
pip install dist/pdfreadermcp-*.whl

# Test entry point
pdfreadermcp --help  # or however entry point works

# Expected: Package installs successfully
# Expected: Entry point accessible
# Expected: Dependencies resolved correctly
```

#### Step 6: Test PyPI Upload (Staging)
```bash
# Upload to test PyPI (if credentials configured)
uv publish --repository testpypi

# Expected: Upload succeeds
# Expected: Package appears on test.pypi.org
# Expected: Metadata displayed correctly
```

### Phase 3: uvx Installation Validation
**Goal**: Verify uvx can install and run the package

#### Step 7: uvx Installation Test
```bash
# Remove local installation
pip uninstall pdfreadermcp

# Test uvx installation and execution
uvx pdfreadmcp

# Expected: Package downloads and installs
# Expected: MCP server starts correctly  
# Expected: All tools available
```

#### Step 8: Claude Desktop Integration Test
Update Claude Desktop configuration:
```json
{
  "mcpServers": {
    "pdfreadermcp": {
      "command": "uvx",
      "args": ["pdfreadermcp"]
    }
  }
}
```

**Validation Steps**:
1. Restart Claude Desktop
2. Verify MCP server connects
3. Test PDF processing in Claude chat
4. Confirm all 18 tools accessible

### Phase 4: Integration Testing
**Goal**: End-to-end workflow validation

#### Step 9: Real-world Workflow Test
Complete PDF processing workflow:
```bash
# 1. Extract text from multi-page PDF
# 2. Search for specific content  
# 3. Split document by sections
# 4. OCR any scanned pages
# 5. Optimize final documents
# 6. Extract metadata and images

# Expected: All operations complete successfully
# Expected: Output files created correctly
# Expected: Processing time acceptable
```

#### Step 10: Error Handling Validation
Test error scenarios:
```bash
# - Invalid file paths
# - Corrupted PDF files
# - Invalid parameter combinations
# - Permission issues
# - Missing Tesseract installation

# Expected: Graceful error messages
# Expected: No server crashes
# Expected: Consistent error format
```

## Success Criteria

### Functional Requirements Validation
- ✅ **FR-001**: All 18 PDF tools work identically to before refactoring
- ✅ **FR-002**: Code structure cleaned and follows Python best practices  
- ✅ **FR-003**: Package builds and publishes to PyPI successfully
- ✅ **FR-004**: `uvx pdfreadermcp` command starts MCP server
- ✅ **FR-005**: Virtual environment cleaned and dependencies optimized
- ✅ **FR-006**: MCP server capabilities unchanged
- ✅ **FR-007**: pyproject.toml properly configured for PyPI
- ✅ **FR-008**: Unnecessary files removed, project structure clean
- ✅ **FR-009**: All tools tested and verified working
- ✅ **FR-010**: Installation and usage instructions updated

### Acceptance Scenarios Validation
1. ✅ Messy code → clean professional structure (all tools preserved)
2. ✅ Refactored project → successful PyPI publication  
3. ✅ Dirty environment → clean rebuild with proper dependencies
4. ✅ Published package → successful `uvx pdfreadermcp` execution

## Troubleshooting Guide

### Common Issues

#### Server Won't Start
```bash
# Check dependencies
uv sync --reinstall

# Check entry point
python -m pdfreadermcp

# Check for import errors
python -c "from pdfreadermcp import server"
```

#### Tool Functionality Issues  
```bash
# Verify Tesseract installation
tesseract --version

# Check file permissions
ls -la sample.pdf

# Test with simple PDF first
```

#### uvx Installation Problems
```bash
# Update uvx
uv self update

# Clear uvx cache
uvx --clear-cache pdfreadermcp

# Check network connectivity
ping pypi.org
```

## Performance Benchmarks

Document processing times for validation:
- Text extraction: < 1s per page
- OCR processing: < 5s per page  
- PDF operations: < 0.5s per page
- Image conversion: < 2s per page
- Optimization: < 3s per MB

## Validation Checklist

**Pre-Refactoring Baseline**:
- [ ] Record current tool outputs for comparison
- [ ] Document processing times
- [ ] Note any existing issues

**Post-Refactoring Validation**:
- [ ] All 18 tools return identical outputs
- [ ] Performance maintained or improved
- [ ] Error messages consistent and helpful
- [ ] Package builds without warnings
- [ ] uvx installation works smoothly
- [ ] Claude Desktop integration successful
- [ ] Documentation updated and accurate

**Final Sign-off**:
- [ ] Code quality improved
- [ ] All tests passing  
- [ ] PyPI package published
- [ ] User workflow validated
- [ ] No functional regressions introduced

This quickstart serves as both validation guide and future regression testing procedure.
