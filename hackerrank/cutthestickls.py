'''
https://www.hackerrank.com/challenges/cut-the-sticks
'''

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while (len(arr)!=0):
	print len(arr)
	mi = min(arr)
	arr = map(lambda x:x-mi, arr)
	arr = filter(lambda x: x!=0, arr)

