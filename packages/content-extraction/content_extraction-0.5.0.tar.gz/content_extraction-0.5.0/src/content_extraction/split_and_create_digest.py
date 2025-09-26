from typing import Any
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import sys
import argparse
import hashlib
import json
import logging
from content_extraction.common_std_io import read_input, write_stream_of_obj
from dataclasses import dataclass, field, asdict

from .logging_config import setup_logging


logger = logging.getLogger(__name__)


@dataclass
class Node:
    title: str
    text: str
    level: int
    subsections: list['Node'] | None = field(default_factory=list)


@dataclass
class SectionDigestNode:
    title: str
    text: str
    subsections: list['SectionDigestNode'] = field(default_factory=list)


@dataclass
class ProcessResultNode:
    digest_hash: str
    parent_digest_hash: str
    title: str
    text: str
    section_digest: SectionDigestNode
    language: str


def shorten_text(text: str, max_elements: int = 2, subsections: list[dict[str, Any]] | None = None) -> str:
    """Shorten text by splitting on lines and keeping at most max_elements, appending '...' if truncated."""
    if max_elements == -1:
        return text

    if not text:
        result = ''
        for child in subsections or []:
            result = '<p>Covered topics in this subsection:</p><ul>'
            for child in subsections or []:
                result += f'<li>{child.get("title")}</li>'
            result += '</ul>'
        return result

    DELIM = ''
    lines = text.splitlines()
    if len(lines) <= max_elements:
        if subsections:
            lines.append('...')
        return DELIM.join(lines)
    shortened = lines[:max_elements]
    shortened.append('...')
    return DELIM.join(shortened)


def generate_section_digest(node: dict) -> SectionDigestNode:
    """Generate a section digest string for a node, including its title/text and immediate children."""
    text = node.get('text', '')
    section_digest = SectionDigestNode(title=node.get('title', ''), text=text)
    # Include immediate children
    for child in node.get('subsections') or []:
        child_title = child.get('title')
        child_text = child.get('text')
        length = 1 if text else -1
        short_text = shorten_text(child_text, length, child.get('subsections'))
        section_digest.subsections.append(SectionDigestNode(title=child_title, text=short_text))
    return section_digest


def compute_digest_hash(section_digest: SectionDigestNode) -> str:
    """Compute a BLAKE2b hash of the section digest text as the node ID."""
    h = hashlib.blake2b(digest_size=16)
    section_digest_text = str(section_digest)
    h.update(section_digest_text.encode('utf-8'))
    return h.hexdigest()


def process_node(node: dict, parent_digest_hash: str | None = None) -> list[dict[str, str | dict[str, Any]]]:
    """
    Recursively process a node and its subsections, returning a flat list of nodes.
    """
    text = node.get('text', '')
    section_digest = generate_section_digest(node)
    digest_hash = compute_digest_hash(section_digest)
    try:
        digest_as_text = str(section_digest)
        language = detect(digest_as_text)
    except LangDetectException:
        logger.warning(f'Failed to detect language for {digest_as_text[:128]=}')
        language = None
    result = ProcessResultNode(
        **{
            'digest_hash': digest_hash,
            'parent_digest_hash': parent_digest_hash,
            'title': node.get('title'),
            'text': text,
            'section_digest': section_digest,
            'language': language,
        }
    )
    result = asdict(result)
    nodes = [result]
    for child in node.get('subsections') or []:
        nodes += process_node(child, parent_digest_hash=digest_hash)
    return nodes


def main():
    parser = argparse.ArgumentParser(
        description=('Split hierarchical JSON into JSON Lines with node summaries and parent digests.')
    )
    parser.add_argument('input', nargs='?', help='Input JSON file (defaults to stdin)')
    parser.add_argument('-o', '--output', help='Output JSONL file (defaults to stdout)')
    args = parser.parse_args()

    setup_logging()

    logger.info(f'Processing input from {args.input or "stdin"}')
    content = read_input(args.input)
    data_list = json.loads(content)
    logger.info(f'Found {len(data_list)} top-level sections to process.')

    nodes = [
        node
        for result_list in (process_node(data, parent_digest_hash=None) for data in data_list)
        for node in result_list
    ]
    write_stream_of_obj(nodes, args.output)
    logger.info(f'Successfully processed and wrote {len(nodes)} nodes to {args.output or "stdout"}.')


if __name__ == '__main__':
    sys.exit(main())
