"""Contactbox test suite module"""
import unittest
from contactbox.tests.main_test import MainTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MainTestCase))
    return suite
