#!/bin/bash

#
# Setup Phase
#

echo "[SHELL] Setting up the execution environment"

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