from app import app

import os
import unittest

class AppTestCase(unittest.TestCase):

def containsAny(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    return 1 in [c in str for c in set]

   def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get('/')
        assert containsAny('visitors',response)

if __name__ == '__main__':
    unittest.main()
