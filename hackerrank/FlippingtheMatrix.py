'''
https://www.hackerrank.com/challenges/flipping-the-matrix
'''

'''
the freedom given makes it possible that at any given position in first quandrant,
the item can take one of the four possible values
(0, 0) - (0, n-1) - (n-1, 0) - (n-1, n-1)
(0, 1) - (0, n-2) - (n-1, 1) - (n-1, n-2)
(1, 0) - (1, n-1) - (n-2, 0) - (n-2, n-1)
(1, 1) - (1, n-2) - (n-2, 1) - (n-2, n-2)

(r, c) - (r, 2n-1-c) - (2n-1-r, c) - (2n-1-r, 2n-1-c)
'''

def findmax(M, n):
	result = 0
	for r in range(0, n):
		for c in range(0, n):
			result += max(M[r][c], M[r][2*n-1-c], M[2*n-1-r][c], M[2*n-1-r][2*n-1-c])
	return result

M = [[112, 42, 83, 119],
	 [56, 125, 56, 49],
	 [15, 78, 101, 43],
	 [62, 98, 114, 108]
]

q = int(raw_input())
for i in range(0, q):
	n = int(raw_input())
	M = []
	for i in range(0, 2*n):
		row = map(int, raw_input().split())
		M.append(row)
	print findmax(M, n)

