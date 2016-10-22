'''
Generate all the strings of length n drawn from an array with length k
'''

def LetterString(n, A):
	if n==1:
		return A 
	else:
		result_list = []
		for i in range(0, len(A)):
			result_list += [A[i]+s for s in LetterString(n-1, A)]
		return result_list

print LetterString(3, ['A', 'B', 'C', 'D', 'E'])