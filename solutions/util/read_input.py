import os
import numpy as np

def read_input(day, integers = False):
	DATA_PATH = os.getcwd() + f'/data/day{day}.advent'
	if not os.path.exists(DATA_PATH):
		os.system(f'sh data/download.sh {day}')
	with open(DATA_PATH) as file:
		inputs = file.readlines()
	for i, line in enumerate(inputs):
		if line[-1:] == '\n':
			inputs[i] = line[:-1]

	if integers:
		inputs = list(map(int, inputs))
	return inputs