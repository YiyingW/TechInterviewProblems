'''
https://www.hackerrank.com/challenges/30-scope

private/protected variable
	have to have a setter and getter

'''

class Difference:
	def __init__(self, a):
		self._elements = a # private integer array for storing N non-negative integers

	def computeDifference(self):
		m = 0
		for i in range(0, len(self._elements)):
			for j in range(i, len(self._elements)):
				diff = self._elements[i] - self._elements[j]
				if diff < 0:
					diff = diff*(-1)
				if diff > m:
					m = diff
		self.maximumDifference = m
		return None



_ = raw_input()

a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference




