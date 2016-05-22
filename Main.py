#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Puzzle import Puzzle
from Configuration import Configuration
from TicTacToe import TicTacToe
import time

if __name__ == "__main__":

    puzzle = Puzzle()
    config = Configuration()
    ticTacToe = TicTacToe()

    # Puzzle inicialization
    print 'Matrix'
    puzzle.createMatrix()
    puzzle.printMatrix(puzzle.getMatrix())

    print 'After shake'
    puzzle.shakeMatrix(puzzle.getMatrix())
    puzzle.printMatrix(puzzle.getMatrix())

    # Xs and Os inicialization
    print 'Tic-Tac-Toe'
    ticTacToe.createBoard()
    ticTacToe.printBoard()


    print 'Algoritms 8-Puzzle'
    print ' 1 - Breadth-first search'
    print ' 2 - Depth-first search'
    print ' 3 - Iterative deepening depth-first search'
    print ' 4 - A*'
    print 'Tic-Tac-Toe'
    print ' 5 - Play MinMax'

    try:
        mode=int(raw_input('Algoritm Number:'))
        if mode == 1:
            start = time.time()
            print puzzle.BFS(puzzle.getMatrix())
            end = time.time()
            elapsed = end - start
            print 'BFS running at',elapsed,'seconds'
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
        elif mode == 4:
            start = time.time()
            print puzzle.Astar(puzzle.getMatrix())
            end = time.time()
            elapsed = end - start
            print 'A*  running at',elapsed,'seconds'
        elif mode == 5:
            start = time.time()
            ticTacToe.playTicTacToe()
            end = time.time()
            elapsed = end - start
            print 'TicTacToe running at',elapsed,'seconds'
        else:
            print 'Option',mode,'is not allowed'
    except ValueError:
        print "Not a number"
