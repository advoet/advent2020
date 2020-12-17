from util.read_input import read_input
import numpy as np

DAY = __file__[-4]
inputs = read_input(DAY)

def is_valid_one(passport):
	# passport is a set with the fields that exist
	if len(passport) == 8:
		return True
	elif len(passport) == 7 and not 'cid' in passport:
		return True
	return False


def part_one(inputs):
	passport = set()
	count = 0
	for line in inputs:
		if line == '':
			if is_valid_one(passport):
				count += 1
			passport = set()
		else:
			fields = line.split(' ')
			for field in fields:
				passport.add(field[:3])
	if is_valid_one(passport):
		count += 1
	print(count)

def is_valid_two(passport):
	# passport is a dict {field: value}
	# the only error condition is missing fields
	if (len(passport) == 8) or (len(passport) == 7 and not 'cid' in passport):
		conditions = (
			1920 <= int(passport['byr']) <= 2002,
			2010 <= int(passport['iyr']) <= 2020,
			2020 <= int(passport['eyr']) <= 2030,
			(passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or \
				(passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76),
			passport['hcl'][0] == '#' and \
				all((char.isdigit() or char in ('a','b','c','d','e','f') for char in passport['hcl'][1:])),
			passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
			len(passport['pid']) == 9 and all((char.isdigit() for char in passport['pid'])),
		)
		return all(conditions)
	return False

def part_two(inputs):
	passport = dict()
	count = 0
	for line in inputs:
		if line == '':
			if is_valid_two(passport):
				count += 1
			passport = dict()
		else:
			fields = line.split(' ')
			for field in fields:
				passport[field[:3]] = field[4:]
	if is_valid_two(passport):
		count += 1
	print(count)

def main():
	part_two(inputs)

if __name__ == '__main__':
	main()