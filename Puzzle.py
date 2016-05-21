#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Configuration import Configuration
from Interface import Interface
from Structure import *
from random import randint
from copy import copy, deepcopy

class Puzzle:
    _config	        = None
    _matrix         = None
    _hash           = None
    _matrixFinal    = None
    _interface      = None
    _numberOfInteractions = None
    _biggestSize    = 0

    # Start the configuraton and interface designer
    def __init__(self):
        self._config    = Configuration()
        self._interface = Interface()
        print 'Configuration'


    # compile two matrix:
    #   one to be changed and another
    #   to be references about the end position
    #   return: none
    def createMatrix(self):
        self._hash          = {}
        self._matrix        = [[0 for x in range(self._config.size_puzzle)] for x in range(self._config.size_puzzle)]
        self._matrixFinal   = [[0 for x in range(self._config.size_puzzle)] for x in range(self._config.size_puzzle)]

        value = 1

        for i in range(self._config.size_puzzle):
            for j in range(self._config.size_puzzle):
                if i == self._config.size_puzzle -1 and j == self._config.size_puzzle -1:
                    self._matrix[i][j] = 0
                    self._matrixFinal[i][j] = 0
                else:
                    self._matrix[i][j] = value
                    self._matrixFinal[i][j] = value
                value+=1

    def getMatrixInt(self,matrix):
        valueString = ""
        for i in range(self._config.size_puzzle):
            for j in range(self._config.size_puzzle):
                valueString += str(matrix[i][j])
        return int(valueString)

    def setMatrix(self,matrix):
        self._matrix = matrix

    def getMatrix(self):
        return self._matrix


    # call the interface to print
    #   a pretty matrix
    #   return none
    def printMatrix(self,matrix):
        self._interface.printMatrix(matrix)


    # return the x,y position zero
    #   return: matrix[1]
    def getEmptyPosition(self,matrix):
        for i in range(self._config.size_puzzle):
            for j in range(self._config.size_puzzle):
                if matrix[i][j] == 0:
                    return [i,j]


    # compute the list of movements
    #   possible about the current position
    #   return: list
    def nextMovimentPossibilities(self,matrix):
        positionAtual = self.getEmptyPosition(matrix)
        size = self._config.size_puzzle-1

        # Corner
        #   only 2 possilities
        if positionAtual[0] == 0 and positionAtual[1] == 0:
            return [[1,0],[0,1]]
        if positionAtual[0] == size and positionAtual[1] == 0:
            return [[size-1,0],[size,1]]
        if positionAtual[0] == size and positionAtual[1] == size:
            return [[size,size-1],[size-1,size]]
        if positionAtual[0] == 0 and positionAtual[1] == size:
            return [[0,size-1],[1,size]]

        # Margin
        #   three possibilities
        if positionAtual[0] == 0:
            return [[positionAtual[0],positionAtual[1]-1],[positionAtual[0],positionAtual[1]+1],[positionAtual[0]+1,positionAtual[1]]]
        if positionAtual[0] == size:
            return [[positionAtual[0],positionAtual[1]-1],[positionAtual[0],positionAtual[1]+1],[positionAtual[0]-1,positionAtual[1]]]
        if positionAtual[1] == 0:
            return [[positionAtual[0]-1,positionAtual[1]],[positionAtual[0]+1,positionAtual[1]],[positionAtual[0],positionAtual[1]+1]]
        if positionAtual[1] == size:
            return [[positionAtual[0]-1,positionAtual[1]],[positionAtual[0]+1,positionAtual[1]],[positionAtual[0],positionAtual[1]-1]]

        # Inside
        #   four possibilities
        return [[positionAtual[0]-1,positionAtual[1]],[positionAtual[0]+1,positionAtual[1]],[positionAtual[0],positionAtual[1]-1],[positionAtual[0],positionAtual[1]+1]]

    # Shake the matrix
    #   this method skake based on size Inside
    #   of config (go to config to see more)
    #   return: none
    def shakeMatrix(self,matrix):
        for i in range(self._config.size_shake):
            self._changePositionOnMatrix(matrix)


    # execute one of shakeMatrix possibilities
    #   change both values on matrix
    #   return: none
    def _changePositionOnMatrix(self,matrix):

        positionAtual = self.getEmptyPosition(matrix)
        positionPossibilities = self.nextMovimentPossibilities(matrix)

        choice = randint(0,len(positionPossibilities)-1)

        oldValue = matrix[positionAtual[0]][positionAtual[1]]
        matrix[positionAtual[0]][positionAtual[1]] = matrix[positionPossibilities[choice][0]][positionPossibilities[choice][1]]
        matrix[positionPossibilities[choice][0]][positionPossibilities[choice][1]] = oldValue
        return matrix

    def possiblesPositionsOnMatrix(self,matrix):
        positionAtual = self.getEmptyPosition(matrix)
        positionPossibilities = self.nextMovimentPossibilities(matrix)

        listOfMatrixToReturn = [None] * len(positionPossibilities)

        for i in range(len(positionPossibilities)):

            old_matrix = deepcopy(matrix)
            oldValue = old_matrix[positionAtual[0]][positionAtual[1]]
            old_matrix[positionAtual[0]][positionAtual[1]] = old_matrix[positionPossibilities[i][0]][positionPossibilities[i][1]]
            old_matrix[positionPossibilities[i][0]][positionPossibilities[i][1]] = oldValue

            listOfMatrixToReturn[i] = old_matrix

        return listOfMatrixToReturn

    # check if matrix is the inicial/final matrix
    #   return Boolean
    def isFinalPosition(self,matrix):
        return matrix == self._matrixFinal


    # Algoritm Breadth-first search
    def BFS(self,matrix):
        self._numberOfInteractions = 0
        self._biggestSize = 1
        q = Stack()
        q.push(matrix)
        while not q.isEmpty():
            matrixAtual = q.pop()
            size = q.size()
            self._numberOfInteractions+=1

            if self._biggestSize < size:
                self._biggestSize = size

            if self.isFinalPosition(matrixAtual):
                print 'number Of Interactions'
                print self._numberOfInteractions
                print 'Biggest Size'
                print self._biggestSize
                return  matrixAtual
            else:
                newKey = self.getMatrixInt(matrixAtual)
                print 'key', newKey
                #print 'Visitando...'
                #neighbors = self.possiblesPositionsOnMatrix(matrixAtual)
                #for i in range(len(neighbors)):
                #    q.push(neighbors[i])
                if self._hash.get(newKey,0) == 0:
                    self._hash[newKey] = True
                    print 'Visitando...'
                    neighbors = self.possiblesPositionsOnMatrix(matrixAtual)
                    for i in range(len(neighbors)):
                        q.push(neighbors[i])
                else:
                    print 'Já visitado!'


    # Algoritm depth-first search
    def DFS(self, matrix,depth):
        self._numberOfInteractions = 0
        self._biggestSize = 1
        q = Queue()
        q.enqueue(matrix)
        while not q.isEmpty():

            matrixAtual = q.dequeue()
            size = q.size()
            self._numberOfInteractions+=1

            if self._biggestSize < size:
                self._biggestSize = size

            if self.isFinalPosition(matrixAtual):
                #print '\nResult!'
                #print 'number Of Interactions'
                #print self._numberOfInteractions
                #print 'Biggest Size'
                #print self._biggestSize
                return  matrixAtual
            else:
                neighbors = self.possiblesPositionsOnMatrix(matrixAtual)
                for i in range(len(neighbors)):
                    q.enqueue(neighbors[i])
                depth-=1
                if depth == 0:
                    #print '\nSo depth'
                    #print 'number Of Interactions'
                    #print self._numberOfInteractions
                    #print 'Biggest Size'
                    #print self._biggestSize
                    return []
        #print '\nEnd executation'
        #print 'number Of Interactions'
        #print self._numberOfInteractions
        #print 'Biggest Size'
        return []

    # Algoritm Iterative deepening depth-first search
    def IDS(self,matrix):
        i = 1
        s = self.DFS(matrix,i)
        while s == []:
            i+=1
            s = self.DFS(matrix,i)

        print 'Result found!'
        print 'depth'
        print i
        print 'Result:'
        return s
