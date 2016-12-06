# generate all the strings of length n drawn from 0, ..., k-1
# use recursion and backtracking
# with replacement

def rangeToList(k):
	# takes a number k and create a list of strings with 0 - k-1
	return [str(i) for i in xrange(k)]

def baseKStrings(n, k):
	if n == 0: return []
	if n == 1: return rangeToList(k)
	return [''.join([digit, bitstring]) for digit in rangeToList(k)
					for bitstring in baseKStrings(n-1, k)]

print baseKStrings(4, 3)

# when writing recursion, just assmue you have already implemented the lower 
# order functions and bridge it to the higher order function. Plus, base cases. 