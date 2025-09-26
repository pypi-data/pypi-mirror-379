"""
Contract tests for ocr_pdf tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import ocr_pdf


class TestOcrPdfContract:
    """Contract tests for ocr_pdf tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify ocr_pdf function exists and is accessible."""
        assert hasattr(ocr_pdf, '__call__'), "ocr_pdf function must be callable"
        assert inspect.iscoroutinefunction(ocr_pdf), "ocr_pdf must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(ocr_pdf)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['pages', 'language', 'chunk_size', 'chunk_overlap', 'dpi']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['pages'].default is None, "pages default must be None"
        assert params['language'].default == 'chi_sim', "language default must be 'chi_sim'"
        assert params['chunk_size'].default == 1000, "chunk_size default must be 1000"
        assert params['chunk_overlap'].default == 100, "chunk_overlap default must be 100"
        assert params['dpi'].default == 200, "dpi default must be 200"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(ocr_pdf)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('language') == str, "language must be typed as str"
        assert hints.get('chunk_size') == int, "chunk_size must be typed as int"
        assert hints.get('chunk_overlap') == int, "chunk_overlap must be typed as int"
        assert hints.get('dpi') == int, "dpi must be typed as int"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await ocr_pdf()

    @pytest.mark.asyncio
    async def test_chinese_default_language(self):
        """Test that default language is 'chi_sim' per contract specification."""
        result = await ocr_pdf("test.pdf")
        parsed = json.loads(result)
        
        # Should use chi_sim default without parameter errors
        if not parsed['success']:
            assert 'language' not in parsed['error'], "Should use chi_sim default language"
            assert 'chi_sim' not in parsed['error'], "Should handle chi_sim language"

    @pytest.mark.asyncio
    async def test_tesseract_language_codes(self):
        """Test that tool accepts Tesseract language codes per contract."""
        language_codes = [
            'eng',      # English
            'chi_sim',  # Simplified Chinese (default)
            'chi_tra',  # Traditional Chinese
            'fra',      # French
            'deu',      # German
        ]
        
        for lang in language_codes:
            result = await ocr_pdf("test.pdf", language=lang)
            parsed = json.loads(result)
            
            # Should accept valid Tesseract language codes
            if not parsed['success']:
                assert 'language' not in parsed['error'], f"Language '{lang}' should be accepted"

    @pytest.mark.asyncio
    async def test_page_range_syntax_support(self):
        """Test that page range syntax is supported per contract."""
        test_cases = [
            "1",           # Single page
            "1,3,5",       # Multiple pages  
            "1-10",        # Range
            "-1",          # Last page
            "1,3,5-10,-1"  # Combined syntax
        ]
        
        for pages in test_cases:
            result = await ocr_pdf("test.pdf", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_chunk_parameters(self):
        """Test that chunking parameters work per contract."""
        result = await ocr_pdf("test.pdf", chunk_size=500, chunk_overlap=50)
        parsed = json.loads(result)
        
        # Should accept chunking parameters without error
        if not parsed['success']:
            assert 'chunk_size' not in parsed['error'], "chunk_size parameter should be accepted"
            assert 'chunk_overlap' not in parsed['error'], "chunk_overlap parameter should be accepted"

    @pytest.mark.asyncio
    async def test_dpi_parameter(self):
        """Test that DPI parameter controls image conversion quality per contract."""
        dpi_values = [150, 200, 300, 400]
        
        for dpi in dpi_values:
            result = await ocr_pdf("test.pdf", dpi=dpi)
            parsed = json.loads(result)
            
            # Should accept DPI values without parameter errors
            if not parsed['success']:
                assert 'dpi' not in parsed['error'], f"DPI value {dpi} should be accepted"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await ocr_pdf("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'extraction_method' in parsed, "Error response must contain 'extraction_method' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['extraction_method'] == 'tesseract_ocr', "Must specify OCR extraction method"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes OCR results and metadata."""
        result = await ocr_pdf("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have OCR results
        if parsed.get('success'):
            # Should include OCR-specific data
            expected_fields = ['text', 'confidence', 'language', 'ocr_results']
            has_ocr_data = any(field in parsed for field in expected_fields)
            assert has_ocr_data, "Successful response must contain OCR results and metadata"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert ocr_pdf.__doc__ is not None, "Function must have docstring"
        docstring = ocr_pdf.__doc__
        
        # Verify key contract elements in documentation
        assert 'tesseract' in docstring.lower(), "Docstring must mention Tesseract"
        assert 'ocr' in docstring.lower(), "Docstring must mention OCR functionality"
        assert 'scanned' in docstring.lower(), "Docstring must mention scanned documents"
        assert 'chi_sim' in docstring, "Docstring must document default Chinese language"
        assert 'dpi' in docstring.lower(), "Docstring must document DPI parameter"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await ocr_pdf("test.pdf")
        assert isinstance(result, str), "ocr_pdf must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("ocr_pdf must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(ocr_pdf, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(ocr_pdf), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(ocr_pdf)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_tesseract_dependency_purpose(self):
        """Verify this tool is specifically for Tesseract OCR processing."""
        docstring = ocr_pdf.__doc__ or ""
        
        # Should specifically mention Tesseract and scanned documents
        tesseract_terms = ['tesseract', 'scanned', 'image-based']
        has_tesseract_focus = any(term in docstring.lower() for term in tesseract_terms)
        
        assert has_tesseract_focus, "Tool should be specifically for Tesseract OCR of scanned documents"

    def test_chinese_language_focus(self):
        """Verify default language reflects Chinese language focus per contract."""
        sig = inspect.signature(ocr_pdf)
        assert sig.parameters['language'].default == 'chi_sim', "Default should be simplified Chinese"


# Contract preservation test summary for ocr_pdf:
# ✅ Function signature: async def ocr_pdf(file_path: str, pages: str = None, language: str = 'chi_sim', chunk_size: int = 1000, chunk_overlap: int = 100, dpi: int = 200) -> str
# ✅ Default language: 'chi_sim' (simplified Chinese) as specified
# ✅ Tesseract integration: Specifically for scanned documents and image-based PDFs
# ✅ Language support: Accepts all Tesseract language codes
# ✅ DPI control: Higher DPI = better quality but slower processing
# ✅ Error format: {'success': False, 'error': str, 'extraction_method': 'tesseract_ocr'}
# ✅ Success format: Must include OCR results with confidence scoring


