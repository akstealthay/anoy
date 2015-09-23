import AppDataCore

from ..utils import FileIO
from ..utils.logger import logger

def isNameValid(name):
    """
    Helps to check whether a profile name or a tag name 'name'
    is valid or not.
    """
    error = None

    if ' ' in name or not name.islower():
        error = 'Invalid name %s' % (name)

    return error

def addTag(tag, profile):
    """
    Adds a new tag `tag` to profile `profile`

    Error message is populated when
        1. profile does not exist
        2. tag already exists
    """
    logger.info('Adding tag %s in profile %s', tag, profile)
    error, response = None, None
    appData = AppDataCore.getAppData()

    # Check if the entered tag name is valid
    error = isNameValid(tag)
    if error:
        response = None
        logger.error('Entered tag name %s contains a whitespace or an uppercase letter', tag)
        error = 'Entered tag name %s contains either a whitespace or an uppercase letter' % (tag)
        return error, response

    # assert: `profile` should exist before adding tag to it
    if not appData['profile'].has_key(profile):
        # `profile` does not exist hence error
        logger.error('Profile %s does not exist', profile)
        error = 'Profile %s does not exist, please create one.' % (profile)
    else:
        # `profile` does exists
        logger.info('Profile %s exists', profile)
        tempSet = set(appData['profile'][profile])

        if tag in tempSet:
            logger.debug('Tag %s already exists in profile %s', tag, profile)
            error = 'Tag %s already exist' % (tag)
        else:
            logger.info('Tag %s does not exist in profile %s hence adding', tag, profile)
            tempSet.add(tag)
            appData['profile'][profile] = list(tempSet)
            AppDataCore.dumpAppData(appData)
            logger.debug('Tag %s added successfully to profile %s', tag, profile)
            response = 'Tag %s added successfully to profile %s' % (tag, profile)

    return error, response

def removeTag(tag, profile):
    """
    Removes the tag `tag` from profile `profile`

    Error message is populated when
        1. profile does not exist
        2. tag does not exists
    """
    logger.info('Removing tag %s from profile %s', tag, profile)
    error, response = None, None
    appData = AppDataCore.getAppData()

    if not appData['profile'].has_key(profile):
        # `profile` does not exist hence error
        logger.error('Profile %s does not exist', profile)
        error = 'Profile %s does not exist, please create one.' % (profile)
    else:
        # `profile` does exists
        logger.info('Profile %s exists', profile)
        tempSet = set(appData['profile'][profile])

        if tag not in tempSet:
            logger.error('Tag %s does not exist in profile %s', tag, profile)
            error = 'Tag %s does not exist' % (tag)
        else:
            logger.info('Tag %s exists in profile %s, hence removing', tag, profile)
            tempSet.remove(tag)
            appData['profile'][profile] = list(tempSet)
            AppDataCore.dumpAppData(appData)
            logger.info('Tag %s removed successfully from profile %s', tag, profile)
            response = 'Tag %s removed successfully from profile %s' % (tag, profile)

    return error, response

def addProfile(profile):
    """
    Adds a new profile `profile`

    Error message is populated when
        1. profile already exist
    """
    logger.info('Adding profile %s', profile)
    error, response = None, None
    appData = AppDataCore.getAppData()

    # Check if the entered profile name is valid
    error = isNameValid(profile)
    if error:
        response = None
        logger.error('Entered profile name %s contains a whitespace or an uppercase letter', profile)
        error = 'Entered profile name %s contains either a whitespace or an uppercase letter' % (profile)
        return error, response

    # assert: `profile` should not exist before adding tag to it
    if appData['profile'].has_key(profile):
        # `profile` does exist hence error
        logger.debug('Profile %s already exists', profile)
        error = 'Profile %s already exist' % (profile)
    else:
        # `profile` does not exist
        logger.info('Profile %s does not exist hence adding', profile)
        appData['profile'][profile] = []
        AppDataCore.dumpAppData(appData)
        logger.debug('Profile %s created successfully', profile)
        response = 'Profile %s created successfully' % (profile)

    return error, response

def removeProfile(profile):
    """
    Removes the profile `profile`

    Error message is populated when
        1. profile does not exist
    """
    logger.info('Removing profile %s', profile)
    error, response = None, None
    appData = AppDataCore.getAppData()

    # assert: `profile` should not exist before adding tag to it
    if not appData['profile'].has_key(profile):
        # `profile` does exist hence error
        logger.error('Profile %s does not exist', profile)
        error = 'Profile %s does not exist' % (profile)
    else:
        # `profile` exist
        logger.info('Profile %s exists hence removing', profile)
        appData['profile'].pop(profile)
        AppDataCore.dumpAppData(appData)
        logger.info('Profile %s removed successfully', profile)
        response = 'Profile %s removed successfully' % (profile)

    return error, response
