#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Puzzle import Puzzle

if __name__ == "__main__":

    puzzle = Puzzle()

    print 'Matrix'
    puzzle.createMatrix()
    puzzle.printMatrix()
    print 'isFinalyPositon'
    print puzzle.isFinalyPosition()

    print 'After shake'
    puzzle.shakeMatrix()
    puzzle.printMatrix()
    print 'isFinalyPositon'
    print puzzle.isFinalyPosition()
