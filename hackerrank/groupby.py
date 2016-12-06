'''
https://www.hackerrank.com/challenges/compress-the-string
'''

from itertools import groupby

s = '11243532215'

for key, group in groupby(s):
	print "({}, {})".format(len(list(group)), key), 
	