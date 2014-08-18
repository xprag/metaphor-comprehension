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
		self._key_separator = '_'
		# list of the lines read from the file_input except the first-one (header)
		self._lines = self._get_rows(file_input)
		# It contains the experiment arguments divided for class
		# Each class matches the key of the dictionary
		# The keys store the lists of experiment arguments
		self._dict_arguments = {}
		# It contains the key values of self._dict_arguments with duplicated values for each argument
		# If the experiment is divided in two parts then the keys will be half
		self._key_dict = []
		self._set_dict()
		# for key in sorted(self._dict_arguments.keys()):
		# 	print key , ', ' , len(self._dict_arguments[key])
		# print self._key_dict.count('T_P_TPPC'), self._key_dict.count('P')
		self._key_dict = self._remove_half_values(self._key_dict)
		# print self._key_dict.count('T_P_TPPC'), self._key_dict.count('P')
		# print self._key_dict
		# print self._dict_arguments.keys()
		self._write_file_output()

	# It read the line from the input_file and return a list containing these values shuffles except the first-one (header)
	def _get_rows(self, filename):
		# TODO implement pathname manipulations "os.path"
		with self._open_file(filename) as f:
			rows = f.readlines()
		# It contains the list of the column names read from the file_input and which will be written in the file_output
		self._arguments_header = rows.pop(0)
		random.shuffle(rows)
		return rows

	def _get_rows_shuffle(self):
		for i in range(len(self._lines)):
			columns = self._lines[i].split(',')
			print columns

	def _set_dict(self):
		for i in range(len(self._lines)):
			columns = self._lines[i].split(',')
			if columns[0] == 'T':
				key = columns[0] + self._key_separator + columns[1] + self._key_separator + columns[3]
			elif columns[0] == 'P':
				key = columns[0]
			if key in self._dict_arguments:
				self._dict_arguments[key] = self._dict_arguments[key] + [columns]
			else:
				self._dict_arguments[key] = [columns]
			self._set_key_list(key, columns[0])

	def _open_file(self, file_name):
		return codecs.open(file_input, encoding='latin-1')

	def _set_key_list(self, key, column):
			if column == 'T':
				self._key_dict = self._key_dict + [key]
			elif column == 'P':
				self._key_dict = self._key_dict + [column]

    # It removes half parts of duplicated elements from a list
    # example:
    # *input* my_array = [‘a’, ‘a’, ‘a’, ‘a’, ‘a’, ‘a’, ‘b’, ‘b’, ‘b’, ‘b’, ‘b’, ‘b’]
    # *output* my_array = [‘a’, ‘a’, ‘a’, ‘b’, ‘b’, ‘b’]
	def _remove_half_values(self, list_):
		unique_values = set(list_)
		for value in unique_values:
		    half_count =  list_.count(value) / 2
		    while half_count > 0:
		        half_count = half_count - 1
		        list_.remove(value)
		return list_

	# It loops reads the arguments from _dict_arguments by means of _key_dict
	# The read arguments are removed
	def _write_file_output(self):
		print self._arguments_header
		# It loops just the arguments which class is 'P'
		while self._key_dict.count('P') > 0:
			print self._dict_arguments['P'].pop()[3]
			self._key_dict.remove('P')
		# It loops the arguments which class begins with 'T'
		while len(self._key_dict) > 0:
			key = self._key_dict.pop()
			print self._dict_arguments[key].pop()[3]

file_input = '../stimuli/arguments.csv'
file_output = '/tmp/arguments.csv'
shuffleRows = ShuffleRows(file_input, file_output)
