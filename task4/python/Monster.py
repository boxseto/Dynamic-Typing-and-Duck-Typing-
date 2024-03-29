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
from NPC import NPC
import random

class Monster(NPC):
    DAMAGE_CAP = 20
    def __init__(self, posx, posy, index, map):
        super(Monster, self).__init__(posx, posy, index, map)
        self.name = ('M' + str(index))
        self.power = (random.randint(0, self.DAMAGE_CAP - 5) + 5)

    def actionOnWarrior(self, warrior):
        self.talk('I am the monster ' + self.name + '.  Here is my territory.  ' + 'My damage power is %d.' % self.power)
        self.talk('Your health is ' + str(warrior.health) + '.')
        self.talk('Do you really want to challenge me?')
        self.talk('You now have following options: ')
        print('1. Yes')
        print('2. No')
        a = input()
        a = int(a)
        if a == 1 :
            if warrior.health > self.power :
                warrior.decreaseHealth(self.power)
                warrior.increaseCrystal(random.randint(0, 5) + 5)
                warrior.talk('Nice, I have killed the monster ' + self.name + '.')
                self._map.decreaseNumOfAliveMonsters()
                return True
            warrior.decreaseHealth(self.power)
        return False
        pass
