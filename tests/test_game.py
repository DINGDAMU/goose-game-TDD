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
        self.assertEqual("players: Pippo", goose.add("add player Pippo"))

    def testAddTwoNames(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        result = goose.add("add player Pluto")
        self.assertEqual("players: Pippo, Pluto", result)

    def testAddDuplicatedName(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        result = goose.add("add player Pippo")
        self.assertEqual("Pippo: already existing player", result)

    def testMovePippoFromStart(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        steps = goose.move_players("move Pippo 4, 2")
        self.assertEqual("Pippo rolls 4, 2. Pippo moves from Start to 6.",
                         steps)

    def testMovePlutoFromStart(self):
        goose = GooseGame()
        goose.add("add player Pluto")
        steps = goose.move_players("move Pluto 2, 2")
        self.assertEqual("Pluto rolls 2, 2. Pluto moves from Start to 4.",
                         steps)

    def testMovePippoFromSix(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        steps = goose.move_players("move Pippo 4, 2")
        steps = goose.move_players("move Pippo 2, 3")
        self.assertEqual("Pippo rolls 2, 3. Pippo moves from 6 to 11.",
                         steps)

    def testVictory(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        steps = goose.move_players("move Pippo 30, 30")
        steps = goose.move_players("move Pippo 1, 2")
        self.assertEqual("Pippo rolls 1, 2. Pippo moves from 60 to 63." +
                         "Pippo Wins!!", steps)

    def testBounces(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        steps = goose.move_players("move Pippo 30, 30")
        steps = goose.move_players("move Pippo 3, 2")
        self.assertEqual("Pippo rolls 3, 2. Pippo moves from 60 to 63. " +
                         "Pippo bounces! Pippo returns to 61", steps)


if __name__ == "__main__":
    unittest.main()
