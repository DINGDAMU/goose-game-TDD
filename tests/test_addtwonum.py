#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from goose-game-TDD.addtwonum import *
class TestClass(unittest.TestCase):
    """Test case docstring."""
    def test_Sample(self):
        self.assertEqual(3,sumofnum(2,1))

if __name__ == "__main__":
    unittest.main()
