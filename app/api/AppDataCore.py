import os
import pickle

from app import config

from ..utils.logger import logger

def getAppData():
    """
    Returns the complete application data
    """
    filePath = os.path.join(config.ANOY_HOME_FOLDER, config.APP_DATA_FILE_NAME)

    with open(filePath, 'rb') as appDataFile:
        logger.info("Reading file %s", filePath)
        appData = pickle.load(appDataFile)
        return appData

def dumpAppData(appData):
    """
    Dumps the appData into ANOY_HOME_FOLDER using pickle
    """
    filePath = os.path.join(config.ANOY_HOME_FOLDER, config.APP_DATA_FILE_NAME)

    with open(filePath, 'wb') as appDataFile:
        logger.info("Writing file %s", filePath)
        logger.debug("App Data %s", appData)
        pickle.dump(appData, appDataFile)

def getAppDataForKey(key):
    """
    Returns the application data for a particular key.
    If key does not exist the `None` is returned.

    For example, to get all the profiles from the app data call
    this method as

    >>> getAppDataForKey('profile')

    """
    appData = getAppData()

    logger.info("Reading key %s from app data", key)

    return appData.get(key, None)