#!/usr/local/bin/python
# coding: latin-1

"""
Shuffle the lines of the cvs file according to the experiment's constraints.

The idea of this piece of code is to create two main data structures:
1. A dictionary of arguments (trial, test, trial-distractors, test-distractors)
2. A list of keys which indicates the class of the arguments.

The first-one is created from the stimuli files "stimuli/arguments.csv" and "stimuli/distractors.csv"
The second-one is created taking into account the constraints
about the frequency of distractors into the trial and test data.

The arguments will be read according the keys inside the list of the second data structure.


"""

import codecs, random, re, sys

class ShuffleRows:
	# there are two main variables:
	# 1 self._key_dict that define the sequence
	# 2 self._dict_arguments that contains the argument which are shuffled

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
		# It contains the key values of self._dict_arguments with duplicated values for each argument for the right hand
		_key_dict_right = self._remove_half_values(self._key_dict)
		# It contains the key values of self._dict_arguments with duplicated values for each argument for the left hand
		_key_dict_left = [] + _key_dict_right
		self._write_file_output(_key_dict_right)
		self._write_file_output(_key_dict_left)

	# It read the line from the input_file and return a list containing these values shuffles except the first-one (header)
	def _get_rows(self, filenames):
		# TODO implement pathname manipulations "os.path"
		rows = []
		for filename in filenames:
			with self._open_file(filename) as f:
				lines = f.readlines()
				lines.pop(0) # the first rows are just the header and it will be removed
				rows = rows + lines
			# It contains the list of the column names read from the file_input and which will be written in the file_output
			# self._arguments_header = rows.pop(0)
		random.shuffle(rows)
		return rows

	# This method aims at dividing the arguments in four categories:
	# T (+ many subcategories), P, T-distracted , P-distracted
	def _set_dict(self):
		for i in range(len(self._lines)):
			columns = self._lines[i].split(',')
			key = '' # it is the key of dictionary and it can be: T, P, T-distracted, P-distracted
			# if columns[1] == 'distrattore':
			# 	continue

			# It sets the key which can cover four main categories (T-distracted, P-distracted, P, T-****)
			if columns[1] == 'distrattore':
				if columns[0] == 'T':
					key = 'T-distracted'
				elif columns[0] == 'P':
					key = 'P-distracted'
			elif columns[0] == 'T':
				key = columns[0] + self._key_separator + columns[1] + self._key_separator + columns[3]
				self._key_dict = self._key_dict + [key]
			elif columns[0] == 'P':
				key = columns[0]
				self._key_dict = self._key_dict + [key]

			# It fills the dictionary
			if key in self._dict_arguments:
				self._dict_arguments[key] = self._dict_arguments[key] + [columns]
			else:
				self._dict_arguments[key] = [columns]

	def _open_file(self, file_name):
		return codecs.open(file_name, encoding='latin-1')

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

	# TODO a better implementation should use just append and shuffle and not random
	# in this way you can optimize the number of distractors
	# when the number of tests is not divisible by the number of distractors
	def _get_key_dict_distracted(self, key_dict, key_src = 'P-distracted', random_num = 3, distractors_num = 2):
		# distractors_num = len(self._dict_arguments[key_src]) / 2
		i = 0
		while i < distractors_num:
			range_num = range(i * random_num, random_num + (random_num * i))
			key_dict.insert(random.choice(range_num), key_src)
			i = i + 1

		# key_dict_prova.insert(random.choice(range_num), l.pop(5))
		return key_dict

	def _write_lines(self, dictionary):
		# TODO write into a output file
		while len(dictionary) > 0:
			# print key_dict_distracted.pop()
			line = self._dict_arguments[dictionary.pop()].pop()
			print line[0], line[3], line[8]
		print '---------------------------'

	# It loops reads the arguments from _dict_arguments by means of _key_dict
	# The read arguments are removed
	def _write_file_output(self, key_dict):

		key_dict.sort()

		key_dict_trial = self._get_key_dict_distracted(
			key_dict[:4],
			key_src = 'P-distracted',
			random_num = 3,
			distractors_num = 2)

		key_dict_test_1 = self._get_key_dict_distracted(key_dict[4:20],
			'T-distracted',
			random_num = 3,
			distractors_num = 6)

		key_dict_test_2 = self._get_key_dict_distracted(key_dict[20:],
			'T-distracted',
			random_num = 2,
			distractors_num = 19)

		key_dict_test = key_dict_test_1 + key_dict_test_2

		self._write_lines(key_dict_trial)
		self._write_lines(key_dict_test)

file_input = ['../stimuli/arguments.csv', '../stimuli/distractors.csv']
file_output = '/tmp/arguments.csv'
shuffleRows = ShuffleRows(file_input, file_output)
