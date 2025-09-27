#!/bin/bash
set -e

# Read version from pyproject.toml
VERSION=$(grep -E '^[[:space:]]*version[[:space:]]*=' pyproject.toml \
          | head -n1 \
          | sed -E 's/[[:space:]]*version[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/')
echo "Using version: $VERSION"

# Update manifest.json
jq --arg ver "$VERSION" \
   '.version = $ver | .user_config.version.default = $ver' \
   manifest.json > manifest.tmp.json && mv manifest.tmp.json manifest.json

# Python lib - install dependencies and pipx
python -m pip install --target ./lib pipx click==8.1.8 packaging==24.2

# Install the package itself so pipx can find it
python -m pip install --target ./lib .

# Pack
npx -y @anthropic-ai/mcpb pack . mcp-instana.mcpb
