#!/usr/bin/bash

# Set PYTHONPATH and run the batch benchmarker
PYTHONPATH=. python tests/batch_benchmarker.py
# move all generated logs to the test logs folder
mv -- *.log tests/logs/
