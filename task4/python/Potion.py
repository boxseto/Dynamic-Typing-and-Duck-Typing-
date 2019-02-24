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

class Potion(NPC):
    AID_CAP = 10;
    def __init__(self, posx, posy, index, map):
        super(Potion, self).__init__(posx, posy, index, map)
        self.setName('P' + str(index))
        self.setPower(random.randint(0,self.AID_CAP - 5) + 5)

    def actionOnWarrior(self,warrior):
        warrior.talk('Very good, I got additional healing potion '+ self.getName() +'.')
        warrior.increaseHealth(self.getPower())
        self.map.decreaseNumOfPotion()
        self.map.deleteTeleportableObj(self)
        return True
        pass
