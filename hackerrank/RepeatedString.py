
'''
https://www.hackerrank.com/challenges/repeated-string
'''

import sys


s = raw_input().strip()
n = long(raw_input().strip())

length = len(s)
hm = n/length


hma = 0

for i in range(0, length):
	if s[i] == 'a':
		hma += 1

result = hm*hma


mod = n%length
for i in range(0, mod):
	if s[i] == 'a':
		result += 1

print result