#!/bin/bash

# Publish script for Point Topic MCP to PyPI using UV
set -e

# Get token from .pypirc if it exists
if [ -f "$HOME/.pypirc" ]; then
    echo "📄 Reading token from ~/.pypirc..."
    PYPI_TOKEN=$(grep "password = " ~/.pypirc | sed 's/.*password = //' | tr -d ' ')
    if [ -z "$PYPI_TOKEN" ]; then
        echo "❌ Could not find token in ~/.pypirc"
        exit 1
    fi
else
    echo "❌ No ~/.pypirc file found!"
    echo "Set up your PyPI credentials first"
    exit 1
fi

echo "🔨 Building package with UV..."
uv build

echo "📦 Built package files:"
ls -la dist/

echo "🚀 Uploading to PyPI with UV..."
uv publish --token "$PYPI_TOKEN"

echo "✅ Successfully published to PyPI!"
echo ""
echo "Users can now install with:"
echo "  pip install point-topic-mcp"
echo ""
echo "And use with:"
echo "  point-topic-mcp"
