"""
PDF Reader MCP Server

A comprehensive MCP (Model Context Protocol) server providing 18 powerful PDF processing tools:
- Intelligent text extraction with chunking support
- Advanced OCR with Tesseract (multi-language support)
- Document operations (split, merge, extract pages)
- Image conversion and extraction
- Metadata management and optimization
- PDF compression and optimization

Optimized for easy installation and execution via uvx:
    uvx pdfreadermcp

Also supports direct execution:
    uv run pdfreadermcp
    python -m pdfreadermcp
"""

__version__ = "0.1.0"
__author__ = "lihongwen"
__email__ = "1062316792@qq.com"
__description__ = "MCP server for comprehensive PDF processing with 18 specialized tools"
__license__ = "MIT"
__url__ = "https://github.com/lihongwen/pdfreadermcp"

from .__main__ import main

__all__ = [
    "main",
    "__version__", 
    "__author__",
    "__email__",
    "__description__",
    "__license__",
    "__url__"
]