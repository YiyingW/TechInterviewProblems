'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function
definition should look like question2(a), and return a string.
'''

'''
dynamic programming solution, O(N^2) time and O(1) space.
	expand around center, there are 2N-1 such centers	
'''

def question2(a):

	def expandAroundCenter(s, c1, c2):
		l = c1
		r = c2
		n = len(s)
		while ((l >= 0)  & (r <= n-1)):
			if (s[l] == s[r]):
				l-=1
				r+=1
			else:
				break
		print l+1, r-l-1
		return s[l+1:r]

	n = len(a)
	if (n==0): return ""
	longest = a[0]
	for i in range(0, n-1):
		p1 = expandAroundCenter(a, i, i)
		if (len(p1) > len(longest)):
			print i
			print 'p1:', p1
			longest = p1
		p2 = expandAroundCenter(a, i, i+1)
		if (len(p2) > len(longest)):
			print 'p2:', p2
			longest = p2
	return longest

a = 'nbvdfjkdkjfadf'

question2('abccbadef')




