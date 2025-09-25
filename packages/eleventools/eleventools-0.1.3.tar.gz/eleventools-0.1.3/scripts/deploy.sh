#!/bin/bash

# Deploy to TestPyPI: ./scripts/deploy.sh test
# Deploy to PyPI: ./scripts/deploy.sh

set -e

if [ "$1" = "test" ]; then
    echo "Deploying to TestPyPI..."
    REPO="--repository testpypi"
else
    echo "Deploying to PyPI..."
    REPO=""
fi

# Run tests
uv run pytest tests/

# Clean and build
rm -rf dist/
uv run python -m build

# Validate
uv run twine check dist/*

# Upload
uv run twine upload $REPO dist/*

echo "Deployment complete!"