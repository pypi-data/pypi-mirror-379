"""
PDF text search tool for finding and locating text content within PDF documents.
Based on Context7 example code patterns for PyPDF text extraction.
"""

import asyncio
import re
from pathlib import Path
from typing import Optional, Dict, Any, Union, List, Tuple
import json

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

from ..utils.file_handler import FileHandler
from ..utils.cache import PDFCache


class PDFTextSearcher:
    """
    PDF text search tool supporting:
    - Search for text/phrases across PDF pages
    - Case-sensitive and case-insensitive search
    - Regular expression search patterns
    - Context extraction around matches
    - Page and position information
    
    Based on Context7 PyPDF text extraction best practices.
    """
    
    def __init__(self):
        """Initialize the PDF text searcher with cache."""
        self.cache = PDFCache(max_entries=25, max_age_seconds=1800)  # 30 minutes
        self.file_handler = FileHandler()
        
        # Search configuration
        self.default_context_chars = 100  # Characters before/after match
        self.max_matches_per_page = 50    # Limit matches per page
    
    async def search_pdf_text(
        self,
        file_path: Union[str, Path],
        query: str,
        pages: Optional[str] = None,
        case_sensitive: bool = False,
        regex_search: bool = False,
        context_chars: int = 100,
        max_matches: int = 100
    ) -> str:
        """
        Search for text content across PDF pages.
        
        Based on Context7 example: page.extract_text() with search logic.
        
        Args:
            file_path: Path to PDF file
            query: Text to search for (or regex pattern if regex_search=True)
            pages: Page range (e.g., "1,3,5-10,-1") or None for all pages
            case_sensitive: Whether search is case-sensitive
            regex_search: Whether to treat query as regex pattern
            context_chars: Number of characters to show around matches
            max_matches: Maximum number of matches to return
            
        Returns:
            JSON string with search results and match locations
        """
        
        if not PdfReader:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        if not query or not query.strip():
            return self._error_response("Search query cannot be empty")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Generate cache key
            cache_key = f"search_{pdf_path.name}_{hash(query)}_{pages}_{case_sensitive}_{regex_search}"
            cached_result = self.cache.get(cache_key, str(pdf_path))
            if cached_result:
                return cached_result
            
            # Context7 pattern: Initialize PDF reader
            reader = PdfReader(str(pdf_path))
            total_pages = len(reader.pages)
            
            # Parse page range
            if pages:
                page_numbers = self.file_handler.parse_page_range(pages, total_pages)
                if not page_numbers:
                    return self._error_response("No valid pages specified")
            else:
                page_numbers = list(range(1, total_pages + 1))
            
            # Prepare search pattern
            search_flags = 0 if case_sensitive else re.IGNORECASE
            if regex_search:
                try:
                    search_pattern = re.compile(query, search_flags)
                except re.error as e:
                    return self._error_response(f"Invalid regex pattern: {str(e)}")
            else:
                # Escape special regex characters for literal search
                escaped_query = re.escape(query)
                search_pattern = re.compile(escaped_query, search_flags)
            
            # Search across specified pages
            all_matches = []
            total_matches = 0
            pages_with_matches = 0
            
            for page_num in page_numbers:
                if total_matches >= max_matches:
                    break
                
                try:
                    # Context7 pattern: Extract text from page
                    page = reader.pages[page_num - 1]  # 0-based indexing
                    page_text = page.extract_text()
                    
                    if not page_text.strip():
                        continue  # Skip empty pages
                    
                    # Find all matches on this page
                    page_matches = []
                    for match in search_pattern.finditer(page_text):
                        if total_matches >= max_matches:
                            break
                        if len(page_matches) >= self.max_matches_per_page:
                            break
                        
                        match_start = match.start()
                        match_end = match.end()
                        matched_text = match.group()
                        
                        # Extract context around the match
                        context_start = max(0, match_start - context_chars)
                        context_end = min(len(page_text), match_end + context_chars)
                        context_text = page_text[context_start:context_end]
                        
                        # Calculate line number (approximate)
                        lines_before_match = page_text[:match_start].count('\n')
                        line_number = lines_before_match + 1
                        
                        # Get the line containing the match
                        lines = page_text.split('\n')
                        current_line = ""
                        if line_number <= len(lines):
                            current_line = lines[line_number - 1] if lines else ""
                        
                        match_info = {
                            'page': page_num,
                            'line_number': line_number,
                            'character_position': match_start,
                            'matched_text': matched_text,
                            'context': context_text.strip(),
                            'current_line': current_line.strip(),
                            'match_length': len(matched_text)
                        }
                        
                        page_matches.append(match_info)
                        total_matches += 1
                    
                    if page_matches:
                        all_matches.extend(page_matches)
                        pages_with_matches += 1
                        
                except Exception as e:
                    # Skip problematic pages but continue processing
                    continue
            
            # Sort matches by page number, then by position
            all_matches.sort(key=lambda x: (x['page'], x['character_position']))
            
            result = {
                'success': True,
                'operation': 'search_pdf_text',
                'source_pdf': str(pdf_path),
                'search_query': query,
                'search_options': {
                    'case_sensitive': case_sensitive,
                    'regex_search': regex_search,
                    'context_chars': context_chars,
                    'pages_searched': pages if pages else 'all'
                },
                'summary': {
                    'total_matches': total_matches,
                    'pages_with_matches': pages_with_matches,
                    'pages_searched': len(page_numbers),
                    'match_limit_reached': total_matches >= max_matches
                },
                'matches': all_matches[:max_matches]  # Ensure we don't exceed limit
            }
            
            # Ensure all Path objects are converted to strings before JSON serialization
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            result_json = json.dumps(result, ensure_ascii=False, indent=2, default=str)
            self.cache.set(cache_key, result_json, str(pdf_path))
            return result_json
            
        except Exception as e:
            return self._error_response(f"Error during PDF text search: {str(e)}")
    
    async def extract_page_text(
        self,
        file_path: Union[str, Path],
        page_number: int,
        extraction_mode: str = "default"
    ) -> str:
        """
        Extract text from a specific PDF page with various extraction options.
        
        Based on Context7 example: page.extract_text() with different modes.
        
        Args:
            file_path: Path to PDF file
            page_number: Page number to extract (1-based)
            extraction_mode: Text extraction mode ('default', 'layout', 'simple')
            
        Returns:
            JSON string with extracted text and metadata
        """
        
        if not PdfReader:
            return self._error_response("PyPDF library not available. Install with: pip install pypdf")
        
        try:
            pdf_path = Path(file_path)
            if not pdf_path.exists():
                return self._error_response(f"PDF file not found: {file_path}")
            
            # Context7 pattern: Initialize PDF reader and get page
            reader = PdfReader(str(pdf_path))
            total_pages = len(reader.pages)
            
            if not (1 <= page_number <= total_pages):
                return self._error_response(f"Page number {page_number} is out of range (1-{total_pages})")
            
            page = reader.pages[page_number - 1]  # 0-based indexing
            
            # Context7 pattern: Extract text based on mode
            if extraction_mode == "layout":
                # Extract text preserving layout
                extracted_text = page.extract_text(
                    extraction_mode="layout",
                    layout_mode_space_vertically=False
                )
            elif extraction_mode == "simple":
                # Simple extraction with minimal processing
                extracted_text = page.extract_text(0)  # Only upright text
            else:
                # Default extraction
                extracted_text = page.extract_text()
            
            # Text analysis
            text_stats = {
                'total_characters': len(extracted_text),
                'total_words': len(extracted_text.split()) if extracted_text else 0,
                'total_lines': extracted_text.count('\n') + 1 if extracted_text else 0,
                'is_empty': not extracted_text.strip()
            }
            
            result = {
                'success': True,
                'operation': 'extract_page_text',
                'source_pdf': str(pdf_path),
                'page_number': page_number,
                'total_pages': total_pages,
                'extraction_mode': extraction_mode,
                'text_statistics': text_stats,
                'extracted_text': extracted_text
            }
            
            # Ensure all Path objects are converted to strings
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error extracting page text: {str(e)}")
    
    async def find_and_highlight_text(
        self,
        file_path: Union[str, Path],
        query: str,
        pages: Optional[str] = None,
        case_sensitive: bool = False
    ) -> str:
        """
        Find text and return pages with highlighting information.
        
        Args:
            file_path: Path to PDF file
            query: Text to search for
            pages: Page range or None for all pages
            case_sensitive: Whether search is case-sensitive
            
        Returns:
            JSON string with pages and text positions for highlighting
        """
        
        try:
            # Use the main search function
            search_result_json = await self.search_pdf_text(
                file_path=file_path,
                query=query,
                pages=pages,
                case_sensitive=case_sensitive,
                regex_search=False,
                context_chars=50,
                max_matches=200
            )
            
            search_result = json.loads(search_result_json)
            
            if not search_result.get('success', False):
                return search_result_json
            
            # Group matches by page for highlighting
            page_highlights = {}
            for match in search_result.get('matches', []):
                page_num = match['page']
                if page_num not in page_highlights:
                    page_highlights[page_num] = []
                
                page_highlights[page_num].append({
                    'start_pos': match['character_position'],
                    'end_pos': match['character_position'] + match['match_length'],
                    'matched_text': match['matched_text'],
                    'line_number': match['line_number']
                })
            
            result = {
                'success': True,
                'operation': 'find_and_highlight_text',
                'source_pdf': str(Path(file_path)),
                'search_query': query,
                'summary': search_result['summary'],
                'page_highlights': page_highlights
            }
            
            # Ensure all Path objects are converted to strings
            def convert_paths_to_strings(obj):
                if isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_paths_to_strings(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_paths_to_strings(item) for item in obj]
                return obj
            
            result = convert_paths_to_strings(result)
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)
            
        except Exception as e:
            return self._error_response(f"Error in find and highlight: {str(e)}")
    
    def _error_response(self, message: str) -> str:
        """Generate standardized error response."""
        return json.dumps({
            'success': False,
            'error': str(message),
            'operation': 'pdf_text_search'
        }, ensure_ascii=False, indent=2, default=str)
