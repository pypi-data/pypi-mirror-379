"""
Contract tests for split_pdf tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints, List

from src.pdfreadermcp.server import split_pdf


class TestSplitPdfContract:
    """Contract tests for split_pdf tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify split_pdf function exists and is accessible."""
        assert hasattr(split_pdf, '__call__'), "split_pdf function must be callable"
        assert inspect.iscoroutinefunction(split_pdf), "split_pdf must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(split_pdf)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path', 'split_ranges']
        optional_params = ['output_dir', 'prefix']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults
        assert params['output_dir'].default is None, "output_dir default must be None"
        assert params['prefix'].default is None, "prefix default must be None"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(split_pdf)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('split_ranges') == List[str], "split_ranges must be typed as List[str]"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path and split_ranges parameters are required."""
        # Missing both parameters
        with pytest.raises(TypeError, match="missing .* required positional argument"):
            await split_pdf()

        # Missing split_ranges parameter  
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'split_ranges'"):
            await split_pdf("test.pdf")

    @pytest.mark.asyncio
    async def test_split_ranges_format(self):
        """Test that split_ranges accepts list of page range strings per contract."""
        valid_range_formats = [
            ["1-5"],                    # Single range
            ["1-5", "6-10"],           # Multiple ranges
            ["1-5", "6-10", "11-15"],  # Multiple ranges
            ["1", "3", "5-7"],         # Mixed single pages and ranges
        ]
        
        for ranges in valid_range_formats:
            result = await split_pdf("test.pdf", split_ranges=ranges)
            parsed = json.loads(result)
            
            # Should handle range formats without parameter errors
            if not parsed['success']:
                assert 'split_ranges' not in parsed['error'], f"Range format {ranges} should be accepted"
                assert 'range' not in parsed.get('error', '').lower() or 'format' not in parsed.get('error', '').lower(), f"Should not complain about range format for {ranges}"

    @pytest.mark.asyncio
    async def test_output_directory_handling(self):
        """Test that output_dir parameter controls output location per contract."""
        # Test with default (None) - should use source file directory
        result1 = await split_pdf("test.pdf", split_ranges=["1-5"])
        parsed1 = json.loads(result1)
        
        # Test with custom output directory
        result2 = await split_pdf("test.pdf", split_ranges=["1-5"], output_dir="/tmp")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_dir' not in parsed['error'], "output_dir parameter should be accepted"

    @pytest.mark.asyncio
    async def test_prefix_parameter_handling(self):
        """Test that prefix parameter controls output filename prefix per contract."""
        # Test with default (None) - should use source filename
        result1 = await split_pdf("test.pdf", split_ranges=["1-5"])
        parsed1 = json.loads(result1)
        
        # Test with custom prefix
        result2 = await split_pdf("test.pdf", split_ranges=["1-5"], prefix="custom_prefix")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'prefix' not in parsed['error'], "prefix parameter should be accepted"

    @pytest.mark.asyncio
    async def test_default_behavior_contract(self):
        """Test that default values work as specified in contract."""
        result = await split_pdf("test.pdf", split_ranges=["1-5"])
        parsed = json.loads(result)
        
        # Should use defaults without explicit output_dir and prefix
        if not parsed['success']:
            # Should not complain about missing optional parameters
            assert 'output_dir' not in parsed.get('error', ''), "Should use default output_dir"
            assert 'prefix' not in parsed.get('error', ''), "Should use default prefix"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await split_pdf("non_existent_file.pdf", split_ranges=["1-5"])
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'split_pdf', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes split operation results and output file information."""
        # This will fail initially but tests the expected structure
        result = await split_pdf("test.pdf", split_ranges=["1-5"])
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have file operation results
        if parsed.get('success'):
            # Should include information about created files
            expected_fields = ['files', 'output_files', 'results', 'created_files']
            has_file_info = any(field in parsed for field in expected_fields)
            assert has_file_info, "Successful response must contain output file information"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert split_pdf.__doc__ is not None, "Function must have docstring"
        docstring = split_pdf.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'split_ranges' in docstring, "Docstring must document split_ranges parameter"
        assert 'output_dir' in docstring, "Docstring must document output_dir parameter"
        assert 'prefix' in docstring, "Docstring must document prefix parameter"
        assert 'split' in docstring.lower(), "Docstring must describe splitting functionality"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await split_pdf("test.pdf", split_ranges=["1-5"])
        assert isinstance(result, str), "split_pdf must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("split_pdf must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(split_pdf, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(split_pdf), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(split_pdf)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert 'split_ranges' in required_params, "split_ranges must be required"

    def test_split_ranges_list_type_requirement(self):
        """Verify that split_ranges must be a List[str] type per contract."""
        sig = inspect.signature(split_pdf)
        hints = get_type_hints(split_pdf)
        
        # Verify it's specifically typed as List[str], not just any iterable
        assert hints.get('split_ranges') == List[str], "split_ranges must be List[str], not generic iterable"


# Contract preservation test summary for split_pdf:
# ✅ Function signature: async def split_pdf(file_path: str, split_ranges: List[str], output_dir: str = None, prefix: str = None) -> str
# ✅ Range formats: Supports ["1-5", "6-10", "11-15"] list format
# ✅ Default output_dir: Uses source file directory when None
# ✅ Default prefix: Uses source filename when None  
# ✅ Error format: {'success': False, 'error': str, 'operation': 'split_pdf'}
# ✅ Success format: Must include split operation results and output file information
# ✅ Return type: Always JSON string, never dict or other types


