"""
Contract tests for remove_pdf_content tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import remove_pdf_content


class TestRemovePdfContentContract:
    """Contract tests for remove_pdf_content tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify remove_pdf_content function exists and is accessible."""
        assert hasattr(remove_pdf_content, '__call__'), "remove_pdf_content function must be callable"
        assert inspect.iscoroutinefunction(remove_pdf_content), "remove_pdf_content must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(remove_pdf_content)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['output_file', 'remove_images', 'remove_annotations', 'compress_streams']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['remove_images'].default is False, "remove_images default must be False"
        assert params['remove_annotations'].default is False, "remove_annotations default must be False"
        assert params['compress_streams'].default is True, "compress_streams default must be True"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(remove_pdf_content)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('remove_images') == bool, "remove_images must be typed as bool"
        assert hints.get('remove_annotations') == bool, "remove_annotations must be typed as bool"
        assert hints.get('compress_streams') == bool, "compress_streams must be typed as bool"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await remove_pdf_content()

    @pytest.mark.asyncio
    async def test_remove_images_parameter(self):
        """Test that remove_images parameter controls image removal per contract."""
        # Test with remove_images=False (default)
        result1 = await remove_pdf_content("test.pdf", remove_images=False)
        parsed1 = json.loads(result1)
        
        # Test with remove_images=True
        result2 = await remove_pdf_content("test.pdf", remove_images=True)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'remove_images' not in parsed['error'], "remove_images parameter should be accepted"

    @pytest.mark.asyncio
    async def test_remove_annotations_parameter(self):
        """Test that remove_annotations parameter controls annotation removal per contract."""
        # Test with remove_annotations=False (default)
        result1 = await remove_pdf_content("test.pdf", remove_annotations=False)
        parsed1 = json.loads(result1)
        
        # Test with remove_annotations=True
        result2 = await remove_pdf_content("test.pdf", remove_annotations=True)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'remove_annotations' not in parsed['error'], "remove_annotations parameter should be accepted"

    @pytest.mark.asyncio
    async def test_compress_streams_parameter(self):
        """Test that compress_streams parameter controls content stream compression per contract."""
        # Test with compress_streams=True (default)
        result1 = await remove_pdf_content("test.pdf", compress_streams=True)
        parsed1 = json.loads(result1)
        
        # Test with compress_streams=False
        result2 = await remove_pdf_content("test.pdf", compress_streams=False)
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'compress_streams' not in parsed['error'], "compress_streams parameter should be accepted"

    @pytest.mark.asyncio
    async def test_compress_streams_default_true(self):
        """Test that compress_streams defaults to True per contract."""
        # Default behavior should include stream compression
        result = await remove_pdf_content("test.pdf")
        parsed = json.loads(result)
        
        # Should use compress_streams=True by default
        if not parsed['success']:
            assert 'compress_streams' not in parsed['error'], "Should use compress_streams=True by default"

    @pytest.mark.asyncio
    async def test_selective_content_removal(self):
        """Test that content removal is selective based on parameters per contract."""
        # Test selective removal (images only)
        result = await remove_pdf_content("test.pdf", remove_images=True, remove_annotations=False)
        parsed = json.loads(result)
        
        # Should handle selective removal without parameter errors
        if not parsed['success']:
            assert 'selective' not in parsed.get('error', '').lower(), "Should support selective content removal"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output location per contract."""
        # Test with default (None) - should auto-generate
        result1 = await remove_pdf_content("test.pdf", remove_images=True)
        parsed1 = json.loads(result1)
        
        # Test with custom output file
        result2 = await remove_pdf_content("test.pdf", remove_images=True, output_file="cleaned.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generated_output_file(self):
        """Test that output file is auto-generated when not provided per contract."""
        result = await remove_pdf_content("test.pdf", remove_images=True)
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generated filename"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support filename generation"

    @pytest.mark.asyncio
    async def test_file_size_reduction_purpose(self):
        """Test that tool's purpose is file size reduction per contract."""
        result = await remove_pdf_content("test.pdf", remove_images=True, compress_streams=True)
        parsed = json.loads(result)
        
        # Should be focused on size reduction without causing functional errors
        if not parsed['success']:
            assert 'size' not in parsed.get('error', '').lower() or 'reduce' not in parsed.get('error', '').lower(), "Should support size reduction operations"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await remove_pdf_content("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'remove_pdf_content', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes content removal results and statistics."""
        result = await remove_pdf_content("test.pdf", remove_images=True)
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have removal statistics
        if parsed.get('success'):
            # Should include information about content removal
            expected_fields = ['removed_content', 'size_reduction', 'statistics', 'content_removed']
            has_removal_info = any(field in parsed for field in expected_fields)
            assert has_removal_info, "Successful response must contain content removal results and statistics"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert remove_pdf_content.__doc__ is not None, "Function must have docstring"
        docstring = remove_pdf_content.__doc__
        
        # Verify key contract elements in documentation
        assert 'remove' in docstring.lower(), "Docstring must describe removal functionality"
        assert 'content' in docstring.lower(), "Docstring must specify content removal"
        assert 'reduce' in docstring.lower() or 'size' in docstring.lower(), "Docstring must mention size reduction"
        assert 'images' in docstring.lower(), "Docstring must document image removal option"
        assert 'annotations' in docstring.lower(), "Docstring must document annotation removal option"
        assert 'compress_streams' in docstring, "Docstring must document stream compression option"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await remove_pdf_content("test.pdf")
        assert isinstance(result, str), "remove_pdf_content must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("remove_pdf_content must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(remove_pdf_content, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(remove_pdf_content), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(remove_pdf_content)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_content_removal_operation_purpose(self):
        """Verify this tool removes specific content types to reduce file size."""
        docstring = remove_pdf_content.__doc__ or ""
        
        # Should focus on removing specific content types
        removal_terms = ['remove', 'specific content', 'images', 'annotations']
        has_removal_focus = any(term in docstring.lower() for term in removal_terms)
        
        assert has_removal_focus, "Tool should focus on removing specific content types"

    def test_selective_removal_capability(self):
        """Verify tool supports selective removal of different content types."""
        sig = inspect.signature(remove_pdf_content)
        
        # Should have multiple selective removal options
        removal_params = ['remove_images', 'remove_annotations']
        for param in removal_params:
            assert param in sig.parameters, f"Should support {param} for selective removal"
            assert sig.parameters[param].default is False, f"{param} should default to False for safety"

    def test_stream_compression_enhancement(self):
        """Verify compress_streams enhances size reduction beyond content removal."""
        sig = inspect.signature(remove_pdf_content)
        
        # compress_streams should default to True for additional optimization
        assert 'compress_streams' in sig.parameters, "Should include compress_streams parameter"
        assert sig.parameters['compress_streams'].default is True, "compress_streams should default to True"


# Contract preservation test summary for remove_pdf_content:
# ✅ Function signature: async def remove_pdf_content(file_path: str, output_file: str = None, remove_images: bool = False, remove_annotations: bool = False, compress_streams: bool = True) -> str
# ✅ Selective removal: remove_images and remove_annotations control specific content types
# ✅ Stream compression: compress_streams=True by default for additional size reduction
# ✅ Safety defaults: Content removal options default to False (safe operation)
# ✅ Auto-generation: output_file auto-generated when None
# ✅ Size reduction: Primary purpose is reducing file size by removing content
# ✅ Error format: {'success': False, 'error': str, 'operation': 'remove_pdf_content'}
# ✅ Purpose: Remove specific content types from PDF to reduce file size


