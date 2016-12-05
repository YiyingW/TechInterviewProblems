'''
decorators -- higher order functions
Functions are first-class objects. 
In python, we can pass functions to other functions as a parameter.

this problem is to use decorator to format the output of a function
'''

def mydecorator(msg="Message"):

	def decorated(f):

		def wrapper(*args, **kwargs):
			print("The message is "+msg)
			print("Inside of the decorator before calling the function.")
			f(*args, **kwargs)
			print("Inside of the decorator after calling the function.")

		return wrapper

	return decorated

@mydecorator(msg="Hello")
def printName(name):
	print(name)



printName("Yiying")
