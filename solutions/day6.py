from util.read_input import read_input
import numpy as np
import os

DAY = __file__[-4]
inputs = read_input(DAY)

def process_input(inputs):
	groups = []
	group = []
	for line in inputs:
		if line == '':
			groups.append(group)
			group = []
		else:
			group.append(line)
	if group:
		groups.append(group)
	return groups

def part_one(groups):
	print(
		sum(
			len(set.union(
				*(set(person) for person in group))
			) for group in groups
		)
	)
def part_two(groups):
	print(
		sum(
			len(set.intersection(
				*(set(person) for person in group))
			) for group in groups
		)
	)
def main():
	groups = process_input(inputs)
	print('part one')
	part_one(groups)
	print('part two')
	part_two(groups)

if __name__ == '__main__':
	main()