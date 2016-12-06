'''
https://www.hackerrank.com/challenges/30-more-exceptions?h_r=email&unlock_token=d5d302787cda6462ffe15d1be14476f357b0cb87&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
'''

class Calculator:

	def power(self,n, p):

		if n >= 0 and p >= 0:
			return n**p
		else:
			raise Exception('n and p should be non-negative')

myCalculator = Calculator()
T = int(raw_input())
for i in range(T):
	n, p = map(int, raw_input().split())

	try:
		ans = myCalculator.power(n, p)
		print ans
	except Exception, e:
		print e 
