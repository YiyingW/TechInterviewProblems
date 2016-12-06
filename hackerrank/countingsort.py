from collections import defaultdict

n = int(raw_input())
arr = []
for i in range(0, n):
	arr.append(int(raw_input().split()[0]))

#ar = map(int, raw_input().split())

def count(n, ar):
	d = defaultdict(int)

	for i in ar:
		d[i] += 1

	for i in range(0, max(ar)+1):
		for j in range(0, d[i]):
			print i, 

def cum_count(n, ar):
	d = defaultdict(int)

	for i in ar:
		d[i] += 1
	result = [d[0]]
	for i in range(1, 100):
		result.append(result[i-1] + d[i])
		
	for n in result:
		print n,

cum_count(n, arr)

