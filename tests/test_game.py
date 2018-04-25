# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: test_game.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2018-04-24 22:28:16
# ###########################

import unittest
from gooseGameTDD.game import *

class TestGame(unittest.TestCase):

    """Test game"""

    def testAddOneName(self):
        goose = GooseGame()
        self.assertEqual("players: Pippo",goose.add("add player Pippo"))
        pass

    def testAddTwoNames(self):
        goose =  GooseGame()
        goose.add("add player Pippo")
        result = goose.add("add player Pluto")
        self.assertEqual("players: Pippo, Pluto", result)
        pass

    def testAddDuplicatedName(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        result = goose.add("add player Pippo")
        self.assertEqual("Pippo: already existing player", result)
        pass

    def test_name(self):
        pass


if __name__ == "__main__":
    unittest.main()
