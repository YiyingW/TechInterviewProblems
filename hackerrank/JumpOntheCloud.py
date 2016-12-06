'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds
'''

import sys

n = int(raw_input())
c = map(int,raw_input().strip().split())

count = 0
i = 0 
while (i < n-1):
	i += (c[i+2] == 0) + 1
	count += 1
print count