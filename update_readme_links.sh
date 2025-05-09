#!/bin/bash

# Update links in each language README file
for file in docs/languages/README_*.md; do
  sed -i '' 's|\[English\](../README.md)|[English](../../README.md)|g' "$file"
done

echo "All README links updated successfully!" 