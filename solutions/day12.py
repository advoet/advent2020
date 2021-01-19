from util.read_input import read_input
import numpy as np
from math import sin, cos, radians

DAY = __file__[-5:-3]
inputs = read_input(DAY, integers = False)

test_inputs = [
	'F10',
	'N3',
	'F7',
	'R90',
	'F11',
]

def part_one(inputs):
	facing = 0
	loc = [0, 0]
	for instruction in inputs:
		action, distance = instruction[0], int(instruction[1:])
		if action == 'F':
			loc[0] += distance*cos(radians(facing))
			loc[1] += distance*sin(radians(facing))
		elif action == 'N':
			loc[1] += distance
		elif action == 'S':
			loc[1] -= distance
		elif action == 'E':
			loc[0] += distance
		elif action == 'W':
			loc[0] -= distance
		elif action == 'L':
			facing += distance % 360
		elif action == 'R':
			facing -= distance % 360
	print(loc)
	print(sum(map(abs, loc)))

def part_two(inputs):
	loc = [0, 0]
	waypoint = [10, 1]
	for instruction in inputs:

		print(f'loc: {loc}')
		print(f'waypoint: {waypoint}')
		print(f'instruction: {instruction}')
		action, distance = instruction[0], int(instruction[1:])
		if action == 'F':
			loc[0] += distance * waypoint[0]
			loc[1] += distance * waypoint[1]
		elif action == 'N':
			waypoint[1] += distance
		elif action == 'S':
			waypoint[1] -= distance
		elif action == 'E':
			waypoint[0] += distance
		elif action == 'W':
			waypoint[0] -= distance
		elif action == 'L':
			waypoint[0], waypoint[1] = rotate(waypoint[0], waypoint[1], distance)
		elif action == 'R':
			waypoint[0], waypoint[1] = rotate(waypoint[0], waypoint[1], -distance)
	print(loc)
	print(sum(map(abs, loc)))

def rotate(x, y, deg):
	ang = radians(deg)
	return x*cos(ang) - y*sin(ang), x*sin(ang) + y*cos(ang)


def main():
	part_two(inputs)
if __name__=='__main__':
	main()