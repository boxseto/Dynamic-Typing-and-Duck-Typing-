#
# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Seto Tsz Kin
# Student ID : 1155092585
# Email Addr : 1155092585@link.cuhk.edu.hk
#
from Elf import Elf
from Land import Land
from Map import Map
from Monster import Monster
from NPC import NPC
from Pos import Pos
from Warrior import Warrior
import random

class TheJourney:
    map = None

    def __init__(self):
        self.map = Map()

    def gameStart(self):
        self.map.initializeAll()
        numOfAliveMonsters = self.map.getNumOfAliveMonsters()
        numOfAliveWarriors = self.map.getNumOfAliveWarriors()
        while (numOfAliveMonsters > 0) and (numOfAliveWarriors > 0):
            self.map.printBoard()
            self.map.teleportAll()
            numOfAliveMonsters = self.map.getNumOfAliveMonsters()
            numOfAliveWarriors = self.map.getNumOfAliveWarriors()
            pass
        if numOfAliveMonsters == 0:
            print('Congratulations, all the monsters have been killed.')
        else :
            print('Unfortunately, the mission failed and all the warriors died.')
        pass

if __name__ == "__main__":
    game = TheJourney()
    game.gameStart()
