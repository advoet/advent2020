from util.read_input import read_input
import numpy as np

DAY = 2
passwords = read_input(DAY)

def part_one():
	valid = 0
	for pp in passwords:
		policy, char, password = pp.split(' ')
		min_, max_ = map(int, policy.split('-'))
		char = char[0]
		count = 0
		for c in password:
			if c == char:
				count += 1
		if min_ <= count <= max_:
			valid += 1
	print(valid)

def part_two():
	valid = 0
	for pp in passwords:
		policy, char, password = pp.split(' ')
		pos1, pos2 = map(int, policy.split('-'))
		pos1 -= 1
		pos2 -= 1
		char = char[0]
		if (password[pos1] == char or password[pos2] == char) and not (password[pos1] == char and password[pos2] == char):
			valid += 1

	print(valid)

def main():
	part_two()

if __name__ == '__main__':
	main()