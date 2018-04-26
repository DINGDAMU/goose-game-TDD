# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################
# File Name: game.py
# Author: dingdamu
# Mail: dingdamu@gmail.com
# Created Time: 2018-04-24 22:28:09
# ###########################


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
        move_steps_sum = int(move_steps_in_number[0])+int(
            move_player_details[3])
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
        if current_steps == 63:
            self.playersteps[player_name] = current_steps
            return info1 + " " + info2 + "." + "{name} Wins!!".format(
                name=player_name)
        if current_steps > 63:
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
