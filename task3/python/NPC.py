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
from Pos import Pos

class NPC:
    pos = None
    index = None
    name = None
    power = None
    map = None

    def __init__(self, posx, posy, index, map):
        self.map = map
        self.pos = Pos(posx, posy)
        self.index = index

    def talk(self, content):
        print(self.name + ": " + content)
        pass

    def actionOnWarrior(self, warrior):
        return False
        pass

    def setPos(self, pos):
        self.pos = pos
        pass

    def getPos(self):
        return self.pos
        pass

    def setName(self, name):
        self.name = name
        pass

    def getName(self):
        return self.name
        pass

    def getPower(self):
        return self.power
        pass

    def setPower(self, power):
        self.power = power
        pass
