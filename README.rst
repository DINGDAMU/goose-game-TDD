goose-game-TDD
==============

.. image:: https://www.travis-ci.org/DINGDAMU/goose-game-TDD.png 
   :target: https://www.travis-ci.org/DINGDAMU/goose-game-TDD  
   :alt: Latest Travis CI build status
.. image:: https://coveralls.io/repos/github/DINGDAMU/goose-game-TDD/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/DINGDAMU/goose-game-TDD?branch=master

A TDD exercise


Requirements
------------
- You may use whatever programming language you prefer. Use something that you know well.
- You should commit your code on GitHub or any other SCM repository you prefer (e.g. bitbucket, gitlab, etc) and send us the link.
- You should release your work under an OSI-approved open-source license of your choice.
- You should deliver the sources of your application, with a README that explains how to compile and run it.

**IMPORTANT:** Implement the requirements focusing on writing the best code you can produce.

Features
--------
1. Add players
--------------
As a player, I want to add me to the game so that I can play.

**Scenarios:**
^^^^^^^^^^^^^^
1. Add Player
^^^^^^^^^^^^^

    If there is no participant

    the user writes: "add player Pippo"

    the system responds: "players: Pippo"

    the user writes: "add player Pluto"

    the system responds: "players: Pippo, Pluto"


2. Duplicated Player
^^^^^^^^^^^^^^^^^^^^

   If there is already a participant "Pippo"

   the user writes: "add player Pippo"

   the system responds: "Pippo: already existing player"


2. Move a player
----------------
As a player, I want to move the marker on the board to make the game progress

**Scenarios:**
^^^^^^^^^^^^^^
1. Start
^^^^^^^^
   
   If there are two participants "Pippo" and "Pluto" on space "Start"

   the user writes: "move Pippo 4, 2"

   the system responds: "Pippo rolls 4, 2. Pippo moves from Start to 6"

   the user writes: "move Pluto 2, 2"

   the system responds: "Pluto rolls 2, 2. Pluto moves from Start to 4"

   the user writes: "move Pippo 2, 3"

   the system responds: "Pippo rolls 2, 3. Pippo moves from 6 to 11"
   

3. Win
------
As a player, I win the game if I land on space "63"

**Scenarios:**
^^^^^^^^^^^^^^
1. Victory
^^^^^^^^^^

   If there is one participant "Pippo" on space "60"

   the user writes: "move Pippo 1, 2"

   the system responds: "Pippo rolls 1, 2. Pippo moves from 60 to 63. Pippo Wins!!"

2. Winning with the exact dice shooting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   If there is one participant "Pippo" on space "60"

   the user writes: "move Pippo 3, 2"

   the system responds: "Pippo rolls 3, 2. Pippo moves from 60 to 63. Pippo bounces! Pippo returns to 61"

4. The game throws the dice
---------------------------
As a player, I want the game throws the dice for me to save effort

**Scenarios:**
^^^^^^^^^^^^^^
1. Dice roll
^^^^^^^^^^^^
   If there is one participant "Pippo" on space "4"

   assuming that the dice get 1 and 2

   when the user writes: "move Pippo"

   the system responds: "Pippo rolls 1, 2. Pippo moves from 4 to 7"

5. Space "6" is "The Bridge"
----------------------------
As a player, when I get to the space "The Bridge", I jump to the space "12"

**Scenarios:**
^^^^^^^^^^^^^^
1. Get to "The Bridge"
^^^^^^^^^^^^^^^^^^^^^^

   If there is one participant "Pippo" on space "4"
   assuming that the dice get 1 and 1

   when the user writes: "move Pippo"

   the system responds: "Pippo rolls 1, 1. Pippo moves from 4 to The Bridge. Pippo jumps to 12"


6. If you land on "The Goose", move again
-----------------------------------------
As a player, when I get to a space with a picture of "The Goose", I move forward again by the sum of the two dice rolled before

The spaces 5, 9, 14, 18, 23, 27 have a picture of "The Goose"

**Scenarios:**
^^^^^^^^^^^^^^
1. Single Jump
^^^^^^^^^^^^^^

   If there is one participant "Pippo" on space "3"

   assuming that the dice get 1 and 1

   when the user writes: "move Pippo"

   the system responds: "Pippo rolls 1, 1. Pippo moves from 3 to 5, The Goose. Pippo moves again and goes to 7"


2. Multiple Jump
^^^^^^^^^^^^^^^^
   If there is one participant "Pippo" on space "10"

   assuming that the dice get 2 and 2

   when the user writes: "move Pippo"

   the system responds: "Pippo rolls 2, 2. Pippo moves from 10 to 14, The Goose. Pippo moves again and goes to 18, The Goose. Pippo moves again and goes to 22"


7. Prank 
------------------------
As a player, when I land on a space occupied by another player, I send him to my previous position so that the game can be more entertaining.

**Scenarios:**
^^^^^^^^^^^^^^
1. Prank
^^^^^^^^

   If there are two participants "Pippo" and "Pluto" respectively on spaces "15" and "17"

   assuming that the dice get 1 and 1

   when the user writes: "move Pippo"

   the system responds: "Pippo rolls 1, 1. Pippo moves from 15 to 17. On 17 there is Pluto, who returns to 15"
   

8. Terminate the game
---------------------
If someone wins the game, terminate the game.

**Scenarios:**
^^^^^^^^^^^^^^
1. Terminate
^^^^^^^^^^^^

    If there are two participants "Pippo" and "Pluto"

    assuming that Pippo reaches 63 
    
    either Pippo or Plutto wants to roll agian 
    
    the system responds: "The game is finished!"

Licence
-------

MIT license
^^^^^^^^^^^
Copyright <2018> <DING DAMU>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Authors
-------

`goose-game-TDD` was written by `DAMU DING <dingdamu@gmail.com>`_.
