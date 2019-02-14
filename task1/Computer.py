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
from Player import Player
import random

class Computer(Player):
    def nextMove(self,board):
        while True:
            row = random.randint(1,8) - 1
            col = random.randint(1,8) - 1
            if (board[row][col] == ' '):
                break
            pass
        return [row, col]
        pass
