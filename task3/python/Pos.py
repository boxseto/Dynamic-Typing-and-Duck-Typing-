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
    _x = None
    _y = None

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def setPos(self, x, y):
        self._x = x
        self._y = y
        pass

    @property
    def x(self):
        return self._x
        pass

    @property
    def y(self):
        return self._y
        pass
