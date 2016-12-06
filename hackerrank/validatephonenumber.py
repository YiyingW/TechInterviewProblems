'''
https://www.hackerrank.com/challenges/validating-the-phone-number

valid mobile number is a ten digit number starting with a 7, 8 or 9

'''

import re

N = int(raw_input())
for i in range(0, N):
	number = raw_input()
	if len(number) != 10:
		print 'NO'
	else:
		pattern = '(7|8|9)[0-9]{9}'
		match = re.search(pattern, number)
		if match:
			print 'YES'
		else:
			print 'NO'
