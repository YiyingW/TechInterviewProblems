'''
https://www.hackerrank.com/challenges/validate-a-roman-number
'''

'''
In Roman numerals, there are seven characters that are repeated and combined in various
ways to represent numbers.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Rules for constructing Roman numerals:
	1. sometimes, characters are additive. I is 1, II is 2, III is 3. VI is 6. VII is 7.
	2. The tens characters (I, X, C, M) can be repeated up to three times. At 4, you need
		to subtract from the next highest fives character. 4 is not IIII but IV. 40 is XL,
		41 is XLI, 42 is XLII, 43 is XLIII, 44 is XLIV.
	3. sometimes, characters are the opposite of additive. 9 is IX. 90 is XC. 900 is CM. 
	4. the five characters can not be repeated. 
	5. Roman numerals are read left to right, so the order of characters matters very much.

1. Checking for thousands. 
	MMM, MM, M, or '' => '^M?M?M?$'
2. Checking for hundreds.
	100 = C
	200 = CC
	300 = CCC
	400 = CD
	500 = D
	600 = DC
	700 = DCC
	800 = DCCC
	900 = CM
	four possible patters:
		1. CM
		2. CD
		3. Zero to three C characters (0 if the hundres place is 0)
		4. D, followed by zero to three C characters
	the last two patterns can be combined: an optional D, followed by zero to three C chars
	=> '^M?M?M?(CM|CD|D?C?C?C?)$'

'''




import re

s = raw_input()

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

match = re.search(pattern, s)
if match:
	print 'True'
else:
	print 'False'

