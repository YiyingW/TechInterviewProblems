'''
https://www.hackerrank.com/challenges/sherlock-and-array
'''

import sys

T = int(raw_input().strip())

for test in range(0, T):
	n = int(raw_input())
	arr = map(int,raw_input().strip().split(' '))
	if (sum(arr) == 0) or (len(arr)==1): print 'YES'
	else:
		i = 0
		j = n-1
		s = 0
		while(i<j):
			if s <= 0:				
				s+=arr[i]
				i+=1

			else:
				s-=arr[j]
				j-=1

		if s == 0: print 'YES'
		else: print 'NO'
		




