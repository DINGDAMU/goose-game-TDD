# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: test_game.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2018-04-24 22:28:16
# ###########################

import unittest
from unittest.mock import Mock
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
        goose.move_players("move Pippo 4, 2")
        steps = goose.move_players("move Pippo 2, 3")
        self.assertEqual("Pippo rolls 2, 3. Pippo moves from 6 to 11.",
                         steps)

    def testVictory(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 30, 30")
        steps = goose.move_players("move Pippo 1, 2")
        self.assertEqual("Pippo rolls 1, 2. Pippo moves from 60 to 63." +
                         "Pippo Wins!!", steps)

    def testBounces(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 30, 30")
        steps = goose.move_players("move Pippo 3, 2")
        self.assertEqual("Pippo rolls 3, 2. Pippo moves from 60 to 63. " +
                         "Pippo bounces! Pippo returns to 61", steps)
    def testDice(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 2, 2")
        goose.dice_roll = Mock(return_value="1, 2")
        move_commands = "move Pippo " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("Pippo rolls 1, 2. Pippo moves from 4 to 7.", steps)

    def testBridge(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 2, 2")
        goose.dice_roll = Mock(return_value="1, 1")
        move_commands = "move Pippo " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("Pippo rolls 1, 1. Pippo moves from 4 to The Bridge.\
 Pippo jumps to 12", steps)

    def testPictureJumps(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 1, 2")
        goose.dice_roll = Mock(return_value="1, 1")
        move_commands = "move Pippo " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("Pippo rolls 1, 1. Pippo moves from 3 to 5, The Goose.\
 Pippo moves again and goes to 7", steps)

    def testMultiplePictureJumps(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.move_players("move Pippo 5, 5")
        goose.dice_roll = Mock(return_value="2, 2")
        move_commands = "move Pippo " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("Pippo rolls 2, 2. Pippo moves from 10 to 14, The Goose.\
 Pippo moves again and goes to 18, The Goose. Pippo moves again\
 and goes to 22", steps)

    def testPrank(self):
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.add("add player Pluto")
        goose.move_players("move Pippo 10, 5")
        goose.move_players("move Pluto 7, 10")
        goose.dice_roll = Mock(return_value="1, 1")
        move_commands = "move Pippo " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("Pippo rolls 1, 1. Pippo moves from 15 to 17. On 17 \
there is Pluto, who returns to 15", steps)

    def testTerminate(self):
        """chekc if terminate works
        :returns: terminate or not

        """
        goose = GooseGame()
        goose.add("add player Pippo")
        goose.add("add player Pluto")
        goose.move_players("move Pippo 30, 30")
        goose.dice_roll = Mock(return_value="1, 2")
        move_commands = "move Pippo " + str(goose.dice_roll())
        goose.move_players(move_commands)
        move_commands = "move Pluto " + str(goose.dice_roll())
        steps = goose.move_players(move_commands)
        self.assertEqual("The game is finished!", steps)

    def testDiceRoll(self):
        """test Dice Rolls
        :returns: the dice result

        """
        goose = GooseGame()
        num1 = 1
        num2 = 2
        goose.dice_roll = Mock(return_value="1, 2")
        self.assertEqual(str(num1) + ", " + str(num2), goose.dice_roll())


if __name__ == "__main__":
    unittest.main()
