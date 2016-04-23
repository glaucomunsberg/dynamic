#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Puzzle import Puzzle
from Configuration import Configuration
import time

if __name__ == "__main__":

    puzzle = Puzzle()
    config = Configuration()

    print 'Matrix'
    puzzle.createMatrix()
    puzzle.printMatrix(puzzle.getMatrix())

    print 'Shake times'
    print config.size_shake

    print 'After shake'
    puzzle.shakeMatrix(puzzle.getMatrix())
    puzzle.printMatrix(puzzle.getMatrix())

    #print 'isFinalPosition'
    #print puzzle.isFinalPosition(puzzle.getMatrix())
    #print 'possible matrix'
    #print puzzle.possiblesPositionsOnMatrix(puzzle.getMatrix())
    #print 'matrix send do FSB'
    #puzzle.printMatrix(puzzle.getMatrix())

    print 'Algoritms'
    print ' 1 - Depth-first search'
    print ' 2 - Breadth-first search'
    print ' 3 - Iterative deepening depth-first search'

    try:
        mode=int(raw_input('Algoritm Number:'))
        if mode == 1:
            start = time.time()
            print puzzle.BFS(puzzle.getMatrix())
            end = time.time()
            elapsed = end - start
            print 'FSB running at',elapsed,'seconds'
        elif mode == 2:
            start = time.time()
            print puzzle.DFS(puzzle.getMatrix(),config.size_shake)
            end = time.time()
            elapsed = end - start
            print 'DFS running at',elapsed,'seconds'
        elif mode == 3:
            start = time.time()
            print puzzle.IDS(puzzle.getMatrix())
            end = time.time()
            elapsed = end - start
            print 'IDS running at',elapsed,'seconds'
        else:
            print 'Option',mode,'is not allowed'
    except ValueError:
        print "Not a number"
