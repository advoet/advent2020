from util.read_input import read_input
import numpy as np

DAY = 3
grid = read_input(DAY)
OPEN = '.'
TREE = '#'
rule = {'right': 3, 'down': 1}

'''
# ADDED TO READ_INPUT
for row in range(len(grid)):
	grid[row] = grid[row][:-1]
'''

def count_collisions(grid, rule):
	row, col = 0, 0
	count = 0
	while row + rule['down'] < len(grid):
		row += rule['down']
		col += rule['right']
		col %= len(grid[0])
		if grid[row][col] == TREE:
			count += 1
	return count

def _make_rule(right, down):
	return {'right': right, 'down': down}

def main():
	total = 1
	for rule in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
		rule = _make_rule(*rule)
		print(rule, count_collisions(grid, rule))
		total *= count_collisions(grid, rule)
	print(f'Product: {total}')

if __name__ == '__main__':
	main()