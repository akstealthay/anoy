import AppDataCore

from ..utils import FileIO

def addTag(tag, profile):
    """
    Adds a new tag `tag` to profile `profile`

    Error message is populated when
        1. profile does not exist
        2. tag already exists
    """
    error, response = None, None
    appData = AppDataCore.getAppData()

    # assert: `profile` should exist before adding tag to it
    if not appData['profile'].has_key(profile):
        # `profile` does not exist hence error
        error = 'Profile %s does not exist, please create one.' % (profile)
    else:
        # `profile` does exists
        tempSet = set(appData['profile'][profile])

        if tag in tempSet:
            error = 'Tag %s already exist' % (tag)
        else:
            tempSet.add(tag)
            appData['profile'][profile] = list(tempSet)
            AppDataCore.dumpAppData(appData)
            response = 'Tag %s added successfully to profile %s' % (tag, profile)

    return error, response

def removeTag(tag, profile):
    """
    Removes the tag `tag` from profile `profile`

    Error message is populated when
        1. profile does not exist
        2. tag does not exists
    """
    error, response = None, None
    appData = AppDataCore.getAppData()

    if not appData['profile'].has_key(profile):
        # `profile` does not exist hence error
        error = 'Profile %s does not exist, please create one.' % (profile)
    else:
        # `profile` does exists
        tempSet = set(appData['profile'][profile])

        if tag not in tempSet:
            error = 'Tag %s does not exist' % (tag)
        else:
            tempSet.remove(tag)
            appData['profile'][profile] = list(tempSet)
            AppDataCore.dumpAppData(appData)
            response = 'Tag %s removed successfully from profile %s' % (tag, profile)

    return error, response

def addProfile(profile):
    """
    Adds a new profile `profile`

    Error message is populated when
        1. profile already exist
    """
    error, response = None, None
    appData = AppDataCore.getAppData()

    # assert: `profile` should not exist before adding tag to it
    if appData['profile'].has_key(profile):
        # `profile` does exist hence error
        error = 'Profile %s already exist' % (profile)
    else:
        # `profile` does not exist
        appData['profile'][profile] = []
        AppDataCore.dumpAppData(appData)
        response = 'Profile %s created successfully' % (profile)

    return error, response

def removeProfile(profile):
    """
    Removes the profile `profile`

    Error message is populated when
        1. profile does not exist
    """
    error, response = None, None
    appData = AppDataCore.getAppData()

    # assert: `profile` should not exist before adding tag to it
    if not appData['profile'].has_key(profile):
        # `profile` does exist hence error
        error = 'Profile %s does not exist' % (profile)
    else:
        # `profile` exist
        appData['profile'].pop(profile)
        AppDataCore.dumpAppData(appData)
        response = 'Profile %s removed successfully' % (profile)

    return error, response