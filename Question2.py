'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function
definition should look like question2(a), and return a string.
'''

'''
dynamic programming solution, O(N^2) time and O(N^2) space.
	base case P[i,i] is true
			  P[i, i+1] is true is Si = Si+1
	first initialize the one and two letters palindromes, then all three letters, and so on
'''

def question2(a):
	n = len(a)
	longestBegin = 0
	maxLen = 1
	table = [[False for i in range(0, n)] for j in range(0, n)]
	# base case
	for i in range(0, n):
		table[i][i] = True 
	for i in range(0, n-1):
		if (a[i] == a[i+1]):
			table[i][i+1] = True
			longestBegin = i
			maxLen = 2
	for length in range(3, n+1):
		for i in range(0, n-length+1):
			j = i+length-1
			if (a[i] == a[j]) & (table[i+1][j-1]):
				table[i][j] = True
				longestBegin = i
				maxLen = length

	return a[longestBegin:longestBegin+maxLen]


