#!/bin/bash

# Set input directories
INPUT_DIR="applications_data"

# Loop through input files
for file in $INPUT_DIR/*; do
  # Check if file is a regular file (not a directory or symlink)
  if [ -f "$file" ]; then
    # Extract filename without extension
    filename=$(basename "$file")
    
    # Check if file is new (added within the last hour)
    if find "$file" -cmin -60 | grep -q "."; then
      # Process file
      python process_memberships.py $filename
    fi
  fi
done
