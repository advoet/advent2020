from util.read_input import read_input
import numpy as np
import os
from collections import defaultdict

DAY = __file__[-4]
inputs = read_input(DAY)

def _make_graph(inputs):
	graph = defaultdict(list)
	for rule in inputs:
		big_bag, little_bag_s = rule.split(' contain ')
		big_bag = big_bag.split(' ')
		big_bag = big_bag[0] + big_bag[1]
		if little_bag_s == 'no other bags.':
			graph[big_bag] = []
		else:
			little_bags = little_bag_s.split(', ')
			for bag in little_bags:
				bag = bag.split(' ')
				count, bag = bag[0], bag[1] + bag[2]
				graph[big_bag].append(bag)
	return graph

def _make_graph_two(inputs):
	graph = defaultdict(dict)
	for rule in inputs:
		big_bag, little_bag_s = rule.split(' contain ')
		big_bag = big_bag.split(' ')
		big_bag = big_bag[0] + big_bag[1]
		if little_bag_s == 'no other bags.':
			graph[big_bag] = {}
		else:
			little_bags = little_bag_s.split(', ')
			for bag in little_bags:
				bag = bag.split(' ')
				count, bag = bag[0], bag[1] + bag[2]
				graph[big_bag].update({bag: int(count)})
	return graph

def _invert_graph(graph):
	inverted = defaultdict(list)
	for source in graph:
		for target in graph[source]:
			inverted[target].append(source)
	return inverted

def _count_subgraph(graph, root, seen = set()):
	# gets the size of 
	seen.add(root)
	if not graph[root]:
		return 1
	else:
		return 1 + sum((_count_subgraph(graph, child, seen) for child in graph[root] if child not in seen))

def _count_subgraph_two(graph, root):
	# gets the size of 
	if not graph[root]:
		return 1
	else:
		total = 0
		for (child, count) in graph[root].items():
			total += count*_count_subgraph_two(graph, child)
		return 1 + total
			

def part_one(inputs):
	'''
	We represent containment as a directed graph.
	There is an arrow from bag1 to bag2 if bag1 > bag2
	Probably faster to just compute rather than invert the whole graph, but this seemed straightforward
	'''
	graph = _make_graph(inputs)
	inverted = _invert_graph(graph)
	print(_count_subgraph(inverted, 'shinygold') - 1)



def part_two(inputs):
	graph = _make_graph_two(inputs)
	print(_count_subgraph_two(graph, 'shinygold') - 1)

def test():
	inputs = [
		'shiny gold bags contain 2 dark red bags.',
		'dark red bags contain 2 dark orange bags.',
		'dark orange bags contain 2 dark yellow bags.',
		'dark yellow bags contain 2 dark green bags.',
		'dark green bags contain 2 dark blue bags.',
		'dark blue bags contain 2 dark violet bags.',
		'dark violet bags contain no other bags.',
	]
	graph = _make_graph_two(inputs)
	print(_count_subgraph_two(graph, 'shinygold') - 1)

def main():
	part_two(inputs)

if __name__ == '__main__':
	main()





