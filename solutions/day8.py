from util.read_input import read_input
import numpy as np

DAY = __file__[-4]
inputs = read_input(DAY)

acc = 0
line = 0




def execute(inputs):
	evaluated = set()

	acc_val = 0
	line = 0

	def acc(value, line, acc_val):
		return line + 1, acc_val + value
	def jmp(value, line, acc_val):
		return line + value, acc_val
	def nop(value, line, acc_val):
		return line + 1, acc_val

	while True:
		instruction = inputs[line]
		command, value = instruction.split(' ')
		sign, value = (value[0], int(value[1:]))
		if sign == '-':
			value *= -1
		next_line, acc_val = eval(command + f'({value}, {line}, {acc_val})')
		evaluated.add(line)
		if next_line in evaluated:
			print(acc_val)
			return
		line = next_line

test_inputs = [
	'nop +0',
	'acc +1',
	'jmp +4',
	'acc +3',
	'jmp -3',
	'acc -99',
	'acc +1',
	'jmp -4',
	'acc +6',
]

def fix_cycle(inputs):
	END = len(inputs)

	def acc(value, line, acc_val):
		return line + 1, acc_val + value
	def jmp(value, line, acc_val):
		return line + value, acc_val
	def nop(value, line, acc_val):
		return line + 1, acc_val

	# queue up possible changes in threads
	# formatted (line, acc_val)
	# always check for repeats to save work
	acc_val = 0
	line = 0
	evaluated = set()
	edits = []
	edited = False
	while True:
		instruction = inputs[line]
		command, value = instruction.split(' ')
		sign, value = (value[0], int(value[1:]))
		if sign == '-':
			value *= -1
		if not edited:
			if command == 'jmp':
				edits.append(nop(value, line, acc_val))
			elif command == 'nop':
				edits.append(jmp(value, line, acc_val))

		next_line, acc_val = eval(command + f'({value}, {line}, {acc_val})')
		evaluated.add(line)

		if next_line == END:
			print(acc_val)
			return

		#not the right answer
		if next_line in evaluated:
			edited = True
			next_line, acc_val = edits.pop()
			while next_line in evaluated:
				next_line, acc_val = edits.pop()
		line = next_line

execute(inputs)
fix_cycle(inputs)