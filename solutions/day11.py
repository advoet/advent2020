from util.read_input import read_input
import numpy as np

DAY = __file__[-5:-3]
inputs = read_input(DAY, integers = False)

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [
	(0, 1),
	(1, 1),
	(1, 0),
	(1, -1),
	(0, -1),
	(-1, -1),
	(-1, 0),
	(-1, 1),
]

test_input = [
	'L.LL.LL.LL',
	'LLLLLLL.LL',
	'L.L.L..L..',
	'LLLL.LL.LL',
	'L.LL.LL.LL',
	'L.LLLLL.LL',
	'..L.L.....',
	'LLLLLLLLLL',
	'L.LLLLLL.L',
	'L.LLLLL.LL',
]


def part_one_step(grid):
	changes = []
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == FLOOR:
				continue
			elif grid[row][col] == EMPTY:
				all_empty = True
				for i in range(max(0, row-1), min(len(grid), row+2)):
					for j in range(max(0, col-1), min(len(grid[0]), col+2)):
						if grid[i][j] == OCCUPIED:
							all_empty = False
				if all_empty:
					changes.append((row, col, OCCUPIED))
			elif grid[row][col] == OCCUPIED:
				occupied_adjacent = 0
				for i in range(max(0, row-1), min(len(grid), row+2)):
					for j in range(max(0, col-1), min(len(grid[0]), col+2)):
						if (i, j) == (row, col):
							continue
						if grid[i][j] == OCCUPIED:
							occupied_adjacent += 1
				if occupied_adjacent >= 4:
					changes.append((row, col, EMPTY))
	return changes



def part_two_step(grid):
	changes = []
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == FLOOR:
				continue
			elif grid[row][col] == EMPTY:
				if count_occupied(grid, row, col) == 0:
					changes.append((row, col, OCCUPIED))
			elif grid[row][col] == OCCUPIED:
				flag = True
				if count_occupied(grid, row, col, flag) >= 5:
					changes.append((row, col, EMPTY))
	return changes

def count_occupied(grid, row, col, flag = False):
	count = 0
	for direction in DIRECTIONS:
		if can_see_occupied(grid, row, col, direction, flag):
			count += 1
	return count

def can_see_occupied(grid, row, col, direction, flag = False):
	try:
		while True:
			row += direction[0]
			col += direction[1]
			if row < 0 or col < 0:
				return False
			if grid[row][col] == OCCUPIED:
				return True
			elif grid[row][col] == EMPTY:
				return False
	except IndexError:
		return False

def update(grid, changes):
	for row, col, val in changes:
		grid[row][col] = val

def part_one(inputs):
	grid = [list(row) for row in inputs]
	changes = part_one_step(grid)
	update(grid, changes)
	while changes:
		changes = part_one_step(grid)
		update(grid, changes)
	
	final_count = 0
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == OCCUPIED:
				final_count += 1

	print(final_count)

def part_two(inputs, show = False):
	grid = [list(row) for row in inputs]

	if show:
		for row in grid:
			print(''.join(row))
		print()
		print('---------------------------------------------------------------')
		print()
	changes = part_two_step(grid)
	update(grid, changes)

	if show:
		for row in grid:
			print(''.join(row))
		print()
		print('---------------------------------------------------------------')
		print()



	while changes:
		changes = part_two_step(grid)
		update(grid, changes)
		if show:
			for row in grid:
				print(''.join(row))
			print()
			print('---------------------------------------------------------------')
			print()
	final_count = 0
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == OCCUPIED:
				final_count += 1

	print(final_count)

def test_part_two():
	part_two(test_input, show = True)

def main():
	part_two(inputs)
if __name__ == '__main__':
	main()