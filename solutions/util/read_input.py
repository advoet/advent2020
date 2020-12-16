import os
import numpy as np

def read_input(day):
	DATA_PATH = os.path.dirname(os.getcwd()) + f'/data/day{day}.advent'
	if not os.path.exists(DATA_PATH):
		os.chdir('..')
		os.system(f'sh download.sh {day}')
		os.chdir('solutions')
	inputs = np.genfromtxt(DATA_PATH)
	return inputs