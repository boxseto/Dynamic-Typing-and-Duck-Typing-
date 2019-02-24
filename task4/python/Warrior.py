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
import random

class Warrior:
    HEALTH_CAP = 40
    pos = None
    index = None
    health = None
    name = None
    map = None
    magic_crystal = None

    def __init__(self, posx, posy, index, map):
        self.pos = Pos(posx, posy)
        self.index = index
        self.map = map
        self.name = 'W' + str(index)
        self.health = self.HEALTH_CAP
        self.magic_crystal = 10

    def teleport(self):
        print('Hi, ' + self.name + '. ' + 'Your position is (%d,%d) and health is %d.' % (self.pos.getX(), self.pos.getY(), self.health))
        print('Specify your target position (Input \'x y\').')
        userinput = input()
        posx, posy = userinput.split()
        posy = int(posy)
        posx = int(posx)
        while (posx == self.pos.getX()) and (posy == self.pos.getY()):
            print('Specify your target position (Input \'x y\'). It should not be the same as the original one.')
            userinput = input()
            posx, posy = userinput.split()
            posx = int(posx)
            posy = int(posy)
            pass
        result = self.map.coming(posx, posy, self)
        if result :
            self.map.setLand(self.pos, None)
            self.pos.setPos(posx, posy)
            self.map.setLand(self.pos, self)
        if self.health <= 0:
            print('Very sorry, '+self.name+' has been killed.')
            self.map.setLand(self.pos, None)
            self.map.deleteTeleportableObj(self)
            self.map.decreaseNumOfWarriors()
        pass

    def talk(self, content):
        print(self.name+': '+content)
        pass

    def increaseCrystal(self, value):
        self.magic_crystal += value;
        pass

    def decreaseCrystal(self, value):
        self.magic_crystal -= value;
        pass

    def increaseHealth(self, value):
        self.health += value;
        if self.health > self.HEALTH_CAP:
            self.health = self.HEALTH_CAP
        pass

    def decreaseHealth(self, value):
        self.health -= value;
        pass

    def getPos(self):
        return self.pos
        pass

    def getName(self):
        return self.name
        pass

    def getHealth(self):
        return self.health
        pass

    def setHealth(self, health):
        self.health = health
        pass

    def getMagic_crystal(self):
        return self.magic_crystal
        pass

    def setMagic_crystal(self, magic_crystal):
        self.magic_crystal = magic_crystal
        pass

    def actionOnWarrior(self,warrior):
        self.talk('Hi, bro. You can call me '+ self.getName() + '.  I am very happy to meet you.  ' + 'I have %d magic crystals.' % self.getMagic_crystal())
        self.talk('The number of your magic crystals is ' + str(warrior.getMagic_crystal())+'.')
        self.talk('Need I share with you some magic crystals?')
        self.talk('You now have following options: ')
        print('1. Yes');
        print('2. No');
        a = input()
        a = int(a)
        if a == 1 :
            value = random.randint(0, self.getMagic_crystal()-2)+2
            if self.getMagic_crystal() > value :
                self.decreaseCrystal(value)
                warrior.increaseCrystal(value)
                warrior.talk('Thanks for your shared %d magic crystals !' % value + self.getName() + '.')
            else :
                self.talk('Very embarrassing, I don\'t have enough crystals.')
                warrior.talk('That is fine, '+ self.getName() + ' ! After all we are all poor sons.')
        return False
        pass
