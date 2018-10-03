#!/bin/bash

# Get current dir from script location
DIR="$( cd "$( dirname "${BASH_SOURCE}" )" >/dev/null && pwd )"

# Enable virtualenv
cd $DIR
. venv/bin/activate

# Install Python libs
pip install -qr requirements.txt

# Start development server
python metrics/app.py
