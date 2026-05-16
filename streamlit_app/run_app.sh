#!/bin/bash

# Customer Retention Intelligence System - Unix/Linux Startup Script
# This script sets up and runs the Streamlit application

echo ""
echo "============================================"
echo "Customer Retention Intelligence System"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ using: apt-get install python3 python3-pip (Ubuntu/Debian)"
    exit 1
fi

echo "✓ Python $(python3 --version | cut -d' ' -f2) found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies installed"

# Run Streamlit application
echo ""
echo "============================================"
echo "Starting application..."
echo "============================================"
echo ""
echo "The application will open at: http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py

deactivate
