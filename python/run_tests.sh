#!/usr/bin/bash

# Debugging: Check current directory and environment
echo "Current directory: $(pwd)"
echo "PYTHONPATH before: $PYTHONPATH"

# Set PYTHONPATH to the current directory (project root)
export PYTHONPATH=$(pwd)

# Debugging: Check PYTHONPATH after setting it
echo "PYTHONPATH after setting: $PYTHONPATH"

# Run the batch benchmarker script
echo "Running batch benchmarker..."
python tests/batch_benchmarker.py

# Run pytest to execute all tests in the tests directory
echo "Running tests with pytest..."
pytest tests

# Move all generated logs to the test logs folder
echo "Moving log files..."
mv -- *.log tests/logs/
