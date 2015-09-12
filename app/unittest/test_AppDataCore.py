#
# Unit Tests for api/AppDataCore.py
#
import os
import unittest

from ..api import AppDataCore

from ..utils.logger import logger

class AppDataCoreTest(unittest.TestCase):

    def test_getAppData(self):
        expectedOutput = {'current_profile':'default' ,'profile': {'default':[]}}
        actualOutput = AppDataCore.getAppData()
        assert expectedOutput == actualOutput

    def test_dumpAppData(self):
        expectedOutput = {'current_profile':'default' ,'profile': {'default':['Sample Tag 1']}}
        AppDataCore.dumpAppData(expectedOutput)
        actualOutput = AppDataCore.getAppData()
        assert expectedOutput == actualOutput

    def test_getAppDataForKey(self):
        expectedOutput = 'default'
        actualOutput = AppDataCore.getAppDataForKey('current_profile')
        assert expectedOutput == actualOutput

    def setUp(self):
        initAppData = {'current_profile':'default' ,'profile': {'default':[]}}
        logger.debug('Dumping initial info %s', initAppData)
        AppDataCore.dumpAppData(initAppData)