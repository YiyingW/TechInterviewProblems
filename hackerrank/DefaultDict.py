'''
https://www.hackerrank.com/challenges/defaultdict-tutorial
'''

from collections import defaultdict

num_A, num_B = map(int, raw_input().split())

list_A = []
for i in range(0, num_A):
	list_A.append(raw_input())

list_B = []
for i in range(0, num_B):
	list_B.append(raw_input())

A = defaultdict(list)
for i in range(0, num_A):
	A[list_A[i]].append(i+1)

for i in range(0, num_B):
	if list_B[i] in A.keys():
		print ' '.join(map(str, A[list_B[i]]))
	else:
		print -1