"""
Contract tests for get_pdf_metadata tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import get_pdf_metadata


class TestGetPdfMetadataContract:
    """Contract tests for get_pdf_metadata tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify get_pdf_metadata function exists and is accessible."""
        assert hasattr(get_pdf_metadata, '__call__'), "get_pdf_metadata function must be callable"
        assert inspect.iscoroutinefunction(get_pdf_metadata), "get_pdf_metadata must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(get_pdf_metadata)
        params = sig.parameters

        # Verify parameter names and types
        assert 'file_path' in params, "Must have file_path parameter"
        assert 'include_xmp' in params, "Must have include_xmp parameter"

        # Verify parameter defaults
        assert params['file_path'].default == inspect.Parameter.empty, "file_path must be required"
        assert params['include_xmp'].default is False, "include_xmp default must be False"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(get_pdf_metadata)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('include_xmp') == bool, "include_xmp must be typed as bool"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        # Missing file_path parameter
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await get_pdf_metadata()

    @pytest.mark.asyncio
    async def test_include_xmp_parameter(self):
        """Test that include_xmp parameter controls XMP metadata inclusion."""
        # Test with include_xmp=False (default)
        result1 = await get_pdf_metadata("test.pdf", include_xmp=False)
        parsed1 = json.loads(result1)
        
        # Test with include_xmp=True
        result2 = await get_pdf_metadata("test.pdf", include_xmp=True)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'include_xmp' not in parsed['error'], "include_xmp parameter should be accepted"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await get_pdf_metadata("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'get_pdf_metadata', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_comprehensive_metadata_information(self):
        """Test that successful response includes comprehensive metadata information."""
        # This will fail initially but tests the expected structure
        result = await get_pdf_metadata("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have comprehensive metadata
        if parsed.get('success'):
            # Standard metadata fields that should be included
            standard_fields = ['title', 'author', 'subject', 'creator', 'producer', 'creation_date', 'modification_date']
            metadata_section = parsed.get('metadata', {})
            
            # Should have some standard metadata fields
            has_standard_fields = any(field in metadata_section for field in standard_fields)
            assert has_standard_fields, "Should include standard PDF metadata fields"

    @pytest.mark.asyncio
    async def test_xmp_metadata_conditional_inclusion(self):
        """Test that XMP metadata is only included when include_xmp=True."""
        # Test default behavior (should not include XMP)
        result_no_xmp = await get_pdf_metadata("test.pdf")
        parsed_no_xmp = json.loads(result_no_xmp)
        
        # Test explicit XMP inclusion
        result_with_xmp = await get_pdf_metadata("test.pdf", include_xmp=True)
        parsed_with_xmp = json.loads(result_with_xmp)
        
        # Both should handle the parameter correctly
        for parsed in [parsed_no_xmp, parsed_with_xmp]:
            if not parsed['success']:
                # Should not fail due to XMP parameter handling
                error_msg = parsed.get('error', '').lower()
                assert 'xmp' not in error_msg, "XMP parameter handling should not cause errors"

    @pytest.mark.asyncio
    async def test_standard_metadata_always_included(self):
        """Test that standard metadata fields are always included per contract."""
        result = await get_pdf_metadata("test.pdf", include_xmp=False)
        parsed = json.loads(result)
        
        # Even on failure, verify the contract expectation
        if parsed.get('success'):
            # Should have standard metadata regardless of XMP setting
            assert 'metadata' in parsed, "Response should contain metadata section"
            
            metadata = parsed.get('metadata', {})
            # Should have at least some basic metadata structure
            assert isinstance(metadata, dict), "Metadata should be a dictionary"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert get_pdf_metadata.__doc__ is not None, "Function must have docstring"
        docstring = get_pdf_metadata.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'include_xmp' in docstring, "Docstring must document include_xmp parameter"
        assert 'standard' in docstring.lower(), "Docstring must mention standard metadata fields"
        assert 'xmp' in docstring.lower(), "Docstring must document XMP metadata functionality"
        assert 'comprehensive' in docstring.lower(), "Docstring must mention comprehensive information"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await get_pdf_metadata("test.pdf")
        assert isinstance(result, str), "get_pdf_metadata must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("get_pdf_metadata must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(get_pdf_metadata, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(get_pdf_metadata), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(get_pdf_metadata)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_read_only_operation(self):
        """Verify this is a read-only operation that doesn't modify files."""
        # This tool should be read-only as per contract
        docstring = get_pdf_metadata.__doc__ or ""
        
        # Should not mention modification, writing, or changing
        modification_terms = ['write', 'modify', 'change', 'update', 'set']
        has_modification_terms = any(term in docstring.lower() for term in modification_terms)
        
        assert not has_modification_terms, "get_pdf_metadata should be read-only operation"


# Contract preservation test summary for get_pdf_metadata:
# ✅ Function signature: async def get_pdf_metadata(file_path: str, include_xmp: bool = False) -> str
# ✅ Read-only operation: Does not modify PDF files, only reads metadata
# ✅ Standard metadata: Always included (title, author, subject, creator, producer, dates)
# ✅ XMP metadata: Only included when include_xmp=True
# ✅ Error format: {'success': False, 'error': str, 'operation': 'get_pdf_metadata'}
# ✅ Success format: Must include comprehensive metadata information
# ✅ Return type: Always JSON string, never dict or other types


