'''
https://www.hackerrank.com/challenges/missing-numbers
'''

from collections import Counter


# A = [203,204,205,206,207,208,203,204,205,206]
# B = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

diff = []
A_dict = Counter(A)
B_dict = Counter(B)
for n in B_dict.keys():
	if n not in A_dict.keys():
		diff.append(n)
	else:
		if B_dict[n] != A_dict[n]:
			diff.append(n)
result = sorted(set(diff))
for r in result:
	print r,


