#
# FileIO.py
#
# Description: All FILE utilities goes here
#

import os

def readFile(filePath):
    """
    Reads the file file_path and returns the data or appropriate error
    """
    error, response = None, {}

    try:
        with open(filePath, 'rb') as dataFile:
            response['raw'] = dataFile.read()
    except IOError as e:        
        error = e.strerror

    return error, response