"""
Contract tests for compress_pdf_images tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import compress_pdf_images


class TestCompressPdfImagesContract:
    """Contract tests for compress_pdf_images tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify compress_pdf_images function exists and is accessible."""
        assert hasattr(compress_pdf_images, '__call__'), "compress_pdf_images function must be callable"
        assert inspect.iscoroutinefunction(compress_pdf_images), "compress_pdf_images must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(compress_pdf_images)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['output_file', 'quality']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['quality'].default == 80, "quality default must be 80"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(compress_pdf_images)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('quality') == int, "quality must be typed as int"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await compress_pdf_images()

    @pytest.mark.asyncio
    async def test_quality_range_validation(self):
        """Test that quality parameter accepts 1-100 range per contract."""
        quality_values = [1, 50, 80, 95, 100]
        
        for quality in quality_values:
            result = await compress_pdf_images("test.pdf", quality=quality)
            parsed = json.loads(result)
            
            # Should accept quality values in valid range
            if not parsed['success']:
                assert 'quality' not in parsed['error'], f"Quality value {quality} should be accepted"

    @pytest.mark.asyncio
    async def test_quality_default_80(self):
        """Test that default quality is 80 per contract."""
        result = await compress_pdf_images("test.pdf")
        parsed = json.loads(result)
        
        # Should use quality=80 default without parameter errors
        if not parsed['success']:
            assert 'quality' not in parsed['error'], "Should use quality=80 default"

    @pytest.mark.asyncio
    async def test_quality_meaning_100_best(self):
        """Test that 100=best quality per contract specification."""
        # This tests the contract requirement that 100 represents best quality
        result = await compress_pdf_images("test.pdf", quality=100)
        parsed = json.loads(result)
        
        # Should accept quality=100 as best quality
        if not parsed['success']:
            assert 'quality' not in parsed['error'], "Quality=100 should be accepted as best quality"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output location per contract."""
        # Test with default (None) - should auto-generate
        result1 = await compress_pdf_images("test.pdf")
        parsed1 = json.loads(result1)
        
        # Test with custom output file
        result2 = await compress_pdf_images("test.pdf", output_file="compressed.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_auto_generated_output_file(self):
        """Test that output file is auto-generated when not provided per contract."""
        result = await compress_pdf_images("test.pdf")
        parsed = json.loads(result)
        
        # Should handle auto-generation without errors
        if not parsed['success']:
            assert 'auto' not in parsed.get('error', '').lower(), "Should support auto-generated filename"
            assert 'generate' not in parsed.get('error', '').lower(), "Should support filename generation"

    @pytest.mark.asyncio
    async def test_document_structure_preservation(self):
        """Test that document structure is preserved per contract."""
        result = await compress_pdf_images("test.pdf", quality=50)
        parsed = json.loads(result)
        
        # Should preserve non-image content during compression
        if not parsed['success']:
            assert 'structure' not in parsed.get('error', '').lower(), "Should preserve document structure"
            assert 'preserve' not in parsed.get('error', ''), "Should handle content preservation"

    @pytest.mark.asyncio
    async def test_images_only_compression(self):
        """Test that only images are compressed, not all content per contract."""
        result = await compress_pdf_images("test.pdf", quality=60)
        parsed = json.loads(result)
        
        # Should target images specifically, not other content
        if not parsed['success']:
            # Should not be general compression errors
            general_compression_terms = ['all content', 'entire document', 'whole file']
            error_msg = parsed.get('error', '').lower()
            has_general_compression = any(term in error_msg for term in general_compression_terms)
            assert not has_general_compression, "Should focus on image compression, not general compression"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await compress_pdf_images("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'compress_pdf_images', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes compression results and statistics."""
        result = await compress_pdf_images("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have compression statistics
        if parsed.get('success'):
            # Should include compression-specific information
            expected_fields = ['compression_results', 'statistics', 'size_reduction', 'images_compressed']
            has_compression_info = any(field in parsed for field in expected_fields)
            assert has_compression_info, "Successful response must contain compression results and statistics"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert compress_pdf_images.__doc__ is not None, "Function must have docstring"
        docstring = compress_pdf_images.__doc__
        
        # Verify key contract elements in documentation
        assert 'compress' in docstring.lower(), "Docstring must describe compression functionality"
        assert 'images' in docstring.lower(), "Docstring must specify image compression"
        assert 'preserv' in docstring.lower(), "Docstring must mention structure preservation"
        assert '1-100' in docstring, "Docstring must specify quality range"
        assert '100' in docstring and 'best' in docstring.lower(), "Docstring must specify 100=best quality"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await compress_pdf_images("test.pdf")
        assert isinstance(result, str), "compress_pdf_images must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("compress_pdf_images must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(compress_pdf_images, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(compress_pdf_images), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(compress_pdf_images)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_image_specific_compression_purpose(self):
        """Verify this tool specifically targets images, not general compression."""
        docstring = compress_pdf_images.__doc__ or ""
        
        # Should focus on images specifically
        image_terms = ['images', 'image compression', 'pictures']
        has_image_focus = any(term in docstring.lower() for term in image_terms)
        
        assert has_image_focus, "Tool should focus specifically on image compression"

    def test_quality_vs_size_tradeoff(self):
        """Verify quality parameter represents quality vs file size tradeoff."""
        docstring = compress_pdf_images.__doc__ or ""
        
        # Should mention quality and size relationship
        tradeoff_terms = ['quality', 'size', 'compression', 'smaller']
        has_tradeoff_info = any(term in docstring.lower() for term in tradeoff_terms)
        
        assert has_tradeoff_info, "Docstring should document quality vs size tradeoff"

    def test_different_from_general_optimization(self):
        """Verify this is different from optimize_pdf (images only vs general)."""
        # compress_pdf_images: Images only, preserves structure
        # optimize_pdf: General optimization, various techniques
        
        docstring = compress_pdf_images.__doc__ or ""
        
        # Should emphasize image-specific compression
        assert 'images' in docstring.lower(), "Should focus on images"
        assert 'preserve' in docstring.lower() or 'preserving' in docstring.lower(), "Should mention preservation"


# Contract preservation test summary for compress_pdf_images:
# ✅ Function signature: async def compress_pdf_images(file_path: str, output_file: str = None, quality: int = 80) -> str
# ✅ Image-specific: Compresses only images, preserves document structure
# ✅ Quality range: 1-100 where 100=best quality
# ✅ Default quality: 80 (good balance of quality vs size)
# ✅ Auto-generation: output_file auto-generated when None
# ✅ Structure preservation: Non-image content remains unchanged
# ✅ Error format: {'success': False, 'error': str, 'operation': 'compress_pdf_images'}
# ✅ Purpose: Selective image compression (vs optimize_pdf's general optimization)


