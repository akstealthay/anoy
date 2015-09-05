import os

from app import app
from app import config
from app import loki

from app.utils import FileIO

if not config.ANOY_HOME_FOLDER:
    loki.error('Please set config.ANOY_HOME_FOLDER in config.py')
    exit()

if not os.path.exists(config.ANOY_HOME_FOLDER):
    loki.error('Please set a valid directory as ANOY_HOME_FOLDER')
    exit()

loki.info('ANOY_HOME_FOLDER set to: %s', config.ANOY_HOME_FOLDER)

# Create blank app data file
filePath = os.path.join(config.ANOY_HOME_FOLDER, config.APP_DATA_FILE_NAME)

if not os.path.exists(filePath):
    initAppData = {'current_profile':'default' ,'profile': {'default':[]}}
    FileIO.dumpAppData(initAppData)
    loki.info('Dumping initial data %s', str(initAppData))

# Start the server
app.run(debug=config.APP_DEBUG)