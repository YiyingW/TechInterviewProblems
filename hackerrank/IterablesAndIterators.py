'''
https://www.hackerrank.com/challenges/iterables-and-iterators
'''
'''
combination without replacement
'''

from itertools import combinations

N = int(raw_input())

letters = raw_input().split()
k = int(raw_input())

no_a_count = 0
result = list(combinations(letters, k))
for item in result:
	if 'a' not in item:
		no_a_count += 1
print "{:.4f}".format(1-1.0*no_a_count/len(result))