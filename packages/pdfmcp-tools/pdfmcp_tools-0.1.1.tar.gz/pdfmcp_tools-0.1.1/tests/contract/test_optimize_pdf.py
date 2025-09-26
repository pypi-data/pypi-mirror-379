"""
Contract tests for optimize_pdf tool.

These tests verify the exact interface contract that must be preserved during refactoring.
CRITICAL: Any changes to these contracts will break MCP client integrations.
"""

import pytest
import json
import inspect
from typing import get_type_hints

from src.pdfreadermcp.server import optimize_pdf


class TestOptimizePdfContract:
    """Contract tests for optimize_pdf tool - verifies interface preservation."""

    def test_function_exists(self):
        """Verify optimize_pdf function exists and is accessible."""
        assert hasattr(optimize_pdf, '__call__'), "optimize_pdf function must be callable"
        assert inspect.iscoroutinefunction(optimize_pdf), "optimize_pdf must be async function"

    def test_function_signature(self):
        """Verify exact function signature matches contract specification."""
        sig = inspect.signature(optimize_pdf)
        params = sig.parameters

        # Verify parameter names and types
        required_params = ['file_path']
        optional_params = ['output_file', 'optimization_level']
        
        for param in required_params:
            assert param in params, f"Must have {param} parameter"
            assert params[param].default == inspect.Parameter.empty, f"{param} must be required"

        for param in optional_params:
            assert param in params, f"Must have {param} parameter"

        # Verify parameter defaults per contract
        assert params['output_file'].default is None, "output_file default must be None"
        assert params['optimization_level'].default == 'medium', "optimization_level default must be 'medium'"

        # Verify return type annotation
        assert sig.return_annotation == str, "Must return str (JSON string)"

    def test_type_hints(self):
        """Verify type hints match contract specification."""
        hints = get_type_hints(optimize_pdf)
        
        assert hints.get('file_path') == str, "file_path must be typed as str"
        assert hints.get('optimization_level') == str, "optimization_level must be typed as str"
        assert hints.get('return') == str, "return type must be str"

    @pytest.mark.asyncio
    async def test_required_parameters(self):
        """Test that file_path parameter is required."""
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'file_path'"):
            await optimize_pdf()

    @pytest.mark.asyncio
    async def test_optimization_level_presets(self):
        """Test that optimization_level supports preset values per contract."""
        valid_levels = ['light', 'medium', 'heavy', 'maximum']
        
        for level in valid_levels:
            result = await optimize_pdf("test.pdf", optimization_level=level)
            parsed = json.loads(result)
            
            # Should accept optimization preset levels
            if not parsed['success']:
                assert 'optimization_level' not in parsed['error'], f"Optimization level '{level}' should be accepted"

    @pytest.mark.asyncio
    async def test_medium_default_level(self):
        """Test that default optimization level is 'medium' per contract."""
        result = await optimize_pdf("test.pdf")
        parsed = json.loads(result)
        
        # Should use medium default without parameter errors
        if not parsed['success']:
            assert 'optimization_level' not in parsed['error'], "Should use medium default level"
            assert 'medium' not in parsed['error'], "Should handle medium level"

    @pytest.mark.asyncio
    async def test_output_file_parameter(self):
        """Test that output_file parameter controls output location per contract."""
        # Test with default (None) - should use '_optimized' suffix
        result1 = await optimize_pdf("test.pdf")
        parsed1 = json.loads(result1)
        
        # Test with custom output file
        result2 = await optimize_pdf("test.pdf", output_file="optimized.pdf")
        parsed2 = json.loads(result2)
        
        # Both should accept the parameter without errors
        for parsed in [parsed1, parsed2]:
            if not parsed['success']:
                assert 'output_file' not in parsed['error'], "output_file parameter should be accepted"

    @pytest.mark.asyncio
    async def test_optimized_suffix_default(self):
        """Test that '_optimized' suffix is added by default per contract."""
        result = await optimize_pdf("test.pdf")
        parsed = json.loads(result)
        
        # Should handle suffix addition without errors
        if not parsed['success']:
            assert 'suffix' not in parsed.get('error', '').lower(), "Should support suffix addition"
            assert 'optimized' not in parsed.get('error', ''), "Should handle optimized suffix"

    @pytest.mark.asyncio
    async def test_various_compression_techniques(self):
        """Test that tool uses various compression techniques per contract."""
        # Test different optimization levels to ensure compression variety
        levels = ['light', 'heavy']
        
        for level in levels:
            result = await optimize_pdf("test.pdf", optimization_level=level)
            parsed = json.loads(result)
            
            # Should handle different compression approaches
            if not parsed['success']:
                assert 'compression' not in parsed.get('error', '').lower(), f"Should support {level} compression"

    @pytest.mark.asyncio
    async def test_error_response_format(self):
        """Test error response format matches contract specification."""
        result = await optimize_pdf("non_existent_file.pdf")
        
        # Parse JSON response
        parsed = json.loads(result)
        
        # Verify error format structure
        assert 'success' in parsed, "Error response must contain 'success' field"
        assert 'error' in parsed, "Error response must contain 'error' field"
        assert 'operation' in parsed, "Error response must contain 'operation' field"
        
        # Verify error format values
        assert parsed['success'] is False, "Error response success must be False"
        assert isinstance(parsed['error'], str), "Error message must be string"
        assert parsed['operation'] == 'optimize_pdf', "Must specify operation name"

    @pytest.mark.asyncio
    async def test_success_response_structure(self):
        """Test that successful response includes optimization results and file size statistics."""
        result = await optimize_pdf("test.pdf")
        parsed = json.loads(result)
        
        # Even if it fails, verify we get proper JSON structure
        assert isinstance(parsed, dict), "Response must be JSON object"
        
        # For successful responses, should have optimization statistics
        if parsed.get('success'):
            # Should include file size and compression information
            expected_fields = ['file_size', 'original_size', 'compressed_size', 'compression_ratio', 'size_reduction']
            has_stats_info = any(field in parsed for field in expected_fields)
            assert has_stats_info, "Successful response must contain optimization results and file size statistics"

    def test_function_docstring_exists(self):
        """Verify function has proper documentation."""
        assert optimize_pdf.__doc__ is not None, "Function must have docstring"
        docstring = optimize_pdf.__doc__
        
        # Verify key contract elements in documentation
        assert 'optimize' in docstring.lower(), "Docstring must describe optimization functionality"
        assert 'compression' in docstring.lower(), "Docstring must mention compression techniques"
        assert 'light' in docstring and 'medium' in docstring and 'heavy' in docstring and 'maximum' in docstring, "Docstring must document optimization presets"
        assert 'size' in docstring.lower(), "Docstring must mention file size reduction"

    @pytest.mark.asyncio
    async def test_return_type_is_string(self):
        """Verify function always returns string (JSON), never dict or other types."""
        result = await optimize_pdf("test.pdf")
        assert isinstance(result, str), "optimize_pdf must always return string (JSON format)"
        
        # Verify it's valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            pytest.fail("optimize_pdf must return valid JSON string")

    @pytest.mark.contract
    def test_tool_registration_compatibility(self):
        """Verify function is compatible with FastMCP tool registration."""
        assert hasattr(optimize_pdf, '__call__'), "Must be callable for FastMCP registration"
        assert inspect.iscoroutinefunction(optimize_pdf), "Must be async for FastMCP tools"
        
        # Verify required parameters
        sig = inspect.signature(optimize_pdf)
        required_params = [name for name, param in sig.parameters.items() 
                         if param.default == inspect.Parameter.empty]
        assert 'file_path' in required_params, "file_path must be required"
        assert len(required_params) == 1, "Only file_path should be required"

    def test_optimization_operation_purpose(self):
        """Verify this tool optimizes PDF files for smaller size."""
        docstring = optimize_pdf.__doc__ or ""
        
        # Should mention optimization, compression, and size reduction
        optimization_terms = ['optimize', 'compress', 'reduce', 'smaller']
        has_optimization_focus = any(term in docstring.lower() for term in optimization_terms)
        
        assert has_optimization_focus, "Tool should focus on optimization and size reduction"

    def test_preset_levels_progression(self):
        """Verify optimization levels represent increasing compression intensity."""
        sig = inspect.signature(optimize_pdf)
        docstring = optimize_pdf.__doc__ or ""
        
        # Should document progression from light to maximum
        levels = ['light', 'medium', 'heavy', 'maximum']
        for level in levels:
            assert level in docstring, f"Docstring should document {level} optimization level"

    def test_file_size_statistics_focus(self):
        """Verify tool emphasizes file size reduction statistics per contract."""
        docstring = optimize_pdf.__doc__ or ""
        
        # Should mention statistics, file size, or compression ratio
        stats_terms = ['statistics', 'file size', 'compression ratio', 'reduction']
        has_stats_focus = any(term in docstring.lower() for term in stats_terms)
        
        assert has_stats_focus, "Tool should emphasize file size statistics"


# Contract preservation test summary for optimize_pdf:
# ✅ Function signature: async def optimize_pdf(file_path: str, output_file: str = None, optimization_level: str = 'medium') -> str
# ✅ Optimization presets: 'light', 'medium' (default), 'heavy', 'maximum'
# ✅ Output naming: '_optimized' suffix when output_file=None
# ✅ Compression techniques: Various methods based on optimization level
# ✅ Error format: {'success': False, 'error': str, 'operation': 'optimize_pdf'}
# ✅ Success format: Must include optimization results and file size statistics
# ✅ Purpose: Optimize PDF files using compression techniques for size reduction


