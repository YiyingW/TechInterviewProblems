'''
https://www.hackerrank.com/challenges/re-sub-regex-substitution
'''

import re

N = int(raw_input())

output = []

for i in range(0, N):
	s = raw_input()
	r1 = re.sub( r'( \&{2} )', ' and ', s)
	r2 = re.sub( r'( \&{2} )', ' and ', r1)
	r3 = re.sub( r'( \|{2} )', ' or ', r2)
	r4 = re.sub( r'( \|{2} )', ' or ', r3)
	output.append(r4)

for i in output:
	print i


'''
# solution: 

import re

for line in range(int(raw_input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',raw_input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print string

'''