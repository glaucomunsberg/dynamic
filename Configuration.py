#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Configuration:

	_instance 		= None

	# Files
	size_puzzle 	= None
	size_shake		= None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):

		# Size Square
		self.size_puzzle	= 3
		self.size_shake		= 1000
		self.number_of_tiles = (self.size_puzzle*self.size_puzzle) - 1

	def printConfiguration(self):

		print "Puzzle Size			",self.size_puzzle
		print "Number of Tiles		",self.number_of_tiles
