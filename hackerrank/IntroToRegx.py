'''
https://www.hackerrank.com/challenges/introduction-to-regex

re.search() : the first location where the regex pattern matches
re.match() : only matches at the beginning of the string

'''


import re 

# def float_check(s):

# 	p1 = '^(\+|-|)\d+(.)\d+'
# 	p2 = '^\d+(.)\d+'
# 	p3 = '^[+-]?\d*\.{1}\d$'

# 	a1 = re.search(p1, s)
# 	a2 = re.search(p2, s)
# 	a3 = re.search(p3, s)

# 	check1, check2, check3 = False, False, False


# 	if a1 == None:
# 		check1 = False
# 	elif len(a1.group(0)) == len(s):
# 		check1 = True
# 	else:
# 		cehck1 = False


# 	if a2 == None:
# 		check2 = False
# 	elif len(a2.group(0)) == len(s):
# 		check2 = True
# 	else:
# 		cehck2 = False

# 	if a3 == None:
# 		check3 = False
# 	elif len(a3.group(0)) == len(s):
# 		check3 = True
# 	else:
# 		cehck3 = False

# 	return check1|check2|check3

def float_check(s):
	p3 = '^[+-]?\d*\.{1}\d+$'
	a3 = re.search(p3, s)
	if a3 == None:
		check3 = False
	elif len(a3.group(0)) == len(s):
		check3 = True
	else:
		cehck3 = False
	return check3




N = int(raw_input())

inputs = []
for i in range(0, N):
	inputs.append(raw_input())

for s in inputs:
	print float_check(s)




