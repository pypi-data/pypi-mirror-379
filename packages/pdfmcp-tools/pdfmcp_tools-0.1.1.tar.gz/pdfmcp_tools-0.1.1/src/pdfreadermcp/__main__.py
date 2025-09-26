"""
Entry point for the PDF Reader MCP server.

This module provides the main entry point for starting the PDF Reader MCP server,
optimized for both direct execution and uvx tool runner compatibility.
"""

import sys
import logging
from typing import NoReturn

from . import __version__
from .server import app


def setup_logging() -> None:
    """Configure logging for the MCP server."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stderr)
        ]
    )


def main() -> NoReturn:
    """
    Main entry point for the PDF Reader MCP server.
    
    Optimized for uvx execution: uvx pdfreadermcp
    Also supports direct execution: python -m pdfreadermcp
    
    The server provides 18 comprehensive PDF processing tools through
    the Model Context Protocol (MCP) interface.
    
    Raises:
        SystemExit: When server startup fails or on shutdown
    """
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"Starting PDF Reader MCP Server v{__version__}")
        logger.info("Providing 18 PDF processing tools via MCP protocol")
        logger.info("Server ready for MCP client connections...")
        
        # Start the FastMCP server
        app.run()
        
    except KeyboardInterrupt:
        logger.info("Received shutdown signal, stopping server...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Failed to start PDF Reader MCP Server: {e}")
        logger.error("Please check your Tesseract OCR installation and dependencies")
        sys.exit(1)


if __name__ == "__main__":
    main()