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

    _occupied_obj = None

    def __init__(self):
        self._occupied_obj = None

    def coming(self, warrior):
        if isinstance(self._occupied_obj, NPC):
            return self._occupied_obj.actionOnWarrior(warrior)
        return True
        pass

    @property
    def occupied_obj(self):
        return self._occupied_obj
        pass

    @occupied_obj.setter
    def occupied_obj(self, occupied_obj):
        self._occupied_obj = occupied_obj
        pass

    def getOccupantName(self):
        if isinstance(self._occupied_obj, NPC):
            return self._occupied_obj.name
        elif type(self._occupied_obj) is Warrior:
            return self._occupied_obj.name
        return None
        pass
