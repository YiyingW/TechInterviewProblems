from abc import ABCMeta, abstractmethod

class Shape(object):

	__metaclass__=ABCMeta

	@abstractmethod
	def area(self): pass

	@abstractmethod
	def perimeter(self): pass

class Rectangle(Shape):

	def __init__(self, width, height):
		self.width = width
		self.height = height

		super(Rectangle, self).__init__()

	def area(self):
		return self.width*self.height

	def perimeter(self):
		return self.width*2 + self.height*2
class Square(Rectangle):

	def __init__(self, side_length):
		self.side_length = side_length
		super(Square, self).__init__(side_length, side_length)

	# override rectangle area method
	def area(self):
		print "Using Square area method"
		return self.width*self.height

s = Square(5)
print s.area()
print s.perimeter()



'''
object
	Shape
		Rectangle
			Square

'''

rect = Rectangle(5, 6)
print rect.area()
print rect.perimeter()




