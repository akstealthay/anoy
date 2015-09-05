#
# FileIO.py
#
# Description: All FILE utilities goes here
#

import os
import pickle

from app import config

def dumpAppData(appData):
    """
    Dumps the appData into ANOY_HOME_FOLDER using pickle
    """
    filePath = os.path.join(config.ANOY_HOME_FOLDER, config.APP_DATA_FILE_NAME)

    with open(filePath, 'wb') as appDataFile:
        pickle.dump(appData, appDataFile)

def loadAppData():
    """
    Loads the appData from ANOY_HOME_FOLDER using pickle
    """
    filePath = os.path.join(config.ANOY_HOME_FOLDER, config.APP_DATA_FILE_NAME)

    with open(filePath, 'rb') as appDataFile:
        appData = pickle.load(appDataFile)
        return appData

def readFile(filePath):
    """
    Reads the file file_path and returns the data or appropriate error
    """
    response = {}

    try:
        with open(filePath, 'rb') as dataFile:
            response['raw'] = dataFile.read()
    except IOError as e:        
        response['error'] = e.strerror

    return response