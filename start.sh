#!/bin/bash

#
# Setup Phase
#

echo "[SHELL] Setting up the execution environment"

if [ ! -d ./fric ]; then
    echo "[SHELL] Setting up new virtual environment"
    virtualenv --clear --no-wheel fric
fi
source fric/bin/activate

echo "[SHELL] Installing required python packages"
pip install -r requirements.txt -q

#
# Execution Phase
#

python run.py

#
# Breakdown Phase
#

echo "[SHELL] Destroying the execution environment"

deactivate