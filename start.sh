#
# Setup Phase
#

echo "Setting up the execution environment"

echo "Activating python virtual environment"
source fric/bin/activate

echo "Installing all required packages"
pip install -r requirements.txt

#
# Execution Phase
#

echo "Starting up the app"

#
# Breakdown Phase
#

echo "Destroying the execution environment"
echo "Deactivating python virtual environment"

deactivate
