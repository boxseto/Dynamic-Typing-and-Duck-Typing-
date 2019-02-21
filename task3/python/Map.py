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
from Land import Land
from Warrior import Warrior
import random
from Pos import Pos
from Monster import Monster
from Elf import Elf

class Map:
    teleportable_obj = []
    lands = None
    D = 10
    e = None
    m = None
    w = None
    totalNum = 0
    numOfAliveMonsters = None
    numOfAliveWarriors = None

    def __init__(self):
        self.lands = []
        self.e = random.randint(0,1) + 2
        self.m = random.randint(0,1) + 2
        self.w = 1
        self.totalNum = self.m + self.e + self.w
        self.numOfAliveMonsters = self.m
        self.numOfAliveWarriors = self.w

    def initializeAll(self):
        print('Welcome to Kafustrok. Light blesses you. ')
        self.lands = [[Land() for x in range(self.D)] for y in range(self.D)]
        for i in range(self.totalNum):
            pos = self.getUnOccupiedPosition()
            print(str(pos.getX()) + '   ' + str(pos.getY()))
            if i < self.m :
                self.lands[pos.getX()][pos.getY()].setOccupied_obj(Monster(pos.getX(), pos.getY(), i, self))
                print(self.lands[pos.getX()][pos.getY()].getOccupantName())
            elif i < (self.m+self.e) :
                self.lands[pos.getX()][pos.getY()].setOccupied_obj(Elf(pos.getX(), pos.getY(), i-self.m, self))
                print(self.lands[pos.getX()][pos.getY()].getOccupantName())
            else:
                self.lands[pos.getX()][pos.getY()].setOccupied_obj(Warrior(pos.getX(), pos.getY(), i-self.m-self.e, self))
                self.teleportable_obj.append(self.lands[pos.getX()][pos.getY()].getOccupied_obj())
                print(self.lands[pos.getX()][pos.getY()].getOccupantName())
            pass
        pass

    def teleportAll(self):
        for obj in self.teleportable_obj:
            if type(obj) is Warrior:
                obj.teleport()
            pass
        pass

    def coming(self, posx, posy, warrior):
        return self.lands[posx][posy].coming(warrior)
        pass

    def setLand(self, pos, occupied_obj):
        self.lands[pos.getX()][pos.getY()].setOccupied_obj(occupied_obj)
        pass

    def deleteTeleportableObj(self, obj):
        index = self.teleportable_obj.indexOf(obj)
        self.teleportable_obj.set(index, None)
        pass

    def getUnOccupiedPosition(self):
        randx = random.randint(0,self.D-1)
        randy = random.randint(0,self.D-1)
        while self.lands[randx][randy].getOccupied_obj() != None:
            randx = random.randint(0, self.D-1)
            randy = random.randint(0, self.D-1)
            pass
        return Pos(randx, randy)
        pass

    def printBoard(self):
        printObject = [[' ']*self.D]*self.D
        for i in range(self.D):
            for j in range(self.D):
                occupantName = self.lands[i][j].getOccupantName();
                if occupantName == None:
                    occupantName = '  '
                printObject[i][j] = occupantName
                pass
            pass
        print(' ', end='', flush=True)
        for i in range(self.D):
            print('| %d  '%i, end='', flush=True)
            pass
        print('|')
        for i in range(int(self.D*5.5)):
            print('-',end='', flush=True)
            pass
        print('')
        for row in range(self.D):
            print(row,end='',flush=True)
            for col in range(self.D):
                print('| %s '%printObject[row][col], end='', flush=True)
                pass
            print('|')
            for i in range(int(self.D*5.5)):
                print('-', end='', flush=True)
                pass
            print('')
        pass

    def decreaseNumOfAliveMonsters(self):
        self.numOfAliveMonsters -= 1
        pass

    def decreaseNumOfWarriors(self):
        self.numOfAliveWarriors -= 1
        pass

    def getNumOfAliveMonsters(self):
        return self.numOfAliveMonsters
        pass

    def setNumOfAliveMonsters(self, numOfAliveMonsters):
        self.numOfAliveMonsters = numOfAliveMonsters
        pass

    def getNumOfAliveWarriors(self):
        return self.numOfAliveWarriors
        pass

    def setNumOfAliveWarriors(self, numOfAliveWarriors):
        self.numOfAliveWarriors = numOfAliveWarriors
        pass
