from itertools import permutations

inputs = raw_input().split()
s, k = inputs[0], int(inputs[1])

for c in sorted(list(permutations(s, k))):
	print ''.join(c)