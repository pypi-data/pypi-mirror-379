#!/usr/bin/env python3
"""
HTML Content Extraction CLI

A command-line tool for extracting structured content from HTML documents.
Converts HTML sections into hierarchical JSON data with preserved formatting.

Usage:
    python main.py [options] [input_file]

Examples:
    # Read from stdin, output to stdout
    cat example.html | python main.py

    # Read from file, output to stdout
    python main.py input.html

    # Read from stdin, output to file
    python main.py -o output.json

    # Read from file, output to file
    python main.py input.html -o output.json

    # Pretty print JSON output
    python main.py --pretty input.html

    # Verbose mode with debug information
    python main.py --verbose input.html
"""

import sys
import argparse
import json
import logging

from content_extraction.common_std_io import read_input, write_output
from content_extraction.semantic_chunk_html import HTMLSectionParser
from .logging_config import setup_logging


logger = logging.getLogger(__name__)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Extract structured content from HTML documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.html                    # Parse file, output to stdout
  %(prog)s -o output.json input.html     # Parse file, save to JSON
  cat input.html | %(prog)s              # Parse from stdin
  %(prog)s --pretty input.html           # Pretty-printed JSON output
  %(prog)s --verbose input.html          # Show debug information
        """,
    )

    parser.add_argument(
        'input_file',
        nargs='?',
        help='Input HTML file (if not provided, reads from stdin)',
    )

    parser.add_argument(
        '-o',
        '--output',
        metavar='FILE',
        help='Output JSON file (if not provided, writes to stdout)',
    )

    parser.add_argument(
        '--pretty',
        action='store_true',
        help='Pretty-print JSON output with indentation',
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Show verbose output and debug information',
    )

    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()
    setup_logging(level=logging.DEBUG if args.verbose else logging.INFO)

    try:
        # Read input
        if args.input_file:
            logger.debug(f'Reading from file: {args.input_file}')
        else:
            logger.debug('Reading from stdin...')

        html_content = read_input(args.input_file)

        # Parse HTML
        parser = HTMLSectionParser()
        result = parser.parse_sections(html_content)

        # Write output
        write_output(json.dumps(result), args.output)

        logger.debug('Processing completed successfully')

    except KeyboardInterrupt:
        logger.warning('Operation cancelled by user')
        return 1
    except Exception:
        logger.error('An unexpected error occurred', exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
