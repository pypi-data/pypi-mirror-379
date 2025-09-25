"""
Contract tests for read_pdf tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from unittest.mock import AsyncMock, patch
from typing import get_type_hints

# Import the server module to test the actual tool functions
from src.pdfreadermcp.server import read_pdf


class TestReadPDFContract:
    """Contract tests for read_pdf tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify read_pdf function exists and is accessible."""
        assert hasattr(read_pdf, '__call__'), "read_pdf function must be callable"
        assert inspect.iscoroutinefunction(read_pdf), "read_pdf must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(read_pdf)
        params = sig.parameters

        # Verify parameter names and types
        assert 'file_path' in params, "Must have file_path parameter"
        assert 'pages' in params, "Must have pages parameter"
        assert 'chunk_size' in params, "Must have chunk_size parameter"  
        assert 'chunk_overlap' in params, "Must have chunk_overlap parameter"

        # Verify parameter defaults
        assert params['pages'].default is None, "pages default must be None"
        assert params['chunk_size'].default == 1000, "chunk_size default must be 1000"
        assert params['chunk_overlap'].default == 100, "chunk_overlap default must be 100"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(read_pdf)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_parameter_validation_file_path_required(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await read_pdf()

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        # This should fail initially - testing with non-existent file
        result = await read_pdf("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"  
        assert 'extraction_method' in parsed, "Error response must contain 'extraction_method' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['extraction_method'] == 'text_extraction', "Must specify extraction method"

    @pytest.mark.asyncio
    async def test_page_range_syntax_support(self):
        """Test that page range syntax is supported per contract."""
        # Test various page range formats (these will fail initially)
        test_cases = [
            "1",           # Single page
            "1,3,5",       # Multiple pages  
            "1-10",        # Range
            "-1",          # Last page
            "1,3,5-10,-1"  # Combined syntax
        ]
        
        for pages in test_cases:
            result = await read_pdf("test.pdf", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            # (Will fail for file not found, but not for parameter issues)
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_chunk_parameters_accepted(self):
        """Test that chunking parameters are accepted."""
        result = await read_pdf("test.pdf", chunk_size=500, chunk_overlap=50)
        parsed = json.loads(result)
        
        # Should accept chunk parameters without error (file not found is expected)
        if not parsed['success']:
            assert 'chunk_size' not in parsed['error'], "chunk_size parameter should be accepted"
            assert 'chunk_overlap' not in parsed['error'], "chunk_overlap parameter should be accepted"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert read_pdf.__doc__ is not None, "Function must have docstring"
        docstring = read_pdf.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'pages' in docstring, "Docstring must document pages parameter" 
        assert 'chunk_size' in docstring, "Docstring must document chunk_size parameter"
        assert 'chunk_overlap' in docstring, "Docstring must document chunk_overlap parameter"
        assert 'JSON string' in docstring, "Docstring must specify JSON string return"

    @pytest.mark.asyncio 
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await read_pdf("test.pdf")
        assert isinstance(result, str), "read_pdf must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("read_pdf must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        # Check that function has attributes expected by FastMCP
        assert hasattr(read_pdf, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(read_pdf), "Must be async for FastMCP tools"
        
        # Verify signature is compatible with FastMCP parameter passing
        sig = inspect.signature(read_pdf)
        for param_name, param in sig.parameters.items():
            if param.default == inspect.Parameter.empty:
                assert param_name == 'file_path', f"Only file_path should be required parameter, but {param_name} is required"


# Contract preservation test summary for read_pdf:
# ✅ Function signature: async def read_pdf(file_path: str, pages: str = None, chunk_size: int = 1000, chunk_overlap: int = 100) -> str
# ✅ Error format: {'success': False, 'error': str, 'extraction_method': 'text_extraction'}
# ✅ Page range syntax: "1,3,5-10,-1" format supported
# ✅ Return type: Always JSON string, never dict or other types
# ✅ FastMCP compatibility: Async function with proper parameter handling


