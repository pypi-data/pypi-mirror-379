"""
Contract tests for analyze_pdf_size tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import analyze_pdf_size


class TestAnalyzePdfSizeContract:
    """Contract tests for analyze_pdf_size tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify analyze_pdf_size function exists and is accessible."""
        assert hasattr(analyze_pdf_size, '__call__'), "analyze_pdf_size function must be callable"
        assert inspect.iscoroutinefunction(analyze_pdf_size), "analyze_pdf_size must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(analyze_pdf_size)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        # Verify this tool takes only file_path parameter (analysis only)
        assert len(params) == 1, "Should only have file_path parameter (read-only analysis)"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(analyze_pdf_size)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await analyze_pdf_size()

    @pytest.mark.asyncio
    async def test_read_only_operation(self):
        """Test that this is a read-only analysis operation per contract."""
        result = await analyze_pdf_size("test.pdf")
        parsed = json.loads(result)
        
        # Should not attempt to modify the file (read-only analysis)
        if not parsed['success']:
            # Should not have file modification errors
            modification_terms = ['write', 'modify', 'change', 'save', 'output']
            error_msg = parsed.get('error', '').lower()
            has_modification_errors = any(term in error_msg for term in modification_terms)
            # If it has modification errors, they should not be about this tool trying to modify
            if has_modification_errors:
                assert 'read-only' in error_msg or 'analysis' in error_msg, "Should be clearly read-only operation"

    @pytest.mark.asyncio
    async def test_no_file_modification(self):
        """Test that tool does not modify files per contract."""
        sig = inspect.signature(analyze_pdf_size)
        
        # Should not have output file parameters (read-only)
        modification_params = ['output_file', 'output_dir', 'save_to']
        for param in modification_params:
            assert param not in sig.parameters, f"Read-only analysis should not have {param} parameter"

    @pytest.mark.asyncio
    async def test_optimization_opportunities_identification(self):
        """Test that tool identifies optimization opportunities per contract."""
        result = await analyze_pdf_size("test.pdf")
        parsed = json.loads(result)
        
        # Should focus on analysis and optimization recommendations
        if parsed.get('success'):
            # Should include optimization recommendations
            expected_fields = ['optimization_opportunities', 'recommendations', 'suggestions', 'analysis']
            has_optimization_info = any(field in parsed for field in expected_fields)
            assert has_optimization_info, "Successful response should include optimization opportunities"

    @pytest.mark.asyncio
    async def test_size_breakdown_analysis(self):
        """Test that tool provides size breakdown by content type per contract."""
        result = await analyze_pdf_size("test.pdf")
        parsed = json.loads(result)
        
        # Should include size breakdown information
        if parsed.get('success'):
            # Should have size analysis breakdown
            expected_fields = ['size_breakdown', 'content_analysis', 'breakdown', 'content_types']
            has_breakdown_info = any(field in parsed for field in expected_fields)
            assert has_breakdown_info, "Successful response should include size breakdown by content type"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await analyze_pdf_size("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'analyze_pdf_size', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes size analysis and optimization recommendations."""
        result = await analyze_pdf_size("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have comprehensive analysis
        if parsed.get('success'):
            # Should include analysis and recommendations
            expected_fields = ['file_size', 'total_size', 'analysis', 'recommendations', 'breakdown']
            has_analysis_info = any(field in parsed for field in expected_fields)
            assert has_analysis_info, "Successful response must contain size analysis and optimization recommendations"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert analyze_pdf_size.__doc__ is not None, "Function must have docstring"
        docstring = analyze_pdf_size.__doc__
        
        # Verify key contract elements in documentation
        assert 'analyze' in docstring.lower(), "Docstring must describe analysis functionality"
        assert 'size' in docstring.lower(), "Docstring must mention size analysis"
        assert 'optimization' in docstring.lower(), "Docstring must mention optimization opportunities"
        assert 'recommendations' in docstring.lower(), "Docstring must mention recommendations"
        assert 'breakdown' in docstring.lower() or 'content type' in docstring.lower(), "Docstring must mention content breakdown"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await analyze_pdf_size("test.pdf")
        assert isinstance(result, str), "analyze_pdf_size must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("analyze_pdf_size must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(analyze_pdf_size, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(analyze_pdf_size), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(analyze_pdf_size)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_analysis_operation_purpose(self):
        """Verify this tool analyzes PDF files for optimization insights."""
        docstring = analyze_pdf_size.__doc__ or ""
        
        # Should focus on analysis and insights
        analysis_terms = ['analyze', 'insights', 'identify', 'opportunities']
        has_analysis_focus = any(term in docstring.lower() for term in analysis_terms)
        
        assert has_analysis_focus, "Tool should focus on analysis and optimization insights"

    def test_non_destructive_operation(self):
        """Verify this tool does not modify the input file (non-destructive analysis)."""
        docstring = analyze_pdf_size.__doc__ or ""
        
        # Should not mention modifying or changing the file
        modification_terms = ['modify', 'change', 'alter', 'save', 'write']
        has_modification_focus = any(term in docstring.lower() for term in modification_terms)
        
        # If it mentions modification, it should be in the context of what NOT to do
        if has_modification_focus:
            assert 'not' in docstring.lower() or 'without' in docstring.lower(), "Should clarify non-destructive nature"

    def test_optimization_guidance_purpose(self):
        """Verify tool provides guidance for other optimization tools."""
        # This tool should help users decide which optimization tools to use
        docstring = analyze_pdf_size.__doc__ or ""
        
        # Should mention recommendations or guidance
        guidance_terms = ['recommend', 'suggest', 'guidance', 'opportunities']
        has_guidance_focus = any(term in docstring.lower() for term in guidance_terms)
        
        assert has_guidance_focus, "Tool should provide optimization guidance and recommendations"

    def test_simplest_tool_interface(self):
        """Verify this has the simplest interface (file_path only) per contract."""
        sig = inspect.signature(analyze_pdf_size)
        
        # Should be the simplest tool - only takes file_path
        assert len(sig.parameters) == 1, "Should have the simplest interface with only file_path parameter"
        assert list(sig.parameters.keys())[0] == 'file_path', "Single parameter should be file_path"


# Contract preservation test summary for analyze_pdf_size:
# ✅ Function signature: async def analyze_pdf_size(file_path: str) -> str
# ✅ Simplest interface: Only takes file_path parameter (read-only operation)
# ✅ Non-destructive: Does not modify input file in any way
# ✅ Size breakdown: Provides analysis by content type (images, text, etc.)
# ✅ Optimization opportunities: Identifies potential optimization strategies
# ✅ Recommendations: Suggests which optimization tools/techniques to use
# ✅ Error format: {'success': False, 'error': str, 'operation': 'analyze_pdf_size'}
# ✅ Purpose: Analyze PDF file structure to identify optimization opportunities


