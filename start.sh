#!/bin/bash

#
# Setup Phase
#

echo "Setting up the execution environment"

echo "Activating python virtual environment"
source fric/bin/activate

echo "Installing required python packages"
pip install -r requirements.txt -q

#
# Execution Phase
#

echo "Starting up the app"
python run.py

#
# Breakdown Phase
#

echo "Destroying the execution environment"
echo "Deactivating python virtual environment"

deactivate