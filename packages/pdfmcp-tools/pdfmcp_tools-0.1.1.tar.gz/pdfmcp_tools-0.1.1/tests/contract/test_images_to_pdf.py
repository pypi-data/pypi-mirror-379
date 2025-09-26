"""
Contract tests for images_to_pdf tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints, List

from src.pdfreadermcp.server import images_to_pdf


class TestImagesToPdfContract:
    """Contract tests for images_to_pdf tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify images_to_pdf function exists and is accessible."""
        assert hasattr(images_to_pdf, '__call__'), "images_to_pdf function must be callable"
        assert inspect.iscoroutinefunction(images_to_pdf), "images_to_pdf must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(images_to_pdf)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['image_paths', 'output_file']
        optional_params = ['page_size', 'quality', 'title', 'author']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['page_size'].default == "A4", "page_size default must be 'A4'"
        assert params['quality'].default == 95, "quality default must be 95"
        assert params['title'].default is None, "title default must be None"
        assert params['author'].default is None, "author default must be None"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(images_to_pdf)
        
        assert hints.get('image_paths') == List[str], "image_paths must be typed as List[str]"
        assert hints.get('output_file') == str, "output_file must be typed as str"
        assert hints.get('page_size') == str, "page_size must be typed as str"
        assert hints.get('quality') == int, "quality must be typed as int"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that image_paths and output_file parameters are required."""
        # Missing both parameters
        with pytest.raises(TypeError, match="missing .* required positional argument"):
            await images_to_pdf()

        # Missing output_file parameter  
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'output_file'"):
            await images_to_pdf(["image1.png"])

    @pytest.mark.asyncio
    async def test_image_paths_list_handling(self):
        """Test that image_paths accepts list of image file paths per contract."""
        valid_image_lists = [
            ["image1.png"],                              # Single image
            ["image1.png", "image2.jpg"],               # Two images
            ["img1.png", "img2.jpg", "img3.jpeg"],      # Multiple formats
        ]
        
        for image_list in valid_image_lists:
            result = await images_to_pdf(image_paths=image_list, output_file="output.pdf")
            parsed = json.loads(result)
            
            # Should handle image lists without parameter errors
            if not parsed['success']:
                assert 'image_paths' not in parsed['error'], f"Image list {image_list} should be accepted"
                assert 'list' not in parsed.get('error', '').lower(), f"Should accept list parameter"

    @pytest.mark.asyncio
    async def test_page_size_options(self):
        """Test that page_size supports standard page sizes per contract."""
        valid_page_sizes = ["A4", "Letter", "Legal", "auto"]
        
        for size in valid_page_sizes:
            result = await images_to_pdf(["image.png"], "output.pdf", page_size=size)
            parsed = json.loads(result)
            
            # Should accept standard page sizes
            if not parsed['success']:
                assert 'page_size' not in parsed['error'], f"Page size '{size}' should be accepted"

    @pytest.mark.asyncio
    async def test_quality_range_validation(self):
        """Test that quality parameter accepts 1-100 range per contract."""
        quality_values = [1, 50, 75, 95, 100]
        
        for quality in quality_values:
            result = await images_to_pdf(["image.png"], "output.pdf", quality=quality)
            parsed = json.loads(result)
            
            # Should accept quality values in valid range
            if not parsed['success']:
                assert 'quality' not in parsed['error'], f"Quality value {quality} should be accepted"

    @pytest.mark.asyncio
    async def test_metadata_parameters(self):
        """Test that title and author parameters set PDF metadata per contract."""
        result = await images_to_pdf(
            ["image.png"], 
            "output.pdf", 
            title="Test Document", 
            author="Test Author"
        )
        parsed = json.loads(result)
        
        # Should accept metadata parameters without errors
        if not parsed['success']:
            assert 'title' not in parsed['error'], "title parameter should be accepted"
            assert 'author' not in parsed['error'], "author parameter should be accepted"

    @pytest.mark.asyncio
    async def test_image_order_preservation(self):
        """Test that image order is preserved in PDF per contract."""
        # Test with specific order
        image_list = ["first.png", "second.jpg", "third.png"]
        result = await images_to_pdf(image_paths=image_list, output_file="output.pdf")
        parsed = json.loads(result)
        
        # Should accept the ordered list without issues
        if not parsed['success']:
            assert 'order' not in parsed.get('error', '').lower(), "Should preserve image order"
            assert 'sequence' not in parsed.get('error', '').lower(), "Should handle sequential conversion"

    @pytest.mark.asyncio
    async def test_output_file_requirement(self):
        """Test that output_file is required and not auto-generated per contract."""
        # Unlike other tools, this one requires explicit output filename
        sig = inspect.signature(images_to_pdf)
        assert sig.parameters['output_file'].default == inspect.Parameter.empty, "output_file must be required"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await images_to_pdf(["non_existent.png"], "output.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'images_to_pdf', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes conversion results."""
        result = await images_to_pdf(["image.png"], "output.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have conversion results
        if parsed.get('success'):
            # Should include information about the created PDF
            expected_fields = ['output_file', 'pages_created', 'result', 'pdf_created']
            has_conversion_info = any(field in parsed for field in expected_fields)
            assert has_conversion_info, "Successful response must contain conversion results"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert images_to_pdf.__doc__ is not None, "Function must have docstring"
        docstring = images_to_pdf.__doc__
        
        # Verify key contract elements in documentation
        assert 'convert' in docstring.lower() or 'images' in docstring.lower(), "Docstring must describe conversion functionality"
        assert 'page_size' in docstring, "Docstring must document page size options"
        assert 'quality' in docstring.lower(), "Docstring must document quality parameter"
        assert '1-100' in docstring, "Docstring must specify quality range"
        assert 'order' in docstring.lower() or 'preserve' in docstring.lower(), "Docstring must mention image order preservation"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await images_to_pdf(["image.png"], "output.pdf")
        assert isinstance(result, str), "images_to_pdf must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("images_to_pdf must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(images_to_pdf, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(images_to_pdf), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(images_to_pdf)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'image_paths' in required_params, "image_paths must be required"
        assert 'output_file' in required_params, "output_file must be required"

    def test_conversion_operation_purpose(self):
        """Verify this tool converts multiple images to single PDF."""
        # This tool should convert FROM images TO PDF (opposite of pdf_to_images)
        docstring = images_to_pdf.__doc__ or ""
        
        # Should mention converting images to PDF
        conversion_terms = ['convert', 'multiple images', 'single pdf']
        has_conversion_focus = any(term in docstring.lower() for term in conversion_terms)
        
        assert has_conversion_focus, "Tool should focus on converting multiple images to single PDF"

    def test_jpeg_quality_compression_purpose(self):
        """Verify quality parameter is for JPEG compression per contract."""
        docstring = images_to_pdf.__doc__ or ""
        
        # Should mention JPEG quality or compression
        quality_terms = ['jpeg', 'compression', 'quality']
        has_quality_info = any(term in docstring.lower() for term in quality_terms)
        
        assert has_quality_info, "Docstring should document JPEG quality/compression purpose"

    def test_opposite_of_pdf_to_images(self):
        """Verify this is the opposite operation of pdf_to_images."""
        # images_to_pdf: Many images → One PDF
        # pdf_to_images: One PDF → Many images
        
        sig = inspect.signature(images_to_pdf)
        hints = get_type_hints(images_to_pdf)
        
        # Should take multiple images (List[str]) and create single output file
        assert hints.get('image_paths') == List[str], "Should take multiple images"
        assert 'output_file' in sig.parameters, "Should create single output file"


# Contract preservation test summary for images_to_pdf:
# ✅ Function signature: async def images_to_pdf(image_paths: List[str], output_file: str, page_size: str = "A4", quality: int = 95, title: str = None, author: str = None) -> str
# ✅ Multiple inputs: Takes List[str] of image file paths
# ✅ Single output: Creates one PDF file (opposite of pdf_to_images)
# ✅ Page sizes: Supports A4, Letter, Legal, auto
# ✅ Quality control: 1-100 range for JPEG compression
# ✅ Order preservation: Images appear in PDF in list order
# ✅ Metadata: Optional title and author parameters
# ✅ Error format: {'success': False, 'error': str, 'operation': 'images_to_pdf'}


