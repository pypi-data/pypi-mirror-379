import json
import pytest
from pathlib import Path

from content_extraction.semantic_chunk_html import HTMLSectionParser


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def read_html(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        print(html)
        return html


@pytest.mark.parametrize(
    'source_filename,expected_result_filename',
    [
        ('example.html', 'example.json'),
        ('example2.html', 'example2.json'),
    ],
)
def test_example_html(source_filename, expected_result_filename):
    parser = HTMLSectionParser()
    input_file_path = str(Path(__file__).parent / source_filename)
    html = read_html(input_file_path)
    result = parser.parse_sections(html)
    print(json.dumps(result, indent=2))
    expected_result = load_json(Path(__file__).parent / expected_result_filename)

    assert result == expected_result
