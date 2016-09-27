'''
https://www.hackerrank.com/challenges/maximize-it
'''

from itertools import product

def function(tup, M):
	result = 0
	for i in range(0, len(tup)):
		result += tup[i]**2

	return result%M

K, M = map(int, raw_input().split())

lists = []

for i in range(0, K):
	this = map(int, raw_input().split())
	lists.append(this[1:])

test_pool = product(*lists)

maxnow = 0
for test in test_pool:
	thisresult = function(test, M)
	if thisresult > maxnow:
		maxnow = thisresult

print maxnow