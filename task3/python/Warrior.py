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

class Warrior:
    _HEALTH_CAP = 40
    _pos = None
    _index = None
    _health = None
    _name = None
    _map = None
    _magic_crystal = None

    def __init__(self, posx, posy, index, map):
        self._pos = Pos(posx, posy)
        self._index = index
        self._map = map
        self._name = 'W' + str(index)
        self._health = self._HEALTH_CAP
        self._magic_crystal = 10

    def teleport(self):
        print('Hi, ' + self._name + '. ' + 'Your position is (%d,%d) and health is %d.' % (self._pos.x, self._pos.y, self._health))
        print('Specify your target position (Input \'x y\').')
        userinput = input()
        posx, posy = userinput.split()
        posy = int(posy)
        posx = int(posx)
        while (posx == self._pos.x) and (posy == self._pos.y):
            print('Specify your target position (Input \'x y\'). It should not be the same as the original one.')
            userinput = input()
            posx, posy = userinput.split()
            posx = int(posx)
            posy = int(posy)
            pass
        result = self._map.coming(posx, posy, self)
        if result :
            self._map.setLand(self._pos, None)
            self._pos.setPos(posx, posy)
            self._map.setLand(self._pos, self)
        if self._health <= 0:
            print('Very sorry, '+self._name+' has been killed.')
            self._map.setLand(self._pos, None)
            self._map.deleteTeleportableObj(self)
            self._map.decreaseNumOfWarriors()
        pass

    def talk(self, content):
        print(self._name+': '+content)
        pass

    def increaseCrystal(self, value):
        self._magic_crystal += value;
        pass

    def decreaseCrystal(self, value):
        self._magic_crystal -= value;
        pass

    def increaseHealth(self, value):
        self._health += value;
        if self._health > self._HEALTH_CAP:
            self._health = self._HEALTH_CAP
        pass

    def decreaseHealth(self, value):
        self._health -= value;
        pass

    @property
    def pos(self):
        return self._pos

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, _health):
        self._health = _health
        pass

    @property
    def magic_crystal(self):
        return self._magic_crystal
        pass

    @magic_crystal.setter
    def magic_crystal(self, _magic_crystal):
        self._magic_crystal = _magic_crystal
        pass
