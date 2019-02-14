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

from GameBoard import GameBoard
from Human import Human
from Computer import Computer

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


if __name__ == "__main__":
    othello = Othello()
    othello.startGame()
