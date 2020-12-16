from util.read_input import read_input
import numpy as np

DAY = 1
nums = read_input(DAY)

def two_sum(nums, target = 2020):
	# returns two elements from nums that sum to 2020
	for i, num1 in enumerate(nums):
		for num2 in nums[i+1:]:
			if num1 + num2 == 2020:
				return num1, num2
	return -1, -1

def main():
	a, b = two_sum(nums)
	print(a, b, f"product {a*b}")

if __name__ == "__main__":
	main()