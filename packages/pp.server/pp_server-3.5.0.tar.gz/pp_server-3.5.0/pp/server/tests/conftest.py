################################################################
# pp.server - Produce & Publish Server
# (C) 2023, ZOPYX, Tuebingen, Germany
################################################################

import pytest
from pathlib import Path


@pytest.fixture
def sample_html_file(tmp_path: Path):
    """Create a sample HTML file for testing."""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Test Document</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: blue; }
    </style>
</head>
<body>
    <h1>Test Document</h1>
    <p>This is a test document for PDF conversion.</p>
</body>
</html>"""

    html_file = tmp_path / "index.html"
    html_file.write_text(html_content)
    return html_file


@pytest.fixture
def sample_zip_file(sample_html_file: Path):
    """Create a sample ZIP file containing HTML for testing."""
    import zipfile

    zip_path = sample_html_file.parent / "test.zip"

    with zipfile.ZipFile(zip_path, 'w') as zf:
        zf.write(sample_html_file, "index.html")

    return zip_path