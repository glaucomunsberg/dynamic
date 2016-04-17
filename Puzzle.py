#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Configuration import Configuration
from Interface import Interface
from random import randint

class Puzzle:
    _config	        = None
    _matrix         = None
    _matrixFinal    = None
    _interface      = None

    def __init__(self):
        self._config    = Configuration()
        self._interface = Interface()
        print 'Configuration'

    def createMatrix(self):
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

    def printMatrix(self):
        self._interface.printMatrix(self._matrix)


    def getEmptyPosition(self):
        for i in range(self._config.size_puzzle):
            for j in range(self._config.size_puzzle):
                if self._matrix[i][j] == 0:
                    return [i,j]

    def nextMovimentPossibilities(self):
        positionAtual = self.getEmptyPosition()
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

    def shakeMatrix(self):
        for i in range(self._config.size_shake):
            self.changePositionOnMatrix()

    def changePositionOnMatrix(self):

        positionAtual = self.getEmptyPosition()
        positionPossibilities = self.nextMovimentPossibilities()

        choice = randint(0,len(positionPossibilities)-1)

        oldValue = self._matrix[positionAtual[0]][positionAtual[1]]
        self._matrix[positionAtual[0]][positionAtual[1]] = self._matrix[positionPossibilities[choice][0]][positionPossibilities[choice][1]]
        self._matrix[positionPossibilities[choice][0]][positionPossibilities[choice][1]] = oldValue

    def isFinalyPosition(self):
        return self._matrix == self._matrixFinal
