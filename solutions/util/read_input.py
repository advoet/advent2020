import os
import numpy as np

def read_input(day):
	DATA_PATH = os.getcwd() + f'/data/day{day}.advent'
	if not os.path.exists(DATA_PATH):
		os.system(f'sh data/download.sh {day}')
	with open(DATA_PATH) as file:
		inputs = file.readlines()
	return inputs