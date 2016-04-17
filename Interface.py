#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  os
from Configuration import Configuration

class Interface:

    _config	    = None
    _topDecoration = None

    def __init__(self):
        self._config    = Configuration()
        self._topDecoration = "┌"
        self._buttonDecoration = "└"
        self._lineDecoration = "├"
        self._lineDataDecoration = "│"
        for i in range(self._config.size_puzzle-1):
            if self._config.size_puzzle > 3:
                self._topDecoration+="──────┬"
                self._buttonDecoration += "──────┴"
                self._lineDecoration += "──────┼"
            else:
                self._topDecoration+="─────┬"
                self._buttonDecoration += "─────┴"
                self._lineDecoration += "─────┼"
        if self._config.size_puzzle > 3:
            self._topDecoration+="──────┐"
            self._buttonDecoration += "──────┘"
            self._lineDecoration += "──────┤"
        else:
            self._topDecoration+="─────┐"
            self._buttonDecoration += "─────┘"
            self._lineDecoration += "─────┤"


    def printMatrix(self,puzzle):
        print self._topDecoration
        for i in range(len(puzzle)):
            if i != 0:
                print self._lineDecoration
            print self.lineToPrint(puzzle[i])
        print self._buttonDecoration

    def lineToPrint(self,listToInterate):
        self._lineDataDecoration = "│"
        for i in range(len(listToInterate)):
            if self._config.size_puzzle > 3:
                if listToInterate[i] > 9:
                    self._lineDataDecoration += "  "+str(listToInterate[i])+"  │"
                else:
                    self._lineDataDecoration += "   "+str(listToInterate[i])+"  │"
            else:
                self._lineDataDecoration += "  "+str(listToInterate[i])+"  │"
        return self._lineDataDecoration
