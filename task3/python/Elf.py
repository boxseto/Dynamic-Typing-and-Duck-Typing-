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
        self.setName('E' + str(index))
        self.setPower(random.randint(0,self.MAGIC_CAP - 5) + 5)

    def actionOnWarrior(self,warrior):
        self.talk('My name is '+ self.getName() + '.  Welcome to my home.  ' + 'My magic power is %d.' % self.getPower())
        self.talk('Your magic crystal is ' + warrior.getMagic_crystal()+'.')
        self.talk('Do you need my help?')
        self.talk('You now have following options: ')
        print('1. Yes');
        print('2. No');
        a = input()
        a = int(a)

        if a == 1 :
            value = TheJourney.rand.nextInt(self.getPower()-2)+2
            if warrior.getMagic_crystal() > value :
                warrior.decreaseCrystal(value)
                warrior.increaseHealth(value)
                warrior.talk('Thanks for your help!' + self.getName + '.')
            else :
                warrior.talk('Very embarrassing, I don\'t have enough crystals.')
        return False
        pass
