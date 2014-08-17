#!/usr/local/bin/python
# coding: latin-1

"""
Shuffle the lines of the cvs file according to the experiment
"""

import re
import codecs
import random

class ShuffleRows:
	# class variable shared by all instances

	def __init__(self, file_input, file_output):
		self.key_separator = '_'
		self.rows = self.__get_rows(file_input)
		self.dict = {}
		self.__shuffle_rows()
		self.__set_dict()
		for key in sorted(self.dict.keys()):
			print key , ', ' , len(self.dict[key])

	def __get_rows(self, filename):
		with self.__open_file(filename) as f:
			rows = f.readlines()
		rows.pop(0)
		return rows

	def __get_rows_shuffle(self):
		for i in range(len(self.rows)):
			columns = self.rows[i].split(',')
			print columns

	def __set_dict(self):
		for i in range(len(self.rows)):
			columns = self.rows[i].split(',')
			key = columns[0] + self.key_separator + columns[1] + self.key_separator + columns[3]
			if key in self.dict:
				self.dict[key] = self.dict[key] + [columns]
			else:
				self.dict[key] = [columns]

	def __open_file(self, file_name):
		return codecs.open(file_input, encoding='latin-1')

	def __shuffle_rows(self):
		random.shuffle(self.rows)

file_input = '../stimuli/arguments.csv'
file_output = '/tmp/arguments.csv'
shuffleRows = ShuffleRows(file_input, file_output)
