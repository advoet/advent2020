from util.read_input import read_input
import numpy as np
from bisect import insort

DAY = __file__[-4]
inputs = read_input(DAY, integers = True)

WINDOW_LEN = 25

def is_sum_of_two(window, num):
	for i in range(len(window)):
		for j in range(i + 1, len(window)):
			if window[i] + window[j] == num:
				return True
	else:
		return False

def part_two(inputs):
	# lets not redo calculations
	target = part_one(inputs)

	start = 0
	end = 1
	window_sum = inputs[start] + inputs[end]
	while end < len(inputs):
		if window_sum < target:
			end += 1
			window_sum += inputs[end]
		elif window_sum > target:
			window_sum -= inputs[start]
			start += 1
			if start == end:
				end += 1
				window_sum += inputs[end]
		else:
			print('part two:', min(inputs[start:end+1]) + max(inputs[start:end+1]))
			return
	print('failure')
	return


def part_one(inputs):
	window = inputs[:WINDOW_LEN]
	index = WINDOW_LEN

	while is_sum_of_two(window, inputs[index]):
		window.pop(0)
		window.append(inputs[index])
		index += 1

	ans = inputs[index]
	print('part one:', ans)
	return ans

def test():
	WINDOW_LEN = 5
	inputs = [
		35,
		20,
		15,
		25,
		47,
		40,
		62,
		55,
		65,
		95,
		102,
		117,
		150,
		182,
		127,
		219,
		299,
		277,
		309,
		576,
	]
	test_ans = 127

	window = inputs[:WINDOW_LEN]
	index = WINDOW_LEN

	while is_sum_of_two(window, inputs[index]):
		window.pop(0)
		window.append(inputs[index])
		index += 1

	ans = inputs[index]
	assert ans == 127

def main():
	part_two(inputs)

if __name__ == '__main__':
	test()
	main()