from util.read_input import read_input
import numpy as np
import os

DAY = __file__[-4]
inputs = read_input(DAY)

ROWS = 128
COLS = 8

def part_one(inputs):
	# generator
	highest_ID = 0
	for ID in id_generator(inputs):
		if ID > highest_ID:
			highest_ID = ID
	print('Highest ID', highest_ID)

def _find_missing(ids):
	# deprecated
	low = min(ids)
	high = max(ids)
	total = ((high - low) + 1 ) * (low + high) / 2
	actual_total = sum(ids)
	return total - actual_total

def part_two():
	# big data style, probably better to load batches
	min_id = 8*ROWS + COLS
	max_id = 0
	running_total = 0
	with open(os.getcwd() + f'/data/day{DAY}.advent') as file:
		for seat in file:
			ID = _get_id(seat[:-1])
			running_total += ID
			if ID < min_id:
				min_id = ID
			if ID > max_id:
				max_id = ID
	# sum from low to high - running_total = missing ID
	print(((max_id - min_id) + 1 ) * (min_id + max_id) / 2 - running_total)

def _get_id(seat):
	lo, hi = 0, ROWS - 1
	for i in range(7):
		(lo, hi) = (lo, (hi + lo) // 2) if seat[i] == 'F' else ((hi + lo) // 2 + 1, hi)
	# assert lo == hi
	# row = lo
	left, right = 0, COLS - 1
	for i in range(7, 10):
		(left, right) = (left, (right + left) // 2) if seat[i] == 'L' else ((right + left) // 2 + 1, right)
	# assert right == left
	# col = left
	# ID = 8*row + col
	return 8*lo + left

def id_generator(inputs):
		for seat in inputs:
			lo, hi = 0, ROWS - 1
			for i in range(7):
				(lo, hi) = (lo, (hi + lo) // 2) if seat[i] == 'F' else ((hi + lo) // 2 + 1, hi)
			left, right = 0, COLS - 1
			for i in range(7, 10):
				(left, right) = (left, (right + left) // 2) if seat[i] == 'F' else ((right + left) // 2 + 1, right)
			yield 8*lo + left

def main():
	part_two(inputs)

if __name__ == '__main__':
	main()