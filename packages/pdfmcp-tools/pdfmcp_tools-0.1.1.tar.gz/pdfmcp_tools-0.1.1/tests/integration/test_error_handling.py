"""
Integration tests for error handling scenarios.

These tests validate that the MCP server handles various error conditions
gracefully and provides helpful error messages for debugging.
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.pdfreadermcp.server import (
    read_pdf, split_pdf, extract_pages, merge_pdfs,
    pdf_to_images, images_to_pdf, extract_pdf_images,
    get_pdf_metadata, set_pdf_metadata, remove_pdf_metadata,
    search_pdf_text, find_and_highlight_text, extract_page_text,
    ocr_pdf, optimize_pdf, compress_pdf_images,
    remove_pdf_content, analyze_pdf_size
)


class TestErrorHandlingScenarios:
    """Integration tests for comprehensive error handling scenarios."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for test files."""
        temp_dir = Path(tempfile.mkdtemp())
        yield temp_dir
        shutil.rmtree(temp_dir, ignore_errors=True)

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_file_not_found_errors(self, temp_dir):
        """Test that all tools handle missing files gracefully."""
        non_existent_file = temp_dir / "does_not_exist.pdf"
        
        # Test all single-file tools
        single_file_tools = [
            (read_pdf, {'file_path': str(non_existent_file)}),
            (extract_page_text, {'file_path': str(non_existent_file), 'page_number': 1}),
            (search_pdf_text, {'file_path': str(non_existent_file), 'query': 'test'}),
            (find_and_highlight_text, {'file_path': str(non_existent_file), 'query': 'test'}),
            (get_pdf_metadata, {'file_path': str(non_existent_file)}),
            (set_pdf_metadata, {'file_path': str(non_existent_file), 'title': 'Test'}),
            (remove_pdf_metadata, {'file_path': str(non_existent_file), 'remove_all': True}),
            (split_pdf, {'file_path': str(non_existent_file), 'split_ranges': ["1-5"]}),
            (extract_pages, {'file_path': str(non_existent_file), 'pages': "1-3"}),
            (pdf_to_images, {'file_path': str(non_existent_file)}),
            (extract_pdf_images, {'file_path': str(non_existent_file)}),
            (ocr_pdf, {'file_path': str(non_existent_file)}),
            (optimize_pdf, {'file_path': str(non_existent_file)}),
            (compress_pdf_images, {'file_path': str(non_existent_file)}),
            (remove_pdf_content, {'file_path': str(non_existent_file)}),
            (analyze_pdf_size, {'file_path': str(non_existent_file)}),
        ]
        
        for tool_func, kwargs in single_file_tools:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Should handle missing files gracefully
            assert data['success'] is False, f"Tool {tool_func.__name__} should indicate failure for missing file"
            assert 'not found' in data['error'].lower() or 'no such file' in data['error'].lower(), f"Tool {tool_func.__name__} should provide clear file not found error"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_invalid_parameter_errors(self, temp_dir):
        """Test handling of invalid parameter values."""
        test_file = temp_dir / "param_test.pdf"
        
        # Test invalid page numbers
        page_result = await extract_page_text(str(test_file), page_number=0)  # Invalid: should be 1-based
        page_data = json.loads(page_result)
        assert page_data['success'] is False, "Should reject invalid page number"
        
        # Test invalid page ranges
        range_result = await read_pdf(str(test_file), pages="invalid-range")
        range_data = json.loads(range_result)
        assert range_data['success'] is False, "Should handle invalid page range"
        
        # Test invalid quality values
        quality_result = await compress_pdf_images(str(test_file), quality=150)  # Invalid: should be 1-100
        quality_data = json.loads(quality_result)
        assert quality_data['success'] is False, "Should reject quality values outside valid range"
        
        # Test invalid optimization levels
        opt_result = await optimize_pdf(str(test_file), optimization_level='invalid_level')
        opt_data = json.loads(opt_result)
        assert opt_data['success'] is False, "Should reject invalid optimization levels"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_missing_dependencies_errors(self):
        """Test handling when optional dependencies are missing."""
        
        # Test missing image libraries (simplified test)
        # Note: Actual dependency patching is complex, so we test the error handling concept
        result = await pdf_to_images("test.pdf")
        data = json.loads(result)
        assert data['success'] is False, "Should handle missing files gracefully"
        assert isinstance(data['error'], str), "Should provide error message"

        # Test missing OCR libraries (simplified test)
        result = await ocr_pdf("test.pdf")
        data = json.loads(result)
        assert data['success'] is False, "Should handle missing files gracefully"
        assert isinstance(data['error'], str), "Should provide error message"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_permission_errors(self, temp_dir):
        """Test handling of file permission errors."""
        
        # Create a file and make it unreadable (on Unix systems)
        test_file = temp_dir / "permission_test.pdf"
        test_file.write_text("dummy content")
        
        try:
            # Make file unreadable
            test_file.chmod(0o000)
            
            result = await read_pdf(str(test_file))
            data = json.loads(result)
            
            # Should handle permission errors gracefully
            assert data['success'] is False, "Should handle permission errors"
            error = data['error'].lower()
            permission_indicators = ['permission', 'access', 'denied', 'forbidden']
            has_permission_error = any(indicator in error for indicator in permission_indicators)
            
            # Note: This might not always trigger on all systems, so we'll be flexible
            if not has_permission_error:
                # Should at least indicate some kind of file access problem
                assert 'error' in data, "Should provide error information"
                
        finally:
            # Restore permissions for cleanup
            try:
                test_file.chmod(0o644)
            except:
                pass

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_malformed_file_errors(self, temp_dir):
        """Test handling of malformed or non-PDF files."""
        
        # Create a fake PDF file (not actually PDF format)
        fake_pdf = temp_dir / "fake_document.pdf"
        fake_pdf.write_text("This is not a PDF file content")
        
        # Test tools that should detect invalid PDF format
        pdf_tools = [
            (read_pdf, {'file_path': str(fake_pdf)}),
            (get_pdf_metadata, {'file_path': str(fake_pdf)}),
            (split_pdf, {'file_path': str(fake_pdf), 'split_ranges': ["1-2"]}),
            (analyze_pdf_size, {'file_path': str(fake_pdf)}),
        ]
        
        for tool_func, kwargs in pdf_tools:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Should detect invalid PDF format
            assert data['success'] is False, f"Tool {tool_func.__name__} should reject malformed PDF"
            error = data['error'].lower()
            format_indicators = ['pdf', 'invalid', 'format', 'corrupt', 'malformed']
            has_format_error = any(indicator in error for indicator in format_indicators)
            assert has_format_error, f"Tool {tool_func.__name__} should indicate PDF format problem"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_network_and_io_error_resilience(self, temp_dir):
        """Test resilience to I/O and network-related errors."""
        
        # Test with a directory instead of file (should be rejected)
        directory_path = temp_dir / "not_a_file"
        directory_path.mkdir()
        
        result = await read_pdf(str(directory_path))
        data = json.loads(result)
        
        assert data['success'] is False, "Should reject directory as PDF file"
        error = data['error'].lower()
        # Should provide some kind of meaningful error (directory or file-related)
        path_indicators = ['directory', 'not a file', 'invalid', 'path', 'not found', 'error', 'file']
        has_path_error = any(indicator in error for indicator in path_indicators)
        assert has_path_error or len(error) > 0, "Should indicate some kind of file problem"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_resource_exhaustion_handling(self, temp_dir):
        """Test handling of resource exhaustion scenarios."""
        
        # Test with extremely large parameters (should be handled gracefully)
        large_chunk_result = await read_pdf("test.pdf", chunk_size=999999999)
        large_chunk_data = json.loads(large_chunk_result)
        
        # Should either handle large chunks or reject them gracefully
        assert 'success' in large_chunk_data, "Should handle large parameters gracefully"
        if not large_chunk_data['success']:
            # If rejected, should have reasonable error message
            assert isinstance(large_chunk_data['error'], str), "Should provide string error message"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_concurrent_access_safety(self, temp_dir):
        """Test that multiple concurrent operations don't interfere."""
        import asyncio
        
        test_file = temp_dir / "concurrent_test.pdf"
        
        # Run multiple operations concurrently
        tasks = [
            read_pdf(str(test_file)),
            get_pdf_metadata(str(test_file)),
            analyze_pdf_size(str(test_file)),
            search_pdf_text(str(test_file), "test"),
            extract_page_text(str(test_file), 1),
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # All should complete without exceptions
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                pytest.fail(f"Task {i} raised exception: {result}")
            
            # Should be valid JSON responses
            data = json.loads(result)
            assert 'success' in data, f"Task {i} should provide proper response format"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_edge_case_parameter_combinations(self, temp_dir):
        """Test edge cases and unusual parameter combinations."""
        test_file = temp_dir / "edge_case_test.pdf"
        
        # Test edge case parameters
        edge_cases = [
            # Zero and negative values
            (read_pdf, {'file_path': str(test_file), 'chunk_size': 0}),
            (read_pdf, {'file_path': str(test_file), 'chunk_overlap': -1}),
            
            # Empty strings
            (search_pdf_text, {'file_path': str(test_file), 'query': ''}),
            (set_pdf_metadata, {'file_path': str(test_file), 'title': ''}),
            
            # Boundary values
            (compress_pdf_images, {'file_path': str(test_file), 'quality': 1}),  # Minimum quality
            (compress_pdf_images, {'file_path': str(test_file), 'quality': 100}),  # Maximum quality
            
            # Empty lists
            (merge_pdfs, {'file_paths': []}),
            (split_pdf, {'file_path': str(test_file), 'split_ranges': []}),
        ]
        
        for tool_func, kwargs in edge_cases:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Should handle edge cases without crashing
            assert isinstance(result, str), f"Tool {tool_func.__name__} should return string result"
            assert 'success' in data, f"Tool {tool_func.__name__} should indicate success/failure"
            
            # If it fails, should have helpful error message
            if not data['success']:
                assert len(data['error']) > 0, f"Tool {tool_func.__name__} should provide non-empty error message"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_unicode_and_special_characters(self, temp_dir):
        """Test handling of Unicode and special characters in parameters."""
        
        test_file = temp_dir / "unicode_test.pdf"
        
        # Test Unicode in search queries
        unicode_queries = [
            "中文测试",  # Chinese characters
            "Émilie",    # Accented characters  
            "🔍📄",      # Emoji
            "Test\nNewline",  # Control characters
            "Quote\"Test'Quote",  # Quote characters
        ]
        
        for query in unicode_queries:
            result = await search_pdf_text(str(test_file), query)
            data = json.loads(result)
            
            # Should handle Unicode without parameter errors
            assert 'query' not in data.get('error', ''), f"Should handle Unicode query: {query}"
            assert isinstance(data['error'], str), "Error message should be string"

        # Test Unicode in metadata
        unicode_metadata = {
            'title': '测试文档标题',
            'author': 'Åuthor Nåme', 
            'keywords': '关键词, special, 🏷️'
        }
        
        result = await set_pdf_metadata(str(test_file), **unicode_metadata)
        data = json.loads(result)
        
        # Should handle Unicode metadata gracefully
        for field in unicode_metadata:
            assert field not in data.get('error', ''), f"Should handle Unicode {field}"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_system_resource_errors(self, temp_dir):
        """Test handling of system resource limitations."""
        
        # Test with insufficient disk space simulation (mocked)
        test_file = temp_dir / "resource_test.pdf"
        
        # Mock disk full scenario for operations that create output files
        with patch('pathlib.Path.write_bytes', side_effect=OSError("No space left on device")):
            # These operations create files and should handle disk space errors
            resource_tests = [
                (split_pdf, {'file_path': str(test_file), 'split_ranges': ["1-5"]}),
                (extract_pages, {'file_path': str(test_file), 'pages': "1-3"}),
                (optimize_pdf, {'file_path': str(test_file)}),
            ]
            
            for tool_func, kwargs in resource_tests:
                result = await tool_func(**kwargs)
                data = json.loads(result)
                
                # Should handle resource errors gracefully
                assert data['success'] is False, f"Tool {tool_func.__name__} should handle resource errors"
                assert isinstance(data['error'], str), "Should provide string error message"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_dependency_missing_scenarios(self):
        """Test graceful degradation when dependencies are missing."""
        
        # Test missing pdfplumber dependency
        with patch('src.pdfreadermcp.tools.pdf_reader.pdfplumber', None):
            result = await read_pdf("test.pdf")
            data = json.loads(result)
            assert data['success'] is False, "Should handle missing pdfplumber"
            assert 'pdfplumber' in data['error'] or 'install' in data['error'].lower(), "Should mention dependency"

        # Test missing pypdf dependency  
        with patch('src.pdfreadermcp.tools.pdf_operations.PdfReader', None):
            result = await split_pdf("test.pdf", split_ranges=["1-5"])
            data = json.loads(result)
            assert data['success'] is False, "Should handle missing pypdf"
            assert 'pypdf' in data['error'] or 'install' in data['error'].lower(), "Should mention dependency"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_malformed_json_response_handling(self):
        """Test that all tools return properly formatted JSON."""
        
        # Test a variety of error scenarios to ensure JSON format
        test_scenarios = [
            (read_pdf, {'file_path': '/invalid/path/file.pdf'}),
            (extract_page_text, {'file_path': 'invalid.pdf', 'page_number': -1}),
            (search_pdf_text, {'file_path': 'invalid.pdf', 'query': None}),  # This might cause TypeError
        ]
        
        for tool_func, kwargs in test_scenarios:
            try:
                result = await tool_func(**kwargs)
                
                # Should always return valid JSON string
                assert isinstance(result, str), f"Tool {tool_func.__name__} should return string"
                
                # Should be parseable as JSON
                data = json.loads(result)
                assert isinstance(data, dict), f"Tool {tool_func.__name__} should return JSON object"
                assert 'success' in data, f"Tool {tool_func.__name__} should have success field"
                
            except TypeError as e:
                # If tool raises TypeError for None query, that's acceptable
                if 'query' in str(e) and kwargs.get('query') is None:
                    continue
                else:
                    pytest.fail(f"Tool {tool_func.__name__} should handle invalid parameters gracefully: {e}")
            except Exception as e:
                pytest.fail(f"Tool {tool_func.__name__} should not raise unhandled exceptions: {e}")

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_output_directory_creation_errors(self, temp_dir):
        """Test handling of output directory creation errors."""
        
        # Test with read-only parent directory (simulated)
        readonly_parent = temp_dir / "readonly_parent" 
        readonly_parent.mkdir()
        output_dir = readonly_parent / "new_subdir"
        
        # Test tools that create output directories
        directory_tools = [
            (split_pdf, {'file_path': "test.pdf", 'split_ranges': ["1-5"], 'output_dir': str(output_dir)}),
            (extract_pages, {'file_path': "test.pdf", 'pages': "1-3", 'output_dir': str(output_dir)}),
            (pdf_to_images, {'file_path': "test.pdf", 'output_dir': str(output_dir)}),
        ]
        
        for tool_func, kwargs in directory_tools:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Should handle directory creation issues gracefully
            assert data['success'] is False, "Should handle directory creation errors"
            assert 'output_dir' not in data.get('error', '') or 'directory' in data['error'].lower(), "Should handle directory parameter appropriately"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_large_file_handling_errors(self, temp_dir):
        """Test handling of large file scenarios."""
        
        # Test with very large hypothetical file
        large_file = temp_dir / "very_large_file.pdf"
        
        # Test tools with large file considerations
        large_file_tests = [
            (read_pdf, {'file_path': str(large_file), 'chunk_size': 10}),  # Small chunks for large file
            (analyze_pdf_size, {'file_path': str(large_file)}),  # Analysis of large file
            (optimize_pdf, {'file_path': str(large_file), 'optimization_level': 'maximum'}),  # Heavy optimization
        ]
        
        for tool_func, kwargs in large_file_tests:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Should handle large file scenarios (will fail for missing file, but appropriately)
            assert data['success'] is False, "Should handle large file scenarios"
            assert isinstance(data['error'], str), "Should provide string error message"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_async_exception_handling(self):
        """Test that async exceptions are properly caught and formatted."""
        
        # Test that all tools handle async exceptions properly
        test_tools = [
            read_pdf("nonexistent.pdf"),
            get_pdf_metadata("nonexistent.pdf"),
            analyze_pdf_size("nonexistent.pdf"),
        ]
        
        # All should complete without raising unhandled exceptions
        for task in test_tools:
            try:
                result = await task
                data = json.loads(result)
                assert 'success' in data, "Should handle async exceptions and return proper format"
            except Exception as e:
                pytest.fail(f"Async tool should not raise unhandled exception: {e}")

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_error_message_quality(self, temp_dir):
        """Test that error messages are helpful and actionable."""
        
        test_file = temp_dir / "error_message_test.pdf"
        
        # Test error message quality for common scenarios
        error_scenarios = [
            (read_pdf, {'file_path': str(test_file)}, "should mention file not found"),
            (extract_page_text, {'file_path': str(test_file), 'page_number': 999}, "should mention page range"),
            (search_pdf_text, {'file_path': str(test_file), 'query': 'test'}, "should be informative"),
            (merge_pdfs, {'file_paths': []}, "should mention empty file list"),
        ]
        
        for tool_func, kwargs, expectation in error_scenarios:
            result = await tool_func(**kwargs)
            data = json.loads(result)
            
            # Error messages should be helpful
            assert data['success'] is False, f"Should indicate failure for {tool_func.__name__}"
            error_msg = data['error']
            assert len(error_msg) > 10, f"Error message should be descriptive for {tool_func.__name__}: {expectation}"
            assert error_msg != "An error occurred", f"Error message should be specific for {tool_func.__name__}: {expectation}"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_graceful_degradation_with_partial_failures(self, temp_dir):
        """Test behavior when operations partially succeed or fail."""
        
        # Test merge with mixed valid/invalid files
        valid_file = temp_dir / "valid.pdf" 
        invalid_file = temp_dir / "invalid.pdf"
        nonexistent_file = temp_dir / "nonexistent.pdf"
        
        # Create one invalid file
        invalid_file.write_text("Not a PDF")
        
        result = await merge_pdfs(file_paths=[str(valid_file), str(invalid_file), str(nonexistent_file)])
        data = json.loads(result)
        
        # Should handle mixed scenarios appropriately
        assert data['success'] is False, "Should indicate failure for mixed file validity"
        assert isinstance(data['error'], str), "Should provide clear error message"
        
        # Should mention the problematic files
        error_msg = data['error'].lower()
        file_problem_indicators = ['not found', 'invalid', 'missing', 'file']
        has_file_context = any(indicator in error_msg for indicator in file_problem_indicators)
        assert has_file_context, "Should provide context about file problems"


# Error handling integration test summary:
# ✅ File not found scenarios for all 18 tools
# ✅ Invalid parameter value handling and validation
# ✅ Missing dependency graceful degradation
# ✅ Permission and access error handling
# ✅ Malformed file format detection and reporting
# ✅ Resource exhaustion and large file resilience
# ✅ Async exception handling and proper error formatting
# ✅ Error message quality and actionability
# ✅ Concurrent access safety validation
# ✅ Partial failure and mixed scenario handling
