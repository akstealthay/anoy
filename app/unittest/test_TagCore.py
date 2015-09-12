#
# Unit Tests for api/AppDataCore.py
#
import os
import unittest

from ..api import TagCore
from ..api import AppDataCore

from ..utils.logger import logger

class TagCoreTest(unittest.TestCase):

    def test_addTag(self):
        newTag = 'New Tag 1'
        newProfile = 'New Profile 1'

        oldAppData = AppDataCore.getAppData()

        error, response = TagCore.addTag(newTag, newProfile)

        assert error is not None
        assert response is None

        newAppData = AppDataCore.getAppData()

        assert oldAppData == newAppData

        error, response = TagCore.addProfile(newProfile)

        if error:
            logger.error('Error adding new profile %s', newProfile)
            return
        
        error, response = TagCore.addTag(newTag, newProfile)

        assert error is None
        assert response is not None

        newAppData = AppDataCore.getAppData()

        assert newAppData['profile'].has_key(newProfile) is True

    def test_addProfile(self):
        newProfile = 'New Profile 2'

        oldAppData = AppDataCore.getAppData()

        assert oldAppData['profile'].has_key(newProfile) is False

        error, response = TagCore.addProfile(newProfile)

        assert error is None
        assert response is not None

        newAppData = AppDataCore.getAppData()

        assert newAppData['profile'].has_key(newProfile) is True

    def test_removeTag(self):
        tagName = 'New Tag 3'
        profileName = 'New Profile 3'

        error, response = TagCore.addProfile(profileName)

        assert error is None
        assert response is not None

        error, response = TagCore.addTag(tagName, profileName)

        appData = AppDataCore.getAppData()

        assert error is None
        assert response is not None
        assert tagName in appData['profile'][profileName]

        error, response = TagCore.removeTag(tagName, profileName)

        assert error is None
        assert response is not None

        appData = AppDataCore.getAppData()

        assert tagName not in appData['profile'][profileName]

    def test_removeProfile(self):
        profileName = 'New Profile 4'

        error, response = TagCore.addProfile(profileName)

        appData = AppDataCore.getAppData()

        assert error is None
        assert response is not None
        assert appData['profile'].has_key(profileName) == True

        error, response = TagCore.removeProfile(profileName)

        appData = AppDataCore.getAppData()

        assert error is None
        assert response is not None
        assert appData['profile'].has_key(profileName) == False

    def setUp(self):
        initAppData = {'current_profile':'default' ,'profile': {'default':[]}}
        logger.debug('Dumping initial info %s', initAppData)
        AppDataCore.dumpAppData(initAppData)