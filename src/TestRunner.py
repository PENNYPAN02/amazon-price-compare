'''
@author: PANAGIOP
'''

from unittest import TestLoader, TestSuite, TextTestRunner
from AmazonTestCase import AmazonTC


if __name__ == "__main__":
    
    test_loader = TestLoader()
    test_suite = TestSuite(test_loader.loadTestsFromTestCase(AmazonTC))
    test_runner = TextTestRunner()
    test_runner.run(test_suite)
    