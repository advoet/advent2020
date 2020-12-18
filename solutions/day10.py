from util.read_input import read_input
import numpy as np
from bisect import insort

DAY = __file__[-5:-3]
inputs = read_input(DAY, integers = True)

def test():
	output_joltages = [
		16,
		10,
		15,
		5,
		1,
		11,
		7,
		19,
		6,
		12,
		4,
	]
	output_joltages.sort()
	my_adapter = max(output_joltages) + 3

	cur_joltage = 0
	ones = 0
	threes = 0
	for jolt in output_joltages:
		if jolt - cur_joltage == 1:
			ones += 1
		elif jolt - cur_joltage == 3:
			threes += 1
		cur_joltage = jolt
	print(ones*(threes+1))

def part_one(inputs):
	output_joltages = sorted(inputs)
	my_adapter = max(output_joltages) + 3
	cur_joltage = 0
	ones = 0
	threes = 0
	for jolt in output_joltages:
		if jolt - cur_joltage == 1:
			ones += 1
		elif jolt - cur_joltage == 3:
			threes += 1
		cur_joltage = jolt
	print(ones*(threes+1))

def part_two(inputs):
	output_joltages = sorted(inputs)
	my_adapter = max(output_joltages) + 3
	bottom = 0
	all_plugs = [bottom] + output_joltages + [my_adapter]

	valid_starting_at_index = [0]*len(all_plugs)
	# length 1
	valid_starting_at_index[-1] = 1
	# must include index element and last element
	valid_starting_at_index[-2] = 1
	# can skip
	valid_starting_at_index[-3] = valid_starting_at_index[-2] + (all_plugs[-3] + 3 >= all_plugs[-1])

	# start at the 4th to last element, traverse backwards through the list
	for i in range(len(all_plugs) - 4, -1, -1):
		valid_starting_at_index[i] = 0 \
			+ (all_plugs[i] + 3 >= all_plugs[i+1])*valid_starting_at_index[i+1] \
			+ (all_plugs[i] + 3 >= all_plugs[i+2])*valid_starting_at_index[i+2] \
			+ (all_plugs[i] + 3 >= all_plugs[i+3])*valid_starting_at_index[i+3]

	print(valid_starting_at_index[0])
	return

def main():
	part_two(inputs)
if __name__ == '__main__':
	main()