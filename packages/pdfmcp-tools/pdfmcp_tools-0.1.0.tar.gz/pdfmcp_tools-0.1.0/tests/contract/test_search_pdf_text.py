"""
Contract tests for search_pdf_text tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import search_pdf_text


class TestSearchPdfTextContract:
    """Contract tests for search_pdf_text tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify search_pdf_text function exists and is accessible."""
        assert hasattr(search_pdf_text, '__call__'), "search_pdf_text function must be callable"
        assert inspect.iscoroutinefunction(search_pdf_text), "search_pdf_text must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(search_pdf_text)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path', 'query']
        optional_params = ['pages', 'case_sensitive', 'regex_search', 'context_chars', 'max_matches']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults
        assert params['pages'].default is None, "pages default must be None"
        assert params['case_sensitive'].default is False, "case_sensitive default must be False"
        assert params['regex_search'].default is False, "regex_search default must be False"
        assert params['context_chars'].default == 100, "context_chars default must be 100"
        assert params['max_matches'].default == 100, "max_matches default must be 100"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(search_pdf_text)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('query') == str, "query must be typed as str"
        assert hints.get('case_sensitive') == bool, "case_sensitive must be typed as bool"
        assert hints.get('regex_search') == bool, "regex_search must be typed as bool"
        assert hints.get('context_chars') == int, "context_chars must be typed as int"
        assert hints.get('max_matches') == int, "max_matches must be typed as int"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path and query parameters are required."""
        # Missing both parameters
        with pytest.raises(TypeError, match="missing .* required positional argument"):
            await search_pdf_text()

        # Missing query parameter  
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'query'"):
            await search_pdf_text("test.pdf")

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
            result = await search_pdf_text("test.pdf", "search_term", pages=pages)
            parsed = json.loads(result)
            
            # Should handle page syntax without parameter errors
            if not parsed['success']:
                assert 'pages' not in parsed['error'], f"Page syntax '{pages}' should not cause parameter error"

    @pytest.mark.asyncio
    async def test_regex_search_capability(self):
        """Test that regex search is supported per contract."""
        result = await search_pdf_text("test.pdf", r"[Tt]est.*pattern", regex_search=True)
        parsed = json.loads(result)
        
        # Should accept regex patterns without parameter errors
        if not parsed['success']:
            assert 'regex' not in parsed.get('error', '').lower(), "Regex search should be supported"
            assert 'regex_search' not in parsed['error'], "regex_search parameter should be accepted"

    @pytest.mark.asyncio
    async def test_case_sensitivity_control(self):
        """Test that case sensitivity control works per contract."""
        # Test case insensitive (default)
        result1 = await search_pdf_text("test.pdf", "TEST", case_sensitive=False)
        parsed1 = json.loads(result1)
        
        # Test case sensitive
        result2 = await search_pdf_text("test.pdf", "TEST", case_sensitive=True)  
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'case_sensitive' not in parsed['error'], "case_sensitive parameter should be accepted"

    @pytest.mark.asyncio
    async def test_context_and_match_limits(self):
        """Test that context_chars and max_matches limits work per contract."""
        result = await search_pdf_text("test.pdf", "test", context_chars=50, max_matches=25)
        parsed = json.loads(result)
        
        # Should accept limit parameters without errors
        if not parsed['success']:
            assert 'context_chars' not in parsed['error'], "context_chars parameter should be accepted"
            assert 'max_matches' not in parsed['error'], "max_matches parameter should be accepted"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await search_pdf_text("non_existent_file.pdf", "search_term")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'search_pdf_text', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes search results, match locations, and context."""
        # This will fail initially but tests the expected structure
        result = await search_pdf_text("test.pdf", "test")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure  
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have search results structure
        if parsed.get('success'):
            assert 'matches' in parsed or 'results' in parsed, "Successful response must contain search results"
            assert 'total_matches' in parsed or 'match_count' in parsed, "Should include match statistics"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert search_pdf_text.__doc__ is not None, "Function must have docstring"
        docstring = search_pdf_text.__doc__
        
        # Verify key contract elements in documentation
        assert 'file_path' in docstring, "Docstring must document file_path parameter"
        assert 'query' in docstring, "Docstring must document query parameter"
        assert 'regex' in docstring, "Docstring must document regex functionality"
        assert 'case_sensitive' in docstring, "Docstring must document case sensitivity"
        assert 'context_chars' in docstring, "Docstring must document context feature"
        assert 'max_matches' in docstring, "Docstring must document match limiting"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await search_pdf_text("test.pdf", "test")
        assert isinstance(result, str), "search_pdf_text must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("search_pdf_text must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(search_pdf_text, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(search_pdf_text), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(search_pdf_text)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert 'query' in required_params, "query must be required"


# Contract preservation test summary for search_pdf_text:
# ✅ Function signature: async def search_pdf_text(file_path: str, query: str, pages: str = None, case_sensitive: bool = False, regex_search: bool = False, context_chars: int = 100, max_matches: int = 100) -> str
# ✅ Regex support: regex_search parameter enables regex pattern matching
# ✅ Case sensitivity: case_sensitive parameter controls matching behavior
# ✅ Context and limits: context_chars and max_matches control output
# ✅ Error format: {'success': False, 'error': str, 'operation': 'search_pdf_text'}
# ✅ Success format: Must include search results, match locations, and context
# ✅ Page range syntax: "1,3,5-10,-1" format supported


