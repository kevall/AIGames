import copy
import numpy as np
import ast
import matplotlib.pyplot as plt
import random

class TTT(object):

    def __init__(self): 
        self.movesExplored = 0
        self.board = [' ']*9
        self.player = 1
        
    def reset(self): 
        self.movesExplored = 0
        self.board = [' ']*9
        self.player = 1
      

    def getBoard(self):
        return self.board
    
    def getMoves(self):
        moves = self.locations(' ')
        return moves

    def locations(self, c):
        return [i for i, mark in enumerate(self.board) if mark == c]

    

    def winner(self):
        whereX = self.locations('X')
        whereO = self.locations('O')
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        isXWon = any([all([wi in whereX for wi in w]) for w in wins])
        isOWon = any([all([wi in whereO for wi in w]) for w in wins])
        if isXWon:
            return 1
        elif isOWon:
            return 2
        elif ' ' not in self.board:
            return 0
        else:
            return None 

    def isOver(self):
        return self.winner() is not None

    #update this
    def makeMove(self, move):
        self.movesExplored += 1
        if self.player == 1:
            self.board[move] = 'X'
        else :
            self.board[move] = 'O'
        return True
        

    def changePlayer(self):
         self.player = 1 if self.player == 2 else 2
        
    
    def __str__(self):
        s = '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*self.board)
        return s
    
    