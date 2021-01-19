from util.read_input import read_input
import numpy as np
from math import sin, cos, radians

DAY = __file__[-5:-3]
inputs = read_input(DAY, integers = False)
test_inputs = [
	939,
	'1789,37,47,1889'
]
def part_one(inputs):
	earliest_time = int(inputs[0])
	bus_ids = [int(ID) for ID in inputs[1].split(',') if ID != 'x']

	best_ID = 0
	best_time = 999999999
	for ID in bus_ids:
		if (wait_time := ((earliest_time // ID) + 1) * ID - earliest_time) < best_time:
			best_ID = ID
			best_time = wait_time
	print(best_ID, best_time)
	print(best_ID * best_time)

def part_two(inputs):
	bus_ids = [
		(int(ID), offset) for offset, ID in enumerate(inputs[1].split(','))
		if ID != 'x'
	]
	
	'''
	goal:

	find TIME s.t.

	TIME % ID == offset for ID, OFFSET in bus_ids

	time = offset mod ID
	'''
	from math import gcd
	def lcm(a, b):
		return a * b // gcd(a, b)

	
	busses_used = [bus_ids[0][0]]
	time = 0
	step = busses_used[0]
	while True:
		for ID, offset in bus_ids:
			if (time + offset) % ID == 0 and ID not in busses_used:
				busses_used.append(ID)
				step = lcm(step, ID)
		if len(busses_used) == len(bus_ids):
			break
		else:
			time += step

	print(time)


part_two(test_inputs)