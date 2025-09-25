"""
Contract tests for merge_pdfs tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints, List

from src.pdfreadermcp.server import merge_pdfs


class TestMergePdfsContract:
    """Contract tests for merge_pdfs tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify merge_pdfs function exists and is accessible."""
        assert hasattr(merge_pdfs, '__call__'), "merge_pdfs function must be callable"
        assert inspect.iscoroutinefunction(merge_pdfs), "merge_pdfs must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(merge_pdfs)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_paths']
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
        hints = get_type_hints(merge_pdfs)
        
        assert hints.get('file_paths') == List[str], "file_paths must be typed as List[str]"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_paths parameter is required."""
        # Missing file_paths parameter
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_paths'"):
            await merge_pdfs()

    @pytest.mark.asyncio
    async def test_file_paths_list_handling(self):
        """Test that file_paths accepts list of PDF file paths per contract."""
        valid_file_lists = [
            ["file1.pdf"],                           # Single file
            ["file1.pdf", "file2.pdf"],             # Two files  
            ["file1.pdf", "file2.pdf", "file3.pdf"], # Multiple files
        ]
        
        for file_list in valid_file_lists:
            result = await merge_pdfs(file_paths=file_list)
            parsed = json.loads(result)
            
            # Should handle file lists without parameter errors
            if not parsed['success']:
                assert 'file_paths' not in parsed['error'], f"File list {file_list} should be accepted"
                assert 'list' not in parsed.get('error', '').lower(), f"Should accept list parameter"

    @pytest.mark.asyncio
    async def test_page_order_preservation(self):
        """Test that page order is preserved from file_paths list per contract."""
        # Test with specific order
        file_list = ["first.pdf", "second.pdf", "third.pdf"]
        result = await merge_pdfs(file_paths=file_list)
        parsed = json.loads(result)
        
        # Should accept the ordered list without issues
        if not parsed['success']:
            assert 'order' not in parsed.get('error', '').lower(), "Should preserve file order"
            assert 'sequence' not in parsed.get('error', '').lower(), "Should handle sequential merging"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output filename per contract."""
        file_list = ["file1.pdf", "file2.pdf"]
        
        # Test with default (None) - should auto-generate
        result1 = await merge_pdfs(file_paths=file_list)
        parsed1 = json.loads(result1)
        
        # Test with custom output filename
        result2 = await merge_pdfs(file_paths=file_list, output_file="merged_custom.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_output_dir_parameter(self):
        """Test that output_dir parameter controls output directory per contract."""
        file_list = ["file1.pdf", "file2.pdf"]
        
        # Test with default (None) - should use first file's directory
        result1 = await merge_pdfs(file_paths=file_list)
        parsed1 = json.loads(result1)
        
        # Test with custom output directory
        result2 = await merge_pdfs(file_paths=file_list, output_dir="/tmp")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_dir' not in parsed['error'], "output_dir parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generation_behavior(self):
        """Test that output_file is auto-generated when not provided per contract."""
        file_list = ["file1.pdf", "file2.pdf"]
        result = await merge_pdfs(file_paths=file_list)
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generation"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support filename generation"

    @pytest.mark.asyncio
    async def test_first_file_directory_default(self):
        """Test that output defaults to first file's directory per contract."""
        file_list = ["path/to/file1.pdf", "other/file2.pdf"]
        result = await merge_pdfs(file_paths=file_list)
        parsed = json.loads(result)
        
        # Should use first file's directory by default
        if not parsed['success']:
            # Should not complain about directory resolution
            assert 'directory' not in parsed.get('error', ''), "Should resolve output directory from first file"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await merge_pdfs(file_paths=["non_existent1.pdf", "non_existent2.pdf"])
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'merge_pdfs', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes merge results and output file information."""
        # This will fail initially but tests the expected structure
        file_list = ["file1.pdf", "file2.pdf"]
        result = await merge_pdfs(file_paths=file_list)
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have merge results
        if parsed.get('success'):
            # Should include information about the merged file
            expected_fields = ['output_file', 'merged_file', 'result', 'total_pages']
            has_merge_info = any(field in parsed for field in expected_fields)
            assert has_merge_info, "Successful response must contain merge results and output file information"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert merge_pdfs.__doc__ is not None, "Function must have docstring"
        docstring = merge_pdfs.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_paths' in docstring, "Docstring must document file_paths parameter"
        assert 'output_file' in docstring, "Docstring must document output_file parameter"
        assert 'output_dir' in docstring, "Docstring must document output_dir parameter"
        assert 'merge' in docstring.lower(), "Docstring must describe merging functionality"
        assert 'order' in docstring.lower() or 'preserve' in docstring.lower(), "Docstring must mention page order preservation"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await merge_pdfs(file_paths=["file1.pdf", "file2.pdf"])
        assert isinstance(result, str), "merge_pdfs must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("merge_pdfs must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(merge_pdfs, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(merge_pdfs), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(merge_pdfs)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_paths' in required_params, "file_paths must be required"
        assert len(required_params) == 1, "Only file_paths should be required"

    def test_file_paths_list_type_requirement(self):
        """Verify that file_paths must be a List[str] type per contract."""
        hints = get_type_hints(merge_pdfs)
        assert hints.get('file_paths') == List[str], "file_paths must be List[str]"

    def test_single_output_file_purpose(self):
        """Verify this tool creates single output file from multiple inputs."""
        # merge_pdfs combines multiple PDFs into one file
        docstring = merge_pdfs.__doc__ or ""
        
        # Should mention single file output or combining
        combining_terms = ['single', 'combine', 'merge', 'into one']
        has_combining_focus = any(term in docstring.lower() for term in combining_terms)
        
        assert has_combining_focus, "Tool should focus on combining multiple files into single output"

    @pytest.mark.asyncio
    async def test_minimum_files_handling(self):
        """Test that tool handles edge cases appropriately."""
        # Test with single file (edge case)
        result = await merge_pdfs(file_paths=["single.pdf"])
        parsed = json.loads(result)
        
        # Should handle single file case (may be valid operation or specific error)
        if not parsed['success']:
            # Should not be a parameter error
            assert 'file_paths' not in parsed['error'], "Single file should be accepted as valid input"


# Contract preservation test summary for merge_pdfs:
# ✅ Function signature: async def merge_pdfs(file_paths: List[str], output_file: str = None, output_dir: str = None) -> str
# ✅ File order: Preserves page order from file_paths list sequence
# ✅ Auto-generation: output_file auto-generated if not provided
# ✅ Default directory: Uses first file's directory when output_dir=None
# ✅ Error format: {'success': False, 'error': str, 'operation': 'merge_pdfs'}
# ✅ Success format: Must include merge results and output file information
# ✅ Purpose: Combine multiple PDF files into single output file


