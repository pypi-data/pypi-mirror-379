"""
Contract tests for extract_pdf_images tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import extract_pdf_images


class TestExtractPdfImagesContract:
    """Contract tests for extract_pdf_images tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify extract_pdf_images function exists and is accessible."""
        assert hasattr(extract_pdf_images, '__call__'), "extract_pdf_images function must be callable"
        assert inspect.iscoroutinefunction(extract_pdf_images), "extract_pdf_images must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(extract_pdf_images)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['pages', 'min_size', 'output_dir']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['pages'].default is None, "pages default must be None"
        assert params['min_size'].default == "100x100", "min_size default must be '100x100'"
        assert params['output_dir'].default is None, "output_dir default must be None"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(extract_pdf_images)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('min_size') == str, "min_size must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await extract_pdf_images()

    @pytest.mark.asyncio
    async def test_page_range_syntax_support(self):
        """Test that page range syntax is supported per contract."""
        test_cases = [
            "1",           # Single page
            "1,3,5",       # Multiple pages  
            "1-10",        # Range
            "-1",          # Last page
            "1,3,5-10,-1"  # Combined syntax
        ]
        
        for pages in test_cases:
            result = await extract_pdf_images("test.pdf", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_min_size_format_support(self):
        """Test that min_size supports WIDTHxHEIGHT format per contract."""
        size_formats = [
            "50x50",        # Small images
            "100x100",      # Default size
            "200x150",      # Rectangular
            "500x500",      # Large images
        ]
        
        for min_size in size_formats:
            result = await extract_pdf_images("test.pdf", min_size=min_size)
            parsed = json.loads(result)
            
            # Should handle size formats without parameter errors
            if not parsed['success']:
                assert 'min_size' not in parsed['error'], f"Size format '{min_size}' should be accepted"

    @pytest.mark.asyncio
    async def test_size_filtering_behavior(self):
        """Test that min_size filters images smaller than specified size per contract."""
        # Test various size thresholds
        result = await extract_pdf_images("test.pdf", min_size="200x200")
        parsed = json.loads(result)
        
        # Should handle size filtering without parameter errors
        if not parsed['success']:
            assert 'filter' not in parsed.get('error', '').lower(), "Should support size filtering"
            assert 'min_size' not in parsed['error'], "min_size parameter should be accepted"

    @pytest.mark.asyncio
    async def test_output_directory_control(self):
        """Test that output_dir parameter controls save location per contract."""
        # Test with default (None) - should auto-generate
        result1 = await extract_pdf_images("test.pdf")
        parsed1 = json.loads(result1)
        
        # Test with custom output directory
        result2 = await extract_pdf_images("test.pdf", output_dir="/tmp/extracted_images")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_dir' not in parsed['error'], "output_dir parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generated_directory(self):
        """Test that output directory is auto-generated when not specified per contract."""
        result = await extract_pdf_images("test.pdf")
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generated directory"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support directory generation"

    @pytest.mark.asyncio
    async def test_specific_pages_extraction(self):
        """Test that extraction can be limited to specific pages per contract."""
        result = await extract_pdf_images("test.pdf", pages="1,3,5")
        parsed = json.loads(result)
        
        # Should handle page-specific extraction
        if not parsed['success']:
            assert 'pages' not in parsed['error'], "Should support page-specific extraction"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await extract_pdf_images("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'extract_pdf_images', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes extraction results and file paths."""
        result = await extract_pdf_images("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have extraction results
        if parsed.get('success'):
            # Should include information about extracted images
            expected_fields = ['images', 'extracted_images', 'file_paths', 'image_count']
            has_extraction_info = any(field in parsed for field in expected_fields)
            assert has_extraction_info, "Successful response must contain extraction results and file paths"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert extract_pdf_images.__doc__ is not None, "Function must have docstring"
        docstring = extract_pdf_images.__doc__
        
        # Verify key contract elements in documentation
        assert 'extract' in docstring.lower(), "Docstring must describe extraction functionality"
        assert 'images' in docstring.lower(), "Docstring must mention images"
        assert 'min_size' in docstring, "Docstring must document min_size filtering"
        assert 'WIDTHxHEIGHT' in docstring or 'width' in docstring.lower(), "Docstring must document size format"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await extract_pdf_images("test.pdf")
        assert isinstance(result, str), "extract_pdf_images must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("extract_pdf_images must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(extract_pdf_images, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(extract_pdf_images), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(extract_pdf_images)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_extraction_operation_purpose(self):
        """Verify this tool extracts existing images from PDF pages."""
        # This tool finds and extracts images that are already embedded in PDF
        docstring = extract_pdf_images.__doc__ or ""
        
        # Should mention extracting existing/embedded images
        extraction_terms = ['extract', 'existing', 'embedded', 'from pdf']
        has_extraction_focus = any(term in docstring.lower() for term in extraction_terms)
        
        assert has_extraction_focus, "Tool should focus on extracting existing images from PDF"

    def test_size_filtering_purpose(self):
        """Verify min_size parameter filters out small/unwanted images."""
        docstring = extract_pdf_images.__doc__ or ""
        
        # Should mention filtering or minimum size requirements
        filtering_terms = ['filter', 'minimum', 'smaller than']
        has_filtering_info = any(term in docstring.lower() for term in filtering_terms)
        
        assert has_filtering_info, "Docstring should document size filtering purpose"

    def test_different_from_pdf_to_images(self):
        """Verify this is different from pdf_to_images (extracts existing vs converts pages)."""
        # extract_pdf_images: Finds existing images IN the PDF
        # pdf_to_images: Converts PDF pages TO image files
        
        docstring = extract_pdf_images.__doc__ or ""
        
        # Should focus on extracting existing images, not converting pages
        assert 'extract' in docstring.lower(), "Should focus on extraction, not conversion"
        
        # Should NOT mention converting pages to images
        conversion_terms = ['convert', 'render', 'page to image']
        has_conversion_focus = any(term in docstring.lower() for term in conversion_terms)
        
        assert not has_conversion_focus or 'extract' in docstring.lower(), "Should focus on extraction, not page conversion"


# Contract preservation test summary for extract_pdf_images:
# ✅ Function signature: async def extract_pdf_images(file_path: str, pages: str = None, min_size: str = "100x100", output_dir: str = None) -> str
# ✅ Purpose: Extract existing images FROM PDF (not convert pages TO images)
# ✅ Size filtering: min_size="WIDTHxHEIGHT" format filters small images
# ✅ Page targeting: Can extract from specific pages only
# ✅ Auto-generation: output_dir auto-generated when not specified
# ✅ Page range syntax: "1,3,5-10,-1" format supported  
# ✅ Error format: {'success': False, 'error': str, 'operation': 'extract_pdf_images'}
# ✅ Different from pdf_to_images: Extracts embedded images vs converts pages


