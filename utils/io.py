#!/usr/local/bin/python
# coding: latin-1

# This script aims at generating a cvs file from the original "Materiale per testare" shared into the Dropbox

import codecs

file_name = 'distrattori.csv'
f = codecs.open(file_name, encoding='latin-1')
new_line = []
for line in f:
	line = ",".join(line.split(','))
	line = ",".join(line.split('|'))
	line = line.split(',')
	tmp_line = []
	for i in range(len(line)):
		if i == 1 or i == 2:
			tmp_line = tmp_line + ['distrattore']
		tmp_line = tmp_line + [line[i]]
	new_line.append(tmp_line)

new_line[0] = 'ArgumentBlock,TWType,ArgumentNumber,ArgumentType,CorrectAnswer,premise1,premise2,conclusion,TW\n'.split(',')


f2 = codecs.open('distractors.csv', mode='w', encoding='utf-8')

for line in new_line:
	f2.write(','.join(line))
