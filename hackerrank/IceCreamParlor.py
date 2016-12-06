'''
https://www.hackerrank.com/challenges/icecream-parlor
'''
from collections import defaultdict

def search(m, n, arr):
	d = defaultdict(list)
	for i in range(0, n):
		d[arr[i]].append(i+1)
	for f1 in d.keys():
		target = m - f1
		if target in d.keys():
			if f1 != target:
				return [d[f1][0], d[target][0]]
			else:
				if len(d[f1])>=2:
					return [d[f1][0], d[f1][1]]
				else:
					pass

T = int(raw_input())
for i in range(0, T):
	m = int(raw_input())
	n = int(raw_input())
	arr = map(int, raw_input().split())
	result = sorted(search(m,n,arr))
	print result[0], result[1] 
