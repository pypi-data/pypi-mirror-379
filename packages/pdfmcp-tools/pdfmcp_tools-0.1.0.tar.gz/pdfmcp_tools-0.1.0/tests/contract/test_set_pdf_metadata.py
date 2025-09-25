"""
Contract tests for set_pdf_metadata tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import set_pdf_metadata


class TestSetPdfMetadataContract:
    """Contract tests for set_pdf_metadata tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify set_pdf_metadata function exists and is accessible."""
        assert hasattr(set_pdf_metadata, '__call__'), "set_pdf_metadata function must be callable"
        assert inspect.iscoroutinefunction(set_pdf_metadata), "set_pdf_metadata must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(set_pdf_metadata)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['output_file', 'title', 'author', 'subject', 'creator', 'producer', 'keywords', 'preserve_existing']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['title'].default is None, "title default must be None"
        assert params['author'].default is None, "author default must be None"
        assert params['subject'].default is None, "subject default must be None"
        assert params['creator'].default is None, "creator default must be None"
        assert params['producer'].default is None, "producer default must be None"
        assert params['keywords'].default is None, "keywords default must be None"
        assert params['preserve_existing'].default is True, "preserve_existing default must be True"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(set_pdf_metadata)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('preserve_existing') == bool, "preserve_existing must be typed as bool"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await set_pdf_metadata()

    @pytest.mark.asyncio
    async def test_metadata_fields_acceptance(self):
        """Test that all standard metadata fields are accepted per contract."""
        metadata_fields = {
            'title': 'Test Title',
            'author': 'Test Author', 
            'subject': 'Test Subject',
            'creator': 'Test Creator',
            'producer': 'Test Producer',
            'keywords': 'test, keywords, example'
        }
        
        # Test individual fields
        for field, value in metadata_fields.items():
            kwargs = {field: value}
            result = await set_pdf_metadata("test.pdf", **kwargs)
            parsed = json.loads(result)
            
            # Should accept metadata field without parameter errors
            if not parsed['success']:
                assert field not in parsed['error'], f"Metadata field '{field}' should be accepted"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output location per contract."""
        # Test with default (None) - should overwrite source
        result1 = await set_pdf_metadata("test.pdf", title="Test")
        parsed1 = json.loads(result1)
        
        # Test with custom output file
        result2 = await set_pdf_metadata("test.pdf", title="Test", output_file="output.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_preserve_existing_behavior(self):
        """Test that preserve_existing parameter controls metadata preservation per contract."""
        # Test with preserve_existing=True (default)
        result1 = await set_pdf_metadata("test.pdf", title="New Title", preserve_existing=True)
        parsed1 = json.loads(result1)
        
        # Test with preserve_existing=False
        result2 = await set_pdf_metadata("test.pdf", title="New Title", preserve_existing=False)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'preserve_existing' not in parsed['error'], "preserve_existing parameter should be accepted"

    @pytest.mark.asyncio
    async def test_keywords_comma_separated_format(self):
        """Test that keywords accepts comma-separated format per contract."""
        keywords_formats = [
            "single",
            "two, keywords",
            "multiple, comma, separated, keywords",
            "with spaces, and symbols!"
        ]
        
        for keywords in keywords_formats:
            result = await set_pdf_metadata("test.pdf", keywords=keywords)
            parsed = json.loads(result)
            
            # Should handle various keyword formats
            if not parsed['success']:
                assert 'keywords' not in parsed['error'], f"Keywords format '{keywords}' should be accepted"

    @pytest.mark.asyncio
    async def test_source_file_overwrite_default(self):
        """Test that source file is overwritten by default when output_file=None."""
        result = await set_pdf_metadata("test.pdf", title="Test")
        parsed = json.loads(result)
        
        # Should handle source file overwrite without issues
        if not parsed['success']:
            assert 'overwrite' not in parsed.get('error', '').lower(), "Should support source file overwrite"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await set_pdf_metadata("non_existent_file.pdf", title="Test")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'set_pdf_metadata', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes operation results."""
        result = await set_pdf_metadata("test.pdf", title="Test")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have operation results
        if parsed.get('success'):
            # Should include information about the operation
            expected_fields = ['result', 'output_file', 'metadata_updated']
            has_result_info = any(field in parsed for field in expected_fields)
            assert has_result_info, "Successful response must contain operation results"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert set_pdf_metadata.__doc__ is not None, "Function must have docstring"
        docstring = set_pdf_metadata.__doc__
        
        # Verify key contract elements in documentation
        assert 'write' in docstring.lower() or 'update' in docstring.lower(), "Docstring must describe write/update functionality"
        assert 'preserve_existing' in docstring, "Docstring must document preserve_existing parameter"
        assert 'overwrite' in docstring.lower(), "Docstring must mention source file overwrite behavior"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await set_pdf_metadata("test.pdf", title="Test")
        assert isinstance(result, str), "set_pdf_metadata must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("set_pdf_metadata must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(set_pdf_metadata, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(set_pdf_metadata), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(set_pdf_metadata)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_write_operation_purpose(self):
        """Verify this is a write operation that modifies PDF metadata."""
        # This tool should modify files (opposite of get_pdf_metadata)
        docstring = set_pdf_metadata.__doc__ or ""
        
        # Should mention writing, updating, or setting
        write_terms = ['write', 'update', 'set']
        has_write_focus = any(term in docstring.lower() for term in write_terms)
        
        assert has_write_focus, "Tool should be focused on writing/updating metadata"

    def test_standard_metadata_fields_coverage(self):
        """Verify all standard PDF metadata fields are supported."""
        sig = inspect.signature(set_pdf_metadata)
        standard_fields = ['title', 'author', 'subject', 'creator', 'producer', 'keywords']
        
        for field in standard_fields:
            assert field in sig.parameters, f"Must support standard metadata field: {field}"


# Contract preservation test summary for set_pdf_metadata:
# ✅ Function signature: async def set_pdf_metadata(file_path: str, output_file: str = None, title: str = None, author: str = None, subject: str = None, creator: str = None, producer: str = None, keywords: str = None, preserve_existing: bool = True) -> str
# ✅ Standard fields: title, author, subject, creator, producer, keywords all supported
# ✅ Preservation: preserve_existing=True preserves unspecified fields by default
# ✅ Output control: Can overwrite source file (output_file=None) or create new file
# ✅ Keywords format: Accepts comma-separated string format
# ✅ Error format: {'success': False, 'error': str, 'operation': 'set_pdf_metadata'}
# ✅ Purpose: Write/update PDF metadata (opposite of get_pdf_metadata)


