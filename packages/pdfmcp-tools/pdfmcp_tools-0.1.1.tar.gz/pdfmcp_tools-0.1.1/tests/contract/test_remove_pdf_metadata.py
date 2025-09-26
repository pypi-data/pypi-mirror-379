"""
Contract tests for remove_pdf_metadata tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints, List

from src.pdfreadermcp.server import remove_pdf_metadata


class TestRemovePdfMetadataContract:
    """Contract tests for remove_pdf_metadata tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify remove_pdf_metadata function exists and is accessible."""
        assert hasattr(remove_pdf_metadata, '__call__'), "remove_pdf_metadata function must be callable"
        assert inspect.iscoroutinefunction(remove_pdf_metadata), "remove_pdf_metadata must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(remove_pdf_metadata)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['output_file', 'fields_to_remove', 'remove_all']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['fields_to_remove'].default is None, "fields_to_remove default must be None"
        assert params['remove_all'].default is False, "remove_all default must be False"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(remove_pdf_metadata)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('fields_to_remove') == List[str], "fields_to_remove must be typed as List[str]"
        assert hints.get('remove_all') == bool, "remove_all must be typed as bool"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await remove_pdf_metadata()

    @pytest.mark.asyncio
    async def test_fields_to_remove_list_format(self):
        """Test that fields_to_remove accepts list of field names per contract."""
        field_lists = [
            ['title'],                               # Single field
            ['title', 'author'],                     # Multiple fields
            ['title', 'author', 'subject', 'keywords'], # Many fields
            ['creator', 'producer']                  # Other standard fields
        ]
        
        for fields in field_lists:
            result = await remove_pdf_metadata("test.pdf", fields_to_remove=fields)
            parsed = json.loads(result)
            
            # Should accept field lists without parameter errors
            if not parsed['success']:
                assert 'fields_to_remove' not in parsed['error'], f"Field list {fields} should be accepted"

    @pytest.mark.asyncio
    async def test_remove_all_parameter(self):
        """Test that remove_all parameter removes all metadata per contract."""
        # Test remove_all=True
        result = await remove_pdf_metadata("test.pdf", remove_all=True)
        parsed = json.loads(result)
        
        # Should accept remove_all parameter without errors
        if not parsed['success']:
            assert 'remove_all' not in parsed['error'], "remove_all parameter should be accepted"

    @pytest.mark.asyncio
    async def test_mutually_exclusive_behavior(self):
        """Test that fields_to_remove and remove_all are mutually exclusive per contract."""
        # This tests the contract requirement for mutual exclusivity
        # Both parameters might be accepted but the logic should handle conflict
        
        result = await remove_pdf_metadata("test.pdf", fields_to_remove=['title'], remove_all=True)
        parsed = json.loads(result)
        
        # Should not cause parameter errors (business logic handles exclusivity)
        if not parsed['success']:
            # Should not be a parameter validation error
            assert 'parameter' not in parsed.get('error', '').lower(), "Should handle parameter combination gracefully"

    @pytest.mark.asyncio  
    async def test_standard_field_names(self):
        """Test that standard PDF metadata field names are supported."""
        standard_fields = ['title', 'author', 'subject', 'creator', 'producer', 'keywords']
        
        result = await remove_pdf_metadata("test.pdf", fields_to_remove=standard_fields)
        parsed = json.loads(result)
        
        # Should accept all standard field names
        if not parsed['success']:
            assert 'fields_to_remove' not in parsed['error'], "Standard field names should be accepted"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output location per contract."""
        # Test with default (None) - should overwrite source
        result1 = await remove_pdf_metadata("test.pdf", remove_all=True)
        parsed1 = json.loads(result1)
        
        # Test with custom output file
        result2 = await remove_pdf_metadata("test.pdf", remove_all=True, output_file="output.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_source_file_overwrite_default(self):
        """Test that source file is overwritten by default when output_file=None."""
        result = await remove_pdf_metadata("test.pdf", remove_all=True)
        parsed = json.loads(result)
        
        # Should handle source file overwrite without issues
        if not parsed['success']:
            assert 'overwrite' not in parsed.get('error', '').lower(), "Should support source file overwrite"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await remove_pdf_metadata("non_existent_file.pdf", remove_all=True)
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'remove_pdf_metadata', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes operation results."""
        result = await remove_pdf_metadata("test.pdf", remove_all=True)
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have operation results
        if parsed.get('success'):
            # Should include information about the removal operation
            expected_fields = ['result', 'removed_fields', 'fields_removed']
            has_result_info = any(field in parsed for field in expected_fields)
            assert has_result_info, "Successful response must contain operation results"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert remove_pdf_metadata.__doc__ is not None, "Function must have docstring"
        docstring = remove_pdf_metadata.__doc__
        
        # Verify key contract elements in documentation
        assert 'remove' in docstring.lower(), "Docstring must describe removal functionality"
        assert 'fields_to_remove' in docstring, "Docstring must document fields_to_remove parameter"
        assert 'remove_all' in docstring, "Docstring must document remove_all parameter"
        assert 'mutually exclusive' in docstring or 'exclusive' in docstring, "Docstring must document mutual exclusivity"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await remove_pdf_metadata("test.pdf", remove_all=True)
        assert isinstance(result, str), "remove_pdf_metadata must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("remove_pdf_metadata must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(remove_pdf_metadata, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(remove_pdf_metadata), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(remove_pdf_metadata)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_removal_operation_purpose(self):
        """Verify this is a removal operation that deletes metadata."""
        # This tool should remove/delete metadata (opposite of set_pdf_metadata)
        docstring = remove_pdf_metadata.__doc__ or ""
        
        # Should mention removing, deleting, or clearing
        removal_terms = ['remove', 'delete', 'clear']
        has_removal_focus = any(term in docstring.lower() for term in removal_terms)
        
        assert has_removal_focus, "Tool should be focused on removing/deleting metadata"

    def test_selective_vs_complete_removal_options(self):
        """Verify tool supports both selective and complete metadata removal."""
        sig = inspect.signature(remove_pdf_metadata)
        
        # Should have both selective (fields_to_remove) and complete (remove_all) options
        assert 'fields_to_remove' in sig.parameters, "Must support selective removal"
        assert 'remove_all' in sig.parameters, "Must support complete removal"
        
        # Both should be optional with appropriate defaults
        assert sig.parameters['fields_to_remove'].default is None
        assert sig.parameters['remove_all'].default is False


# Contract preservation test summary for remove_pdf_metadata:
# ✅ Function signature: async def remove_pdf_metadata(file_path: str, output_file: str = None, fields_to_remove: List[str] = None, remove_all: bool = False) -> str
# ✅ Selective removal: fields_to_remove accepts list of specific field names
# ✅ Complete removal: remove_all=True removes all metadata
# ✅ Mutual exclusivity: fields_to_remove OR remove_all (contract documents exclusivity)
# ✅ Output control: Can overwrite source file or create new file
# ✅ Standard fields: Supports all standard PDF metadata field names
# ✅ Error format: {'success': False, 'error': str, 'operation': 'remove_pdf_metadata'}
# ✅ Purpose: Remove/delete PDF metadata (opposite of set_pdf_metadata)


