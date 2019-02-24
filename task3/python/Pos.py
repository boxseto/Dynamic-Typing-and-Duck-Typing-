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

class Pos:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPos(self, x, y):
        self.x = x
        self.y = y
        pass

    def getX(self):
        return self.x
        pass

    def getY(self):
        return self.y
        pass
