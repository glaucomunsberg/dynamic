#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Configuration:

	_instance 		= None

	# Files
	size_puzzle 	= None
	size_shake		= None

	#Test
	times_tests		= None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		self.size_puzzle	= 3
		self.size_shake		= 10
		self.size_jungle	= 7
		self.number_of_tiles = (self.size_puzzle*self.size_puzzle) - 1

		self.times_tests = 2

	# Method used to print the configuration
	#	used on configuration
	def printConfiguration(self):
		print "Property				| Value"
		print " Puzzle Size			  ",self.size_puzzle
		print " Number of Tiles		  ",self.number_of_tiles
		print " Number of Shakes	  ",self.size_shake
		print " Number of Tests       ",self.times_tests
