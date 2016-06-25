#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from runner.runner_tests.test_mountain import TestMountain
from runner.runner_tests.test_sensei import TestSensei
from runner.runner_tests.test_helper import TestHelper

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(TestMountain))
    suite.addTests(loader.loadTestsFromTestCase(TestSensei))
    suite.addTests(loader.loadTestsFromTestCase(TestHelper))
    return suite

if __name__ == '__main__':
    res = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not res.wasSuccessful())
