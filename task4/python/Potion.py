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
import random
from Pos import Pos

class Potion:
    _AID_CAP = 10;
    _pos = None
    _index = None
    _name = None
    _power = None
    _map = None

    def __init__(self, posx, posy, index, map):
        self._map = map
        self._pos = Pos(posx, posy)
        self._index = index
        self.name = 'P' + str(index)
        self.power = random.randint(0,self._AID_CAP - 5) + 5

    def actionOnWarrior(self,warrior):
        warrior.talk('Very good, I got additional healing potion '+ self.name +'.')
        warrior.increaseHealth(self.power)
        self._map.decreaseNumOfPotion()
        self._map.deleteTeleportableObj(self)
        return True
        pass

    def talk(self, content):
        print(self._name + ": " + content)
        pass

    @property
    def pos(self):
        return self._pos
        pass

    @pos.setter
    def pos(self, _pos):
        self._pos = _pos
        pass

    @property
    def name(self):
        return self._name
        pass

    @name.setter
    def name(self, _name):
        self._name = _name
        pass

    @property
    def power(self):
        return self._power
        pass

    @power.setter
    def power(self, _power):
        self._power = _power
        pass
