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

class Human(Player):
    def nextMove(self,board):
        while True:
            userinput = input('Type the row and col to put the disc: ')
            try:
                row, col = userinput.split()
                row = int(row)-1
                col = int(col)-1
            except ValueError:
                print('Invalid Input')
                continue
            if (board[row][col] != ' ') or (col > 8) or (col < 0) or (row > 8) or (row < 0):
                print('Invalid Input')
                #print('human Invalid Input: %d %d'%(row+1,col+1))
            else:
                break
            pass
        return [row, col]
        pass
