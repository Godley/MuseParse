import unittest
from MuseParse.classes.Output.helpers import setupLilypondClean as setupLilypond
import os

def load_tests(loader, tests, pattern):
    ''' Discover and load all unit tests in all files named ``*_test.py`` in ``./src/``
    '''
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('', pattern='test*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    setupLilypond('C:\\Program Files (x86)\\LilyPond\\usr\\bin')
    unittest.main()