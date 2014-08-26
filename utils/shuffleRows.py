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
		self._file_output = file_output
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
		self._string2write = self._arguments_header # it contains just the header of stimuli files
		self._string2write = self._string2write + self._get_string2write(_key_dict_right)
		self._string2write = self._string2write + self._get_string2write(_key_dict_left)
		ouptup_file = codecs.open(self._file_output, mode='w', encoding='utf-8')
		ouptup_file.write(self._string2write )
		print 'The stimuli file is available at this location: ', self._file_output


	# It read the line from the input_file and return a list containing these values shuffles except the first-one (header)
	def _get_rows(self, filenames):
		# TODO implement pathname manipulations "os.path"
		rows = []
		for filename in filenames:
			with codecs.open(filename, encoding='utf-8') as f:
				lines = f.readlines()
				self._arguments_header = lines.pop(0) # the first rows are just the header and it will be removed
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

	# This method takes a list "key_list" and then for a specific number of items "items_num" 
	# it adds a specific number of other items "items2add_num"
	# which key is specified into "key2add_name" parameter
	# Example: each three items it should add randomly two items which value is 'test'
	# ex1: ['test', 'a', 'test', 'b', 'c', 'test', 'd', 'e', 'f', 'test',]
	# ex2: ['a', 'b', 'c', 'test', 'test', 'test', 'test', 'd', 'e', 'f']
	def _get_key_mixed(self, key_list = ['a', 'b', 'c', 'd', 'e', 'f'], items_num = 3, items2add_num = 2, key2add_name = 'test'):
		# distractors_num = len(self._dict_arguments[key_src]) / 2
		# print 'len(key_list): ', len(key_list)
		item_start = 0
		item_step = items_num
		item_end = item_step
		key_list_length = len(key_list)
		key_list_result = []

		while item_end < key_list_length + 1:
			key_list_tmp = key_list[item_start: item_end]
			i = 0
			while i < items2add_num:
				key_list_tmp.append(key2add_name)
				i = i + 1
			random.shuffle(key_list_tmp)
			key_list_result = key_list_result + key_list_tmp
			item_start = item_end
			item_end = item_end + item_step
		return key_list_result


	def _get_lines(self, dictionary):
		# TODO write into a output file
		buffer_output = ''
		while len(dictionary) > 0:
			line = self._dict_arguments[dictionary.pop()].pop()
			buffer_output = buffer_output + ','.join(line)
		return buffer_output

	# It loops reads the arguments from _dict_arguments by means of _key_dict
	# The read arguments are removed
	def _get_string2write(self, key_dict):

		string2write = ''
		key_dict.sort()

		key_list_trial = self._get_key_mixed(
			key_list = key_dict[:4], # it gets all the keys (four) which name is 'P' because the items has been sorted
			items_num = 2,
			items2add_num = 1,
			key2add_name = 'P-distracted'
			)
		string2write = string2write + self._get_lines(key_list_trial)

		# I need to distribute randomly 25 items 'T-distractors' inside a list of 36 items 'T-****'
		# I can divide the 36 items and the 25 items 'T-distractors' into two parts:
		# First part: 21 'T-****' vs 15 'T-distractors' -> 7/5; the probability density will be about 66%
		key_list_test1 = self._get_key_mixed(
			key_list = key_dict[4:25], # it gets the first 21 items which name is 'T-****' because the items has been sorted
			items_num = 7,
			items2add_num = 5,
			key2add_name = 'T-distracted'
			)
		# Second part: 15 'T-****' vs 10 'T-distractors' -> 3/2; the probability density will be about 71%
		key_list_test2 = self._get_key_mixed(
			key_list = key_dict[25:], # it gets the last 15 items which name is 'T-****' because the items has been sorted
			items_num = 3,
			items2add_num = 2,
			key2add_name = 'T-distracted'
			)
		key_list_test = key_list_test2 + key_list_test1
		string2write = string2write  + self._get_lines(key_list_test)

		return string2write

file_input = ['../stimuli/arguments.csv', '../stimuli/distractors.csv']
file_output = '/tmp/arguments.csv'
shuffleRows = ShuffleRows(file_input, file_output)
