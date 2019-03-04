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

import sys
import random

class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        while True:
            print('Please choose player %d (%s):' % (playerNum, symbol))
            print('1. Human\n2. Computer Player')
            choice = input('Your choice is: ')
            try:
                choice = int(choice)
            except ValueError:
                print('Invalid Input.')
                continue
            if (choice != 1) and (choice != 2):
                print('Invalid Input.')
            else:
                break
            pass
        if choice == 1:
            print('Player %s is Human.'% symbol)
            return Human(symbol)
        else:
            print('Player %s is Computer.'% symbol)
            return Computer(symbol)
        pass

    def startGame(self):
        #basic logic
        self.player1 = self.createPlayer('O', 1)
        self.player2 = self.createPlayer('X', 2)
        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

        while not self.gameBoard.check_ending():
            current_player = [self.player1,self.player2][self.turn]
            print('Player %s\'s turn.'% current_player.playerSymbol)
            if self.gameBoard.check_legal_move(current_player.playerSymbol):
                while True:
                    pos = current_player.nextMove(self.gameBoard.board)
                    row = pos[0]
                    col = pos[1]
                    if self.gameBoard.legal_move(row,col,current_player.playerSymbol):
                        break
                    else:
                        if type(current_player) is Human :
                            print('Invalid Input')
                            print('main Invalid Input: %d %d'%(row+1,col+1))
                pass
                #self.gameBoard.board[row][col] = current_player.playerSymbol
                #self.gameBoard.printGameBoard()
                #self.gameBoard.board[row][col] = ' '
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            else:
                print('There is no valid move for Player %s' % current_player.playerSymbol)
            self.turn = 1 - self.turn

            self.gameBoard.printGameBoard()

        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')

class Player:
    def __init__(self, symbol):
        self.playerSymbol = symbol
    def nextMove(self, board):
        pass

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

class GameBoard:
    board = None
    def __init__(self, board=None):
        if board == None:
            self.board = None
        else:
            board = board

    def init_gameBoard(self):
        self.board = [[' ']*8,[' ']*8,[' ']*8,[' ']*8,[' ']*8,[' ']*8,[' ']*8,[' ']*8]
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'
        self.board[3][3] = 'X'
        self.board[4][4] = 'X'
        pass

    def check_ending(self):
        #check whether the game is over or not
        #return True or False
        if self.check_legal_move('X') or self.check_legal_move('O'):
            return False
        else:
            return True
        pass

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

    def check_legal_move(self,symbol):
        #check if their is a legal move given symbol
        #return True or False
        haveflag = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ' ':
                    if self.legal_move(i, j, symbol):
                        #print('Symbol %s legal in %d, %d' % (symbol, i+1, j+1))
                        haveflag = 1
                if haveflag == 1:
                    break
            if haveflag == 1:
                break
        if haveflag == 1:
            return True
        if haveflag == 0:
            return False
        pass

    def check_winner(self):
        #return a list[s1,s2], represent the total number for O and X
        blackX = 0
        whiteO = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'O':
                    whiteO += 1
                elif self.board[i][j] == 'X':
                    blackX += 1
        return [whiteO, blackX]
        pass

    def execute_flip(self, pos, symbol):
        i = pos[0]
        j = pos[1]
        if symbol == 'X':
            opposym = 'O'
        else:
            opposym = 'X'
        #print('flipping: %d %d %s'%(i+1,j+1,symbol))
        self.board[i][j] = symbol
        #check up
        tempi = i + 1
        tempj = j
        while (tempi < 8):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while tempi != i:
                    self.board[tempi][tempj] = symbol
                    tempi -= 1
                    pass
                break
            pass
        #check down
        tempi = i - 1
        tempj = j
        while (tempi >= 0):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while tempi != i:
                    self.board[tempi][tempj] = symbol
                    tempi += 1
                    pass
                break
            pass
        #check left
        tempi = i
        tempj = j - 1
        while (tempj >= 0):
            if self.board[tempi][tempj] == opposym :
                tempj -= 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while tempj != j:
                    self.board[tempi][tempj] = symbol
                    tempj += 1
                    pass
                break
            pass
        #check right
        tempi = i
        tempj = j + 1
        while (tempj < 8):
            if self.board[tempi][tempj] == opposym :
                tempj += 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while tempj != j:
                    self.board[tempi][tempj] = symbol
                    tempj -= 1
                    pass
                break
            pass
        #check up right
        tempi = i - 1
        tempj = j + 1
        while (tempi >= 0) and (tempj < 8):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
                tempj += 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while (tempi != i) and (tempj != j):
                    self.board[tempi][tempj] = symbol
                    tempi += 1
                    tempj -= 1
                    pass
                break
            pass
        #check up left
        tempi = i - 1
        tempj = j - 1
        while (tempi >= 0) and (tempj >= 0):
            if self.board[tempi][tempj] == opposym :
                tempi -= 1
                tempj -= 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while (tempi != i) and (tempj != j):
                    self.board[tempi][tempj] = symbol
                    tempi += 1
                    tempj += 1
                    pass
                break
            pass
        #check down right
        tempi = i + 1
        tempj = j + 1
        while (tempi < 8) and (tempj < 8):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
                tempj += 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while (tempi != i) and (tempj != j):
                    self.board[tempi][tempj] = symbol
                    tempi -= 1
                    tempj -= 1
                    pass
                break
            pass
        #check down left
        tempi = i + 1
        tempj = j - 1
        while (tempi < 8) and (tempj >= 0):
            if self.board[tempi][tempj] == opposym :
                tempi += 1
                tempj -= 1
            elif self.board[tempi][tempj] == ' ':
                break
            elif self.board[tempi][tempj] == symbol:
                while (tempi != i) and (tempj != j):
                    self.board[tempi][tempj] = symbol
                    tempi -= 1
                    tempj += 1
                    pass
                break
            pass
        pass

    def printGameBoard(self):
        print('   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
        print('------------------------------------')
        for i in range(8):
            print(' %d |'% (i+1), end='', flush=True)
            for j in range(8):
                print(' %c |'% self.board[i][j], end='', flush=True)
            print()
            print('------------------------------------')
        pass

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

if __name__ == "__main__":
    othello = Othello()
    othello.startGame()
