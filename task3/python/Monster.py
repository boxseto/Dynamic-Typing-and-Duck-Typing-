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
        self.setName('M' + str(index))
        self.setPower(random.randint(0, self.DAMAGE_CAP - 5) + 5)

    def actionOnWarrior(warrior):
        self.talk('I am the monster ' + self.getName() + '.  Here is my territory.  ' + 'My damage power is %d.' % self.getPower())
        self.talk('Your health is ' + warrior.getHealth() + '.')
        self.talk('Do you really want to challenge me?')
        self.talk('You now have following options: ')
        print('1. Yes')
        print('2. No')
        a = input()
        if a == 1 :
            if warrior.getHealth() > self.getPower() :
                warrior.decreaseHealth(self.getPower)
                warrior.increaseCrystal(TheJourney.rand.nextInt(5) + 5)
                warrior.talk('Nice, I have killed the monster ' + self.getName() + '.')
                self.map.decreaseNumOfAliveMonsters()
                return True
            warrior.decreaseHealth(self.getPower())
        return False
        pass
