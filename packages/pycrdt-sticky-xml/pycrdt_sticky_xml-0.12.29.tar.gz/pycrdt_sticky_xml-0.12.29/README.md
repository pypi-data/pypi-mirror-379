# pycrdt-sticky-xml

A fork of [pycrdt](https://github.com/y-crdt/pycrdt) that adds sticky_index support for XML types (XmlElement and XmlText).

## What's New

This fork extends the original pycrdt library by adding `sticky_index` functionality to XML types:

- **XmlElement.sticky_index()**: Create sticky indices for XML element children
- **XmlText.sticky_index()**: Create sticky indices within XML text content

## Installation

### From PyPI (when published)

```bash
pip install pycrdt-sticky-xml
```

### Development Installation

For development, you need Rust installed (via [rustup](https://rustup.rs/)):

```bash
# Clone the repository
git clone https://github.com/yourusername/pycrdt-sticky-xml.git
cd pycrdt-sticky-xml

# Install with uv (recommended)
uv pip install -e .

# Or build with maturin
source "$HOME/.cargo/env"  # If Rust installed via rustup
uv run maturin develop
```

**Note**: The Python module is imported as `pycrdt_sticky_xml` (with underscores), even though the package name uses hyphens.

## Usage

```python
from pycrdt_sticky_xml import Doc, XmlFragment, XmlElement, XmlText, Assoc

# Create a document with XML content
doc = Doc()
frag = doc.get("content", type=XmlFragment)

# Add XML text
text = XmlText("Hello World")
frag.children.append(text)

# Create a sticky index at position 5
idx = text.sticky_index(5, Assoc.AFTER)

# Insert text before the sticky position
text.insert(0, "Say ")

# The sticky index maintains its semantic position
print(idx.get_index())  # Now points to position 9 (after "Say Hello")
```

## Features

- All features from the original pycrdt
- Sticky indices for XmlElement children
- Sticky indices for XmlText content
- Full compatibility with Yrs collaborative editing

## Running Tests

```bash
# Install test dependencies
uv pip install pydantic pytest-mypy-testing trio

# Run tests
uv run pytest

# Run specific test file
uv run pytest tests/test_xml.py -v
```

## Original Project

This is a fork of [pycrdt](https://github.com/y-crdt/pycrdt). All credit for the core functionality goes to the original authors.

## License

MIT License (same as original pycrdt)