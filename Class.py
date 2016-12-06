'''
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
'''
import math

class ComplexNum(object):
	def __init__(self, a, b): # number is a + bi
		self.a = a
		self.b = b

	def __add__(self, num2):
		newa = self.a + num2.a
		newb = self.b + num2.b
		return ComplexNum(newa, newb)

	def __sub__(self, num2):
		newa = self.a - num2.a
		newb = self.b - num2.b
		return ComplexNum(newa, newb)

	def __mul__(self, num2):
		newa = self.a*num2.a - self.b*num2.b
		newb = self.a*num2.b + self.b*num2.a
		return ComplexNum(newa, newb)

	def div(self, num2):
		conjugate = ComplexNum(num2.a, -1*num2.b)
		numerator = self.__mul__(conjugate)
		denomenator = float(num2.a**2 + num2.b**2)
		return ComplexNum(numerator.a/denomenator, numerator.b/denomenator)

	def mod(self):
		m = math.sqrt(self.a**2+self.b**2)
		return ComplexNum(m, 0)

	def printthis(self):
		if self.b >= 0:
			print "{0:.2f}+{1:.2f}i".format(self.a, self.b)
		else:
			print "{0:.2f}{1:.2f}i".format(self.a, self.b)

inputs = []
for i in range(0, 2):
	inputs.append(map(float, raw_input().split()))

A = ComplexNum(*inputs[0])
B = ComplexNum(*inputs[1])

(A+B).printthis()
(A-B).printthis()
(A*B).printthis()
(A.div(B)).printthis()
(A.mod()).printthis()
(B.mod()).printthis()





