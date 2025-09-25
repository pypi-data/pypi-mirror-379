#!/bin/bash

# Production PyPI Upload Script for personal-doc-library
# Usage: ./upload_to_pypi.sh

set -e

echo "🚀 PyPI Upload Script for personal-doc-library"
echo "============================================="

# Check if distribution files exist
if [ ! -f "dist/personal_doc_library-0.1.0-py3-none-any.whl" ] || [ ! -f "dist/personal_doc_library-0.1.0.tar.gz" ]; then
    echo "❌ Distribution files not found in dist/"
    echo "Run: venv_mcp/bin/python -m build"
    exit 1
fi

# Confirm this is intentional
echo ""
echo "⚠️  WARNING: This will upload to PRODUCTION PyPI"
echo "Package: personal-doc-library v0.1.0"
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "❌ Upload cancelled"
    exit 1
fi

# Check for token
if [ -z "$PYPI_TOKEN" ]; then
    echo ""
    echo "⚠️  PyPI token not found in environment"
    echo ""
    echo "To set your token:"
    echo "  export PYPI_TOKEN='your-token-here'"
    echo ""
    echo "Or create ~/.pypirc with:"
    echo "[pypi]"
    echo "username = __token__"
    echo "password = your-token-here"
    echo ""
    read -p "Enter your PyPI token (or press Ctrl+C to cancel): " PYPI_TOKEN
    if [ -z "$PYPI_TOKEN" ]; then
        echo "❌ Token required"
        exit 1
    fi
fi

# Install/upgrade twine if needed
echo "📦 Ensuring twine is installed..."
venv_mcp/bin/pip install --quiet --upgrade twine

# Upload to PyPI
echo ""
echo "📤 Uploading to PyPI..."
echo ""

if [ -f ~/.pypirc ] && grep -q "^\\[pypi\\]" ~/.pypirc; then
    # Use .pypirc if configured
    venv_mcp/bin/python -m twine upload dist/*
else
    # Use environment variables
    TWINE_USERNAME=__token__ TWINE_PASSWORD=$PYPI_TOKEN \
    venv_mcp/bin/python -m twine upload dist/*
fi

echo ""
echo "✅ Upload complete!"
echo ""
echo "🎉 Your package is now available on PyPI!"
echo ""
echo "📋 Installation:"
echo "   pip install personal-doc-library"
echo "   uv pip install personal-doc-library"
echo "   pipx install personal-doc-library  # For CLI tools"
echo ""
echo "📦 Package page:"
echo "   https://pypi.org/project/personal-doc-library/"
echo ""
echo "🏷️  Don't forget to:"
echo "   1. Create a GitHub release with tag v0.1.0"
echo "   2. Update README with PyPI badges"
echo "   3. Announce the release!"