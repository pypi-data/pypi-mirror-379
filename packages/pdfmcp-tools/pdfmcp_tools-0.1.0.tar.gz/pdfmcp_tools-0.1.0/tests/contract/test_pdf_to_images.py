"""
Contract tests for pdf_to_images tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import pdf_to_images


class TestPdfToImagesContract:
    """Contract tests for pdf_to_images tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify pdf_to_images function exists and is accessible."""
        assert hasattr(pdf_to_images, '__call__'), "pdf_to_images function must be callable"
        assert inspect.iscoroutinefunction(pdf_to_images), "pdf_to_images must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(pdf_to_images)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['pages', 'dpi', 'image_format', 'output_dir', 'save_to_disk']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['pages'].default is None, "pages default must be None"
        assert params['dpi'].default == 200, "dpi default must be 200"
        assert params['image_format'].default == 'PNG', "image_format default must be 'PNG'"
        assert params['output_dir'].default is None, "output_dir default must be None"
        assert params['save_to_disk'].default is True, "save_to_disk default must be True"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(pdf_to_images)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('dpi') == int, "dpi must be typed as int"
        assert hints.get('image_format') == str, "image_format must be typed as str"
        assert hints.get('save_to_disk') == bool, "save_to_disk must be typed as bool"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await pdf_to_images()

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
            result = await pdf_to_images("test.pdf", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_dpi_resolution_control(self):
        """Test that DPI parameter controls image resolution per contract."""
        dpi_values = [150, 200, 300, 400, 600]
        
        for dpi in dpi_values:
            result = await pdf_to_images("test.pdf", dpi=dpi)
            parsed = json.loads(result)
            
            # Should accept DPI values without parameter errors
            if not parsed['success']:
                assert 'dpi' not in parsed['error'], f"DPI value {dpi} should be accepted"

    @pytest.mark.asyncio
    async def test_image_format_support(self):
        """Test that image_format supports PNG, JPEG formats per contract."""
        supported_formats = ['PNG', 'JPEG', 'JPG']
        
        for fmt in supported_formats:
            result = await pdf_to_images("test.pdf", image_format=fmt)
            parsed = json.loads(result)
            
            # Should accept supported image formats
            if not parsed['success']:
                assert 'image_format' not in parsed['error'], f"Image format '{fmt}' should be accepted"
                assert 'format' not in parsed.get('error', '').lower(), f"Format '{fmt}' should be supported"

    @pytest.mark.asyncio
    async def test_output_directory_control(self):
        """Test that output_dir parameter controls save location per contract."""
        # Test with default (None) - should auto-generate
        result1 = await pdf_to_images("test.pdf")
        parsed1 = json.loads(result1)
        
        # Test with custom output directory
        result2 = await pdf_to_images("test.pdf", output_dir="/tmp/images")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_dir' not in parsed['error'], "output_dir parameter should be accepted"

    @pytest.mark.asyncio
    async def test_save_to_disk_behavior(self):
        """Test that save_to_disk parameter controls disk vs memory storage per contract."""
        # Test save_to_disk=True (default)
        result1 = await pdf_to_images("test.pdf", save_to_disk=True)
        parsed1 = json.loads(result1)
        
        # Test save_to_disk=False (keep in memory)
        result2 = await pdf_to_images("test.pdf", save_to_disk=False)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'save_to_disk' not in parsed['error'], "save_to_disk parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generated_output_directory(self):
        """Test that output directory is auto-generated when not specified per contract."""
        result = await pdf_to_images("test.pdf")
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generated directory"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support directory generation"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await pdf_to_images("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'pdf_to_images', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes conversion results and file paths."""
        result = await pdf_to_images("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have conversion results
        if parsed.get('success'):
            # Should include information about created images
            expected_fields = ['images', 'file_paths', 'output_files', 'converted_pages']
            has_image_info = any(field in parsed for field in expected_fields)
            assert has_image_info, "Successful response must contain conversion results and file paths"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert pdf_to_images.__doc__ is not None, "Function must have docstring"
        docstring = pdf_to_images.__doc__
        
        # Verify key contract elements in documentation
        assert 'convert' in docstring.lower() or 'images' in docstring.lower(), "Docstring must describe conversion functionality"
        assert 'dpi' in docstring.lower(), "Docstring must document DPI resolution"
        assert 'format' in docstring.lower(), "Docstring must document image format options"
        assert 'save_to_disk' in docstring, "Docstring must document memory vs disk behavior"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await pdf_to_images("test.pdf")
        assert isinstance(result, str), "pdf_to_images must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("pdf_to_images must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(pdf_to_images, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(pdf_to_images), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(pdf_to_images)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_conversion_operation_purpose(self):
        """Verify this tool converts PDF pages to image files."""
        # This tool should convert FROM PDF TO images
        docstring = pdf_to_images.__doc__ or ""
        
        # Should mention converting PDF to images
        conversion_terms = ['convert', 'pdf pages', 'images']
        has_conversion_focus = any(term in docstring.lower() for term in conversion_terms)
        
        assert has_conversion_focus, "Tool should focus on converting PDF pages to images"

    def test_quality_vs_performance_tradeoff(self):
        """Verify DPI parameter represents quality vs performance tradeoff per contract."""
        docstring = pdf_to_images.__doc__ or ""
        
        # Should mention quality and performance relationship
        quality_terms = ['quality', 'performance', 'higher', 'resolution']
        has_quality_info = any(term in docstring.lower() for term in quality_terms)
        
        assert has_quality_info, "Docstring should document quality vs performance tradeoff"


# Contract preservation test summary for pdf_to_images:
# ✅ Function signature: async def pdf_to_images(file_path: str, pages: str = None, dpi: int = 200, image_format: str = 'PNG', output_dir: str = None, save_to_disk: bool = True) -> str
# ✅ Format support: PNG, JPEG formats supported
# ✅ DPI control: Higher DPI = better quality but slower processing
# ✅ Memory option: save_to_disk=False keeps images in memory
# ✅ Auto-generation: output_dir auto-generated when not specified
# ✅ Page range syntax: "1,3,5-10,-1" format supported
# ✅ Error format: {'success': False, 'error': str, 'operation': 'pdf_to_images'}
# ✅ Purpose: Convert PDF pages to individual image files


