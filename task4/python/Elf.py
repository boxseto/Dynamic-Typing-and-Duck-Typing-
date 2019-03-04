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

class Elf(NPC):
    MAGIC_CAP = 20;
    def __init__(self, posx, posy, index, map):
        super(Elf, self).__init__(posx, posy, index, map)
        self.name = 'E' + str(index)
        self.power = random.randint(0,self.MAGIC_CAP - 5) + 5

    def actionOnWarrior(self,warrior):
        self.talk('My name is '+ self.name + '.  Welcome to my home.  ' + 'My magic power is %d.' % self.power)
        self.talk('Your magic crystal is ' + str(warrior.magic_crystal)+'.')
        self.talk('Do you need my help?')
        self.talk('You now have following options: ')
        print('1. Yes');
        print('2. No');
        a = input()
        a = int(a)

        if a == 1 :
            value = random.randint(0, self.power-2)+2
            if warrior.magic_crystal > value :
                warrior.decreaseCrystal(value)
                warrior.increaseHealth(value)
                warrior.talk('Thanks for your help!' + self.name + '.')
            else :
                warrior.talk('Very embarrassing, I don\'t have enough crystals.')
        return False
        pass
