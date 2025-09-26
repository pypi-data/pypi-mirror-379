# Build Instructions for PyPI

```shell
# Upgrade to latest dependencies
uv sync --upgrade

# Install build tools
uv pip install build twine

# Clean up any old builds first
rm -rf dist/ build/ *.egg-info/

# Build both wheel and source distribution
uv run python -m build

# Check the build
uv run twine check dist/*

# Upload to PyPI
uv run twine upload dist/*  # Requires token
```
