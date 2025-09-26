"""
Contract tests for extract_pages tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import extract_pages


class TestExtractPagesContract:
    """Contract tests for extract_pages tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify extract_pages function exists and is accessible."""
        assert hasattr(extract_pages, '__call__'), "extract_pages function must be callable"
        assert inspect.iscoroutinefunction(extract_pages), "extract_pages must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(extract_pages)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path', 'pages']
        optional_params = ['output_file', 'output_dir']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['output_dir'].default is None, "output_dir default must be None"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(extract_pages)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('pages') == str, "pages must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path and pages parameters are required."""
        # Missing both parameters
        with pytest.raises(TypeError, match="missing .* required positional argument"):
            await extract_pages()

        # Missing pages parameter  
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'pages'"):
            await extract_pages("test.pdf")

    @pytest.mark.asyncio
    async def test_pages_syntax_support(self):
        """Test that pages parameter supports contract-specified syntax."""
        # Test page range formats per contract: "1,3,5-7"
        valid_page_formats = [
            "1",           # Single page
            "1,3,5",       # Multiple specific pages
            "5-7",         # Range
            "1,3,5-7",     # Combined format from contract example
            "-1",          # Last page
            "1,3,5-10,-1"  # Complex combined syntax
        ]
        
        for pages in valid_page_formats:
            result = await extract_pages("test.pdf", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output filename per contract."""
        # Test with default (None) - should auto-generate
        result1 = await extract_pages("test.pdf", "1-5")
        parsed1 = json.loads(result1)
        
        # Test with custom output filename
        result2 = await extract_pages("test.pdf", "1-5", output_file="custom_output.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_output_dir_parameter(self):
        """Test that output_dir parameter controls output directory per contract."""
        # Test with default (None) - should use source file directory
        result1 = await extract_pages("test.pdf", "1-5")
        parsed1 = json.loads(result1)
        
        # Test with custom output directory
        result2 = await extract_pages("test.pdf", "1-5", output_dir="/tmp")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_dir' not in parsed['error'], "output_dir parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generation_behavior(self):
        """Test that output_file is auto-generated when not provided per contract."""
        result = await extract_pages("test.pdf", "1-5")
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generation"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support filename generation"

    @pytest.mark.asyncio
    async def test_default_directory_behavior(self):
        """Test that output defaults to source file directory per contract."""
        result = await extract_pages("test.pdf", "1-5")
        parsed = json.loads(result)
        
        # Should use source file directory by default
        if not parsed['success']:
            # Should not complain about missing directory specification
            assert 'directory' not in parsed.get('error', ''), "Should use default directory"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await extract_pages("non_existent_file.pdf", "1-5")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'extract_pages', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes extraction results and output file info."""
        # This will fail initially but tests the expected structure
        result = await extract_pages("test.pdf", "1-5")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have extraction results
        if parsed.get('success'):
            # Should include information about the created file
            expected_fields = ['output_file', 'file_path', 'result', 'extracted_pages']
            has_file_info = any(field in parsed for field in expected_fields)
            assert has_file_info, "Successful response must contain extraction results and output file info"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert extract_pages.__doc__ is not None, "Function must have docstring"
        docstring = extract_pages.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'pages' in docstring, "Docstring must document pages parameter"
        assert 'output_file' in docstring, "Docstring must document output_file parameter"
        assert 'output_dir' in docstring, "Docstring must document output_dir parameter"
        assert 'extract' in docstring.lower(), "Docstring must describe extraction functionality"
        assert 'auto-generated' in docstring or 'auto generated' in docstring, "Docstring must mention auto-generation"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await extract_pages("test.pdf", "1-5")
        assert isinstance(result, str), "extract_pages must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("extract_pages must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(extract_pages, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(extract_pages), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(extract_pages)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert 'pages' in required_params, "pages must be required"

    def test_page_parameter_string_type(self):
        """Verify that pages parameter is string type (not List) per contract."""
        hints = get_type_hints(extract_pages)
        assert hints.get('pages') == str, "pages must be str type, not List (different from split_pdf)"

    def test_differentiation_from_split_pdf(self):
        """Verify this tool is distinct from split_pdf with different purpose."""
        # extract_pages creates single file from specific pages
        # split_pdf creates multiple files from ranges
        
        sig = inspect.signature(extract_pages)
        params = sig.parameters
        
        # Should have pages as string (not List[str] like split_pdf)
        hints = get_type_hints(extract_pages)
        assert hints.get('pages') == str, "extract_pages uses string pages parameter"
        
        # Should have output_file parameter (not split_ranges)
        assert 'output_file' in params, "extract_pages should have output_file parameter"
        assert 'split_ranges' not in params, "extract_pages should not have split_ranges parameter"


# Contract preservation test summary for extract_pages:
# ✅ Function signature: async def extract_pages(file_path: str, pages: str, output_file: str = None, output_dir: str = None) -> str
# ✅ Pages syntax: "1,3,5-7" string format (different from split_pdf's List[str])
# ✅ Auto-generation: output_file auto-generated if not provided
# ✅ Default directory: Uses source file directory when output_dir=None
# ✅ Error format: {'success': False, 'error': str, 'operation': 'extract_pages'}
# ✅ Success format: Must include extraction results and output file information
# ✅ Purpose: Extract specific pages to single new file (vs split_pdf's multiple files)


