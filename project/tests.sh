#!/bin/bash

export PYTHONPATH=$(pwd)/..

echo "Running unit tests..."
pytest ../tests/test_pipeline.py

echo "Running system tests..."
pytest ../tests/test_system.py