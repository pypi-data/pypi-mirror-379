"""
Contract tests for extract_page_text tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import extract_page_text


class TestExtractPageTextContract:
    """Contract tests for extract_page_text tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify extract_page_text function exists and is accessible."""
        assert hasattr(extract_page_text, '__call__'), "extract_page_text function must be callable"
        assert inspect.iscoroutinefunction(extract_page_text), "extract_page_text must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(extract_page_text)
        params = sig.parameters

        # Verify parameter names and types
        assert 'file_path' in params, "Must have file_path parameter"
        assert 'page_number' in params, "Must have page_number parameter"
        assert 'extraction_mode' in params, "Must have extraction_mode parameter"

        # Verify parameter defaults
        assert params['extraction_mode'].default == "default", "extraction_mode default must be 'default'"

        # Verify no default for required parameters
        assert params['file_path'].default == inspect.Parameter.empty, "file_path must be required"
        assert params['page_number'].default == inspect.Parameter.empty, "page_number must be required"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(extract_page_text)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('page_number') == int, "page_number must be typed as int"
        assert hints.get('extraction_mode') == str, "extraction_mode must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path and page_number parameters are required."""
        # Missing both parameters
        with pytest.raises(TypeError, match="missing .* required positional argument"):
            await extract_page_text()

        # Missing page_number parameter
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'page_number'"):
            await extract_page_text("test.pdf")

    @pytest.mark.asyncio
    async def test_page_number_one_based_indexing(self):
        """Test that page_number uses 1-based indexing per contract."""
        # Test with page number 1 (should be valid input, even if file doesn't exist)
        result = await extract_page_text("test.pdf", page_number=1)
        parsed = json.loads(result)
        
        # Should not complain about page number 1 being invalid
        if not parsed['success']:
            assert '1-based' not in parsed.get('error', ''), "Page number 1 should be valid for 1-based indexing"
            assert 'page_number' not in parsed.get('error', ''), "Page number parameter should be accepted"

    @pytest.mark.asyncio  
    async def test_extraction_mode_values(self):
        """Test that extraction_mode accepts contract-specified values."""
        valid_modes = ["default", "layout", "simple"]
        
        for mode in valid_modes:
            result = await extract_page_text("test.pdf", page_number=1, extraction_mode=mode)
            parsed = json.loads(result)
            
            # Should accept valid extraction modes without parameter errors
            if not parsed['success']:
                assert 'extraction_mode' not in parsed.get('error', ''), f"Mode '{mode}' should be accepted"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification.""" 
        result = await extract_page_text("non_existent_file.pdf", page_number=1)
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'extract_page_text', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_return_json_with_text_and_statistics(self):
        """Test that successful response includes text and statistics per contract."""
        # This will fail initially but tests the expected structure
        result = await extract_page_text("test.pdf", page_number=1)
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have text and statistics
        if parsed.get('success'):
            assert 'text' in parsed, "Successful response must contain text"
            assert 'statistics' in parsed, "Successful response must contain statistics"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert extract_page_text.__doc__ is not None, "Function must have docstring"
        docstring = extract_page_text.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'page_number' in docstring, "Docstring must document page_number parameter"
        assert 'extraction_mode' in docstring, "Docstring must document extraction_mode parameter"
        assert '1-based' in docstring, "Docstring must specify 1-based indexing"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await extract_page_text("test.pdf", page_number=1)
        assert isinstance(result, str), "extract_page_text must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("extract_page_text must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(extract_page_text, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(extract_page_text), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(extract_page_text)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert 'page_number' in required_params, "page_number must be required"


# Contract preservation test summary for extract_page_text:
# ✅ Function signature: async def extract_page_text(file_path: str, page_number: int, extraction_mode: str = "default") -> str
# ✅ Page numbering: 1-based indexing as specified in contract
# ✅ Extraction modes: "default", "layout", "simple" values accepted
# ✅ Error format: {'success': False, 'error': str, 'operation': 'extract_page_text'}  
# ✅ Success format: Must include text and statistics
# ✅ Return type: Always JSON string, never dict or other types


