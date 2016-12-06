'''
problem url: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle

'''
import sys 
import math

class Point(object):
	def __init__(self, cord):
		self.x = cord[0]
		self.y = cord[1]
		self.z = cord[2]

def diff(B,A):
	diff_cord = [B.x-A.x, B.y-A.y, B.z-A.z]
	return Point(diff_cord)

'''
cross product: (a1, a2, a3)X(b1, b2, b3) = (a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)
'''
def cross(A, B):
	result = [A.y*B.z-A.z*B.y, A.z*B.x-A.x*B.z, A.x*B.y-A.y*B.x]
	return Point(result)

def dot(A, B):
	return sum([A.x*B.x, A.y*B.y, A.z*B.z])
def mag(A):
	return math.sqrt(A.x**2+A.y**2+A.z**2)

def cosine(X, Y):
	if (mag(X)!=0 and mag(Y)!=0):
		return float(dot(X,Y))/(mag(X)*mag(Y))
	else:
		return 100



inputs = []
for i in range(0, 4):
	inputs.append(map(float,sys.stdin.readline().strip("\n").split(" ")))

A = Point(inputs[0])
B = Point(inputs[1])
C = Point(inputs[2])
D = Point(inputs[3])

AB = diff(B, A)
BC = diff(C, B)
CD  = diff(D, C)

X = cross(AB, BC)
Y = cross(BC, CD)


cos_phi = cosine(X, Y)

if cos_phi == 100:
	degree = 90
else:
	degree = math.degrees(math.acos(cos_phi))

print "{0:.2f}".format(degree)



