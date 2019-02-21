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
from Warrior import Warrior

class Land:

    occupied_obj = None

    def __init__(self):
        self.occupied_obj = None

    def coming(warrior):
        if type(self.occupied_obj) is NPC:
            return self.occupied_obj.actionOnWarrior(warrior)
        return True
        pass

    def getOccupied_obj(self):
        return self.occupied_obj
        pass

    def setOccupied_obj(self, occupied_obj):
        self.occupied_obj = occupied_obj
        print('receieved object' + str(type(occupied_obj)))
        pass

    def getOccupantName(self):
        if isinstance(self.occupied_obj, NPC):
            return self.occupied_obj.getName()
        elif type(self.occupied_obj) is Warrior:
            return self.occupied_obj.getName()
        return None
        pass
