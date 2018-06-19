import copy
import numpy as np
import ast
import matplotlib.pyplot as plt
import random

class Mancala(object):
        
    def __init__(self):
        self.board = [0, 2, 2, 2, 2, 0, 2, 2, 2, 2]
        self.player = 1
        
    def reset(self):
        self.board = [0, 2, 2, 2, 2, 0, 2, 2, 2, 2]
        self.player = 1

    def getBoard(self):
        return self.board
    
    
    def winner(self):
        if self.board[0] < self.board[5]:
            return 1
        elif self.board[0] >  self.board[5]:
            return 2
        else:
            return 0

        
    def changePlayer(self):
        self.player = 1 if self.player == 2 else 2        
          
    def getUtility(self):
        if (self.board[0] + self.board[5]) == 16:
            if self.board[0]< self.board[5]:
                return 1 if self.player is 1 else -1
            elif self.board[0]> self.board[5]:
                return 1 if self.player is 2 else -1  
            else:
                return 0
        else:
            return None
        

    def isOver(self):
        return self.getUtility() is not None
        
        
    def getMoves(self):
        moves = []
        if self.player is 1:
            for x in range(1,5):
                if self.getBoard()[x] is not 0:
                    moves.append((x,self.board[x]))
        elif self.player is 2:
            for x in range(6,10):
                if self.getBoard()[x] is not 0:
                    moves.append((x,self.board[x]))
        return moves


    def __str__(self):
        print(" --------------------------------\n",
            "|" ,self.board[0],"| " , self.board[9], " | " , self.board[8]," | ",self.board[7]," | " , self.board[6],  " |   |\n",
              "|   |-----------------------|   |\n",          "|   | " ,
            self.board[1]," | " , self.board[2]," | " , self.board[3]," | " , self.board[4]," | ", self.board[5],"|\n",
              "--------------------------------", ) 
        return ""
    
    
    def cleanUp(self):
        check1=0
        check2=0
        for stones in range(1,5):
            check1 += self.board[stones]
        for stones in range(6,10):
            check2 += self.board[stones]
        if ((check1 is 0) or (check2 is 0)):
            self.board[5] += check1
            self.board[0] += check2
            for spots in range (1,10):
                if spots is not 5:
                    self.board[spots]= 0
        return
    
    def makeMove(self, move):
        #this is just the set up so i can keep track of thing like the start index and the old board
        index = move[0]
               
        #this goes while the indexed spot is not empty
        #we update the index to the next spot, check to see if your player x and not in player y's goal move stone from 
        #the start spot and add stone to the indexed spot
        while(self.board[move[0]]):
            index = ((index + 1) % 10)
            if self.player is 1 and index is not 0:
                self.board[move[0]] -= 1
                self.board[index] +=1
            elif self.player is 2 and index is not 5:
                self.board[move[0]] -= 1
                self.board[index] +=1
        
        #check to see if the last stone landed in the players goal, if so return with out changing players
        if (self.player is 1 and index is 5) or (self.player is 2 and index is 0):
            self.cleanUp()
            return False    
        
        #check to see if the last stone was put in an empty slot and if the oppisite spot is not empty
        #if you are player x and on your side of the board then you 
        #clear all the stones from those 2 sopts and put them in your goal
        if self.board[index] is 1 and self.board[10-index] is not 0 :
            if self.player is 1 and 0 < index < 5:
                self.board[5] += self.board[index] + self.board[10-index]
                self.board[index] = 0
                self.board[10-index] = 0
            elif self.player is 2 and 5 < index < 10:
                self.board[0] += self.board[index] + self.board[10-index]
                self.board[index] = 0
                self.board[10-index] = 0
        
        self.cleanUp()
        return True
    