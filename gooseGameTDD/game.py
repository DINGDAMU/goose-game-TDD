# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: game.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2018-04-24 22:28:09
# ###########################
import random


class GooseGame(object):
    """rules of gooseGame"""
    def __init__(self):
        self.result = 'players:'
        self.names = []
        self.playersteps = {}

    def add(self, command):
        """add player's name

        :command: the command by user
        :returns: the system's response

        """
        command_list = str(command).split(" ")
        if command_list[2] in self.names:
            return "Pippo: already existing player"
        else:
            self.names.append(command_list[2])
            self.playersteps[command_list[2]] = "Start"

        name_length = len(self.names)
        if name_length == 1:
            self.result += " " + str(self.names[0])
        else:
            self.result += ", "+str(self.names[name_length-1])

        return self.result

    def move_players(self, move_steps):
        """The steps which player moves

        :moveSteps:the steps which player moves
        :returns: the current player's steps

        """
        move_player_details = move_steps.split(" ")
        move_steps_in_number = move_player_details[2].split(",")
        player_name = move_player_details[1]
        step1 = move_steps_in_number[0]
        step2 = move_player_details[3]
        move_steps_sum = int(step1) + int(step2)
        if self.playersteps[player_name] == "Start":
            info1 = "{name} rolls {details}.".format(
                name=player_name, details=move_player_details[2]
                + " " + move_player_details[3])
            info2 = "{name} moves from {start} to {current}".format(
                name=player_name, start=self.playersteps[player_name],
                current=move_steps_sum)
            self.playersteps[player_name] = move_steps_sum
            return info1+" "+info2+"."

        info1 = "{name} rolls {details}.".format(
            name=player_name, details=move_player_details[2]
            + " " + move_player_details[3])
        current_steps = self.playersteps[player_name]+move_steps_sum
        info2 = "{name} moves from {start} to {current}".format(
            name=player_name, start=self.playersteps[player_name],
            current=current_steps)
        if current_steps == 6:
            info2 = "{name} moves from {start} to {current}".format(
                name=player_name, start=self.playersteps[player_name],
                current="The Bridge")
            info3 = "{name} jumps to {jumps}".format(name=player_name,
                                                     jumps=12)
            self.playersteps[player_name] = 12
            return info1+" "+info2+". "+info3

        results = info1+" "
        if current_steps == 5 or current_steps == 9 or current_steps == 14\
           or current_steps == 18 or current_steps == 23\
                or current_steps == 27:
            picture_steps = current_steps + move_steps_sum
            info3 = "{name} moves again and goes to {pictureSteps}".format(
                name=player_name, pictureSteps=picture_steps)
            results += info2+", The Goose. "+info3
            while (picture_steps == 9 or picture_steps == 14
                   or picture_steps == 18 or picture_steps == 23
                   or picture_steps == 27):
                picture_steps += move_steps_sum
                info3 = ", The Goose. " + "{name} moves again and\
 goes to {pictureSteps}".format(name=player_name, pictureSteps=picture_steps)
                results += info3
            self.playersteps[player_name] = picture_steps
            return results

        for name in self.names:
            if self.playersteps[name] == current_steps:
                prank_steps = current_steps - move_steps_sum
                info4 = "On {position} there is {name_player}, who returns to\
 {prank}".format(position=current_steps, name_player=name, prank=prank_steps)
                return info1 + " " + info2 + ". " + info4

        if current_steps == 63:
            self.playersteps[player_name] = current_steps
            return info1 + " " + info2 + "." + "{name} Wins!!".format(
                name=player_name)
        elif current_steps > 63:
            back_steps = current_steps - 63
            current_steps = 63 - back_steps
            info2 = "{name} moves from {start} to {current}".format(
                name=player_name, start=self.playersteps[player_name],
                current=63)
            self.playersteps[player_name] = current_steps
            return info1 + " " + info2 + ". " +\
                "{name} bounces! {name} returns to {current}".format(
                    name=player_name, current=current_steps)

        return info1 + " " + info2+"."

    def dice_roll(self):
        """dice roll two times
        :returns: dice results

        """
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        return str(num1)+", "+str(num2)
