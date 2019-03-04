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

import random
from Player import Player

class AI(Player):

    def legal_move(self, i, j, symbol):
        if symbol == 'X':
            opposym = 'O'
        else:
            opposym = 'X'
        haveflag = 0
        #check up
        tempi = i + 1
        tempj = j
        tempflag = 0
        while (tempi < 8) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check down
        tempi = i - 1
        tempj = j
        tempflag = 0
        while (tempi >= 0) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check left
        tempi = i
        tempj = j - 1
        tempflag = 0
        while (tempj >= 0) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempj -= 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check right
        tempi = i
        tempj = j + 1
        tempflag = 0
        while (tempj < 8) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempj += 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check up right
        tempi = i - 1
        tempj = j + 1
        tempflag = 0
        while (tempi >= 0) and (tempj < 8) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
                tempj += 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check up left
        tempi = i - 1
        tempj = j - 1
        tempflag = 0
        while (tempi >= 0) and (tempj >= 0) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
                tempj -= 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check down right
        tempi = i + 1
        tempj = j + 1
        tempflag = 0
        while (tempi < 8) and (tempj < 8) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
                tempj += 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #check down left
        tempi = i + 1
        tempj = j - 1
        tempflag = 0
        while (tempi < 8) and (tempj >= 0) and (haveflag != 1):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
                tempj -= 1
                tempflag = 1
            elif (tempflag == 1) and (self.board[tempi][tempj] == symbol):
                haveflag = 1
                break
            elif (tempflag == 0) and (self.board[tempi][tempj] == symbol):
                break
            elif self.board[tempi][tempj] == ' ':
                break
            pass
        #pass result
        if haveflag == 1:
            return True
        if haveflag == 0:
            return False
        pass

    def nextMove(self,board):
        while True:
            row = random.randint(1,8) - 1
            col = random.randint(1,8) - 1
            if ((board[row][col] == ' ') and legal_move(row, col, self.playerSymbol)) :
                break
            pass
        return [row, col]
        pass
