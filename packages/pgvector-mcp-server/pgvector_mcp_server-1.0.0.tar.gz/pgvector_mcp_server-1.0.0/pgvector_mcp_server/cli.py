#!/usr/bin/env python3
"""
CLI entry point for pgvector MCP Server

This module provides the command-line interface for running the pgvector MCP server.
Only contains server startup functionality - no CLI tools.
"""

import sys
import argparse
from typing import Optional

from .server import mcp


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser for MCP server."""
    parser = argparse.ArgumentParser(
        prog='pgvector-mcp-server',
        description='PostgreSQL pgvector MCP server for vector database management'
    )
    
    parser.add_argument(
        '--host',
        type=str,
        default='localhost',
        help='Host to bind the server (default: localhost)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port to bind the server (default: 8000)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode with verbose logging'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='pgvector-mcp-server 1.0.0'
    )
    
    return parser


def main(args: Optional[list] = None) -> int:
    """
    Main entry point for the MCP server CLI.
    
    Args:
        args: Command line arguments (defaults to sys.argv)
        
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    try:
        parser = create_parser()
        parsed_args = parser.parse_args(args)
        
        # Set debug mode if requested
        if parsed_args.debug:
            import logging
            logging.basicConfig(level=logging.DEBUG)
            print("Debug mode enabled")
        
        print(f"Starting pgvector MCP server...")
        print(f"Configuration will be loaded from environment variables:")
        print(f"  - DATABASE_URL (required)")
        print(f"  - DASHSCOPE_API_KEY (required)")
        
        # Run the MCP server
        mcp.run()
        
        return 0
        
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        return 0
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
