'''
https://www.hackerrank.com/challenges/camelcase
'''

import sys


s = raw_input().strip()

upper_count = sum(1 for c in s if c.isupper())

print upper_count + 1