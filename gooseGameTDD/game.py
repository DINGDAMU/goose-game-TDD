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
        self.names=[]
        pass

    def add(self, command):
        """add player's name

        :command: the command by user
        :returns: the system's response

        """
        commandList = str(command).split(" ")
        if commandList[2] in self.names:
            return "Pippo: already existing player"
        else:
            self.names.append(commandList[2])

        getNamesLength = len(self.names)
        if getNamesLength==1:
            self.result +=  " " + str(self.names[0])
        else:
            self.result += ", "+str(self.names[getNamesLength-1])

        return self.result

