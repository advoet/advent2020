from util.read_input import read_input
import numpy as np

DAY = 1
nums = read_input(DAY, integers = True)

def two_sum(nums, target = 2020):
	# returns two elements from nums that sum to 2020
	for i, num1 in enumerate(nums):
		for num2 in nums[i+1:]:
			if num1 + num2 == 2020:
				return num1, num2
	return -1, -1

def two_sum_hash(nums, target = 2020):
	seen = set()
	for num in nums:
		if target - num in seen:
			return num, target - num
		else:
			seen.add(num)
	return False

def three_sum(nums, target = 2020):
	for i, num in enumerate(nums):
		if (ans:=two_sum_hash(nums[i:], target = target - num)):
			return num, *ans

def main():
	a, b = two_sum_hash(nums)
	print(a, b, f"product {a*b}")
	a, b, c = three_sum(nums)
	print(a, b, c, f'product {a*b*c}')

if __name__ == "__main__":
	main()