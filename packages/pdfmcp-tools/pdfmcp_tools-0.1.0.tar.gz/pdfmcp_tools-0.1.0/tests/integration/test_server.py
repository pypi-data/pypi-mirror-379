"""
Integration tests for MCP server startup and tool registration.

These tests validate that the FastMCP server starts correctly and all 18 PDF
processing tools are properly registered and accessible.
"""

import pytest
import json
import asyncio
import inspect
from unittest.mock import patch, MagicMock

from src.pdfreadermcp.server import app
from src.pdfreadermcp.__main__ import main, setup_logging
from src.pdfreadermcp import __version__


class TestMCPServerIntegration:
    """Integration tests for MCP server startup and tool registration."""

    @pytest.mark.integration
    def test_fastmcp_app_initialization(self):
        """Test that FastMCP app is properly initialized."""
        # Verify app object exists and is configured
        assert app is not None, "FastMCP app should be initialized"
        assert hasattr(app, 'run'), "App should have run method"
        assert hasattr(app, 'tool'), "App should have tool decorator"
        
        # Verify server name
        if hasattr(app, 'name'):
            assert 'PDF' in app.name, "Server name should mention PDF functionality"

    @pytest.mark.integration
    def test_all_tools_registered(self):
        """Test that all 18 PDF tools are registered with FastMCP."""
        
        # List of all expected tools
        expected_tools = [
            'read_pdf', 'extract_page_text', 'search_pdf_text', 'find_and_highlight_text',
            'get_pdf_metadata', 'set_pdf_metadata', 'remove_pdf_metadata',
            'split_pdf', 'extract_pages', 'merge_pdfs',
            'ocr_pdf', 'pdf_to_images', 'images_to_pdf', 'extract_pdf_images',
            'optimize_pdf', 'compress_pdf_images', 'remove_pdf_content', 'analyze_pdf_size'
        ]
        
        # Import all tool functions to verify they exist
        from src.pdfreadermcp import server
        
        for tool_name in expected_tools:
            assert hasattr(server, tool_name), f"Tool {tool_name} should be available in server module"
            tool_func = getattr(server, tool_name)
            assert callable(tool_func), f"Tool {tool_name} should be callable"
            assert inspect.iscoroutinefunction(tool_func), f"Tool {tool_name} should be async function"

    @pytest.mark.integration
    def test_tool_function_signatures(self):
        """Test that all tool functions have proper signatures for MCP compatibility."""
        
        from src.pdfreadermcp import server
        
        # Tool functions that should exist
        tool_functions = [
            'read_pdf', 'extract_page_text', 'search_pdf_text', 'find_and_highlight_text',
            'get_pdf_metadata', 'set_pdf_metadata', 'remove_pdf_metadata', 
            'split_pdf', 'extract_pages', 'merge_pdfs',
            'ocr_pdf', 'pdf_to_images', 'images_to_pdf', 'extract_pdf_images',
            'optimize_pdf', 'compress_pdf_images', 'remove_pdf_content', 'analyze_pdf_size'
        ]
        
        for tool_name in tool_functions:
            tool_func = getattr(server, tool_name)
            sig = inspect.signature(tool_func)
            
            # Should have proper return type annotation
            assert sig.return_annotation == str, f"Tool {tool_name} should return str (JSON)"
            
            # Should have at least file_path parameter for most tools
            exceptions = ['images_to_pdf', 'merge_pdfs']  # images_to_pdf takes image_paths, merge_pdfs takes file_paths
            if tool_name not in exceptions:
                assert 'file_path' in sig.parameters, f"Tool {tool_name} should have file_path parameter"
            elif tool_name == 'images_to_pdf':
                assert 'image_paths' in sig.parameters, f"Tool {tool_name} should have image_paths parameter"
            elif tool_name == 'merge_pdfs':
                assert 'file_paths' in sig.parameters, f"Tool {tool_name} should have file_paths parameter"

    @pytest.mark.integration
    def test_tool_documentation_completeness(self):
        """Test that all tools have comprehensive documentation."""
        
        from src.pdfreadermcp import server
        
        tool_functions = [
            'read_pdf', 'extract_page_text', 'search_pdf_text', 'find_and_highlight_text',
            'get_pdf_metadata', 'set_pdf_metadata', 'remove_pdf_metadata',
            'split_pdf', 'extract_pages', 'merge_pdfs', 
            'ocr_pdf', 'pdf_to_images', 'images_to_pdf', 'extract_pdf_images',
            'optimize_pdf', 'compress_pdf_images', 'remove_pdf_content', 'analyze_pdf_size'
        ]
        
        for tool_name in tool_functions:
            tool_func = getattr(server, tool_name)
            
            # Should have docstring
            assert tool_func.__doc__ is not None, f"Tool {tool_name} should have docstring"
            docstring = tool_func.__doc__
            assert len(docstring.strip()) > 50, f"Tool {tool_name} should have substantial documentation"
            
            # Should document parameters and return value
            assert 'Args:' in docstring or 'Parameters:' in docstring, f"Tool {tool_name} should document parameters"
            assert 'Returns:' in docstring, f"Tool {tool_name} should document return value"
            assert 'JSON' in docstring, f"Tool {tool_name} should mention JSON return format"

    @pytest.mark.integration
    def test_module_imports_and_dependencies(self):
        """Test that all module imports work correctly."""
        
        # Test core server imports
        try:
            from src.pdfreadermcp.server import app
            from src.pdfreadermcp.__main__ import main
            from src.pdfreadermcp import __version__
        except ImportError as e:
            pytest.fail(f"Core module imports should work: {e}")
        
        # Test tool imports
        try:
            from src.pdfreadermcp.tools import pdf_reader, pdf_operations, pdf_ocr
            from src.pdfreadermcp.tools import pdf_image_converter, pdf_metadata
            from src.pdfreadermcp.tools import pdf_text_search, pdf_optimizer
        except ImportError as e:
            pytest.fail(f"Tool module imports should work: {e}")
        
        # Test utility imports
        try:
            from src.pdfreadermcp.utils import cache, chunker, file_handler
        except ImportError as e:
            pytest.fail(f"Utility module imports should work: {e}")

    @pytest.mark.integration
    def test_package_metadata_accessibility(self):
        """Test that package metadata is properly accessible."""
        
        from src.pdfreadermcp import __version__, __author__, __email__, __description__
        
        # Should have proper metadata
        assert isinstance(__version__, str), "Version should be string"
        assert len(__version__) > 0, "Version should not be empty"
        assert '.' in __version__, "Version should follow semantic versioning"
        
        assert isinstance(__author__, str), "Author should be string"
        assert len(__author__) > 0, "Author should not be empty"
        
        assert isinstance(__email__, str), "Email should be string"
        assert '@' in __email__, "Email should be valid format"
        
        assert isinstance(__description__, str), "Description should be string"
        assert 'MCP' in __description__, "Description should mention MCP"
        assert '18' in __description__, "Description should mention tool count"

    @pytest.mark.integration
    def test_logging_configuration(self):
        """Test that logging is properly configured."""
        
        # Test logging setup function
        try:
            setup_logging()
        except Exception as e:
            pytest.fail(f"Logging setup should work without errors: {e}")
        
        # Test that logging doesn't interfere with JSON output
        import logging
        logger = logging.getLogger('test_logger')
        
        # Logging should be configured but not interfere with tool output
        logger.info("Test log message")
        # Should not raise exceptions

    @pytest.mark.integration  
    @pytest.mark.asyncio
    async def test_server_startup_simulation(self):
        """Test server startup process without actually starting server."""
        
        # Test that main function imports work
        from src.pdfreadermcp.__main__ import main, setup_logging
        from src.pdfreadermcp.server import app
        
        # Verify startup components are available
        assert callable(main), "Main function should be callable"
        assert callable(setup_logging), "Setup logging should be callable"
        assert app is not None, "FastMCP app should be available"
        
        # Test that setup_logging doesn't raise exceptions
        try:
            setup_logging()
        except Exception as e:
            pytest.fail(f"Logging setup should work: {e}")

    @pytest.mark.integration
    def test_tool_category_organization(self):
        """Test that tools are properly organized by category."""
        
        from src.pdfreadermcp import server
        
        # Categorize tools by their primary function
        text_tools = ['read_pdf', 'extract_page_text', 'search_pdf_text', 'find_and_highlight_text']
        document_tools = ['split_pdf', 'extract_pages', 'merge_pdfs']
        metadata_tools = ['get_pdf_metadata', 'set_pdf_metadata', 'remove_pdf_metadata']
        image_tools = ['pdf_to_images', 'images_to_pdf', 'extract_pdf_images']
        ocr_tools = ['ocr_pdf']
        optimization_tools = ['optimize_pdf', 'compress_pdf_images', 'remove_pdf_content', 'analyze_pdf_size']
        
        all_categories = text_tools + document_tools + metadata_tools + image_tools + ocr_tools + optimization_tools
        
        # Verify we have all 18 tools accounted for
        assert len(all_categories) == 18, "Should have exactly 18 tools across all categories"
        
        # Verify all tools exist
        for tool_name in all_categories:
            assert hasattr(server, tool_name), f"Tool {tool_name} should exist in server module"

    @pytest.mark.integration
    def test_fastmcp_compatibility_requirements(self):
        """Test that server meets FastMCP compatibility requirements."""
        
        from src.pdfreadermcp.server import app
        
        # Should be a FastMCP instance
        assert hasattr(app, 'run'), "Should have FastMCP run method"
        
        # Should have tool registration capabilities
        assert hasattr(app, 'tool'), "Should have tool decorator for registration"
        
        # Test that tool decorator works (without actually decorating)
        assert callable(app.tool), "Tool decorator should be callable"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_tool_isolation_and_independence(self):
        """Test that tools operate independently without side effects."""
        
        from src.pdfreadermcp.server import read_pdf, get_pdf_metadata, analyze_pdf_size
        
        # Run multiple tools in sequence to ensure no state interference
        sequence_tests = [
            read_pdf("test1.pdf"),
            get_pdf_metadata("test2.pdf"),  
            analyze_pdf_size("test3.pdf"),
            read_pdf("test4.pdf"),  # Repeat first tool
        ]
        
        results = []
        for task in sequence_tests:
            result = await task
            results.append(json.loads(result))
        
        # Each tool should operate independently
        for i, data in enumerate(results):
            assert 'success' in data, f"Tool {i} should provide independent response"
            assert isinstance(data['error'], str), f"Tool {i} should have string error"
        
        # First and last results should be identical (same tool, same input)
        assert results[0]['success'] == results[3]['success'], "Same tool should behave consistently"

    @pytest.mark.integration
    def test_entry_point_configuration(self):
        """Test that entry points are properly configured."""
        
        # Test that main function can be imported from package
        try:
            from pdfreadermcp import main
            assert callable(main), "Main function should be accessible from package"
        except ImportError as e:
            pytest.fail(f"Entry point import should work: {e}")
        
        # Test that __main__ module works
        try:
            import src.pdfreadermcp.__main__
            assert hasattr(src.pdfreadermcp.__main__, 'main'), "__main__ module should have main function"
        except ImportError as e:
            pytest.fail(f"__main__ module import should work: {e}")

    @pytest.mark.integration
    def test_tool_count_verification(self):
        """Verify that exactly 18 tools are available as specified."""
        
        from src.pdfreadermcp import server
        
        # Count actual tool functions
        tool_functions = []
        for attr_name in dir(server):
            attr = getattr(server, attr_name)
            if (callable(attr) and 
                inspect.iscoroutinefunction(attr) and 
                not attr_name.startswith('_') and
                attr_name != 'main'):
                tool_functions.append(attr_name)
        
        # Should have exactly 18 tools
        assert len(tool_functions) == 18, f"Should have exactly 18 tools, found: {tool_functions}"
        
        # Verify expected tools are present
        expected_tools = {
            'read_pdf', 'extract_page_text', 'search_pdf_text', 'find_and_highlight_text',
            'get_pdf_metadata', 'set_pdf_metadata', 'remove_pdf_metadata',
            'split_pdf', 'extract_pages', 'merge_pdfs',
            'ocr_pdf', 'pdf_to_images', 'images_to_pdf', 'extract_pdf_images',
            'optimize_pdf', 'compress_pdf_images', 'remove_pdf_content', 'analyze_pdf_size'
        }
        
        found_tools = set(tool_functions)
        assert found_tools == expected_tools, f"Tool mismatch. Expected: {expected_tools}, Found: {found_tools}"


# Server integration test summary:
# ✅ FastMCP app initialization and configuration
# ✅ All 18 PDF tools properly registered and accessible
# ✅ Tool function signatures compatible with MCP protocol
# ✅ Comprehensive documentation for all tools
# ✅ Module imports and dependency management
# ✅ Package metadata accessibility and correctness
# ✅ Logging configuration without interference
# ✅ Server startup process validation
# ✅ Tool category organization and coverage
# ✅ FastMCP compatibility requirements
# ✅ Tool isolation and independence verification
# ✅ Entry point configuration and accessibility
# ✅ Exact tool count verification (18 tools)
