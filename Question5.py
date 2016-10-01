'''
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if 
a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function
 definition should look like question5(ll, m), where ll is the first node of a linked list 
 and m is the "mth number from the end". You should copy/paste the Node class below to use 
 as a representation of a node in the linked list. Return the value of the node at that 
 position.
'''

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None 



def question5subRoutine(ll, m, counter):
	if ll == None:
		return 0
	counter += question5subRoutine(ll.next, m, counter) + 1
	if counter == m:
		print ll.data
	return counter




A = Node(2)
B = Node(3)
C = Node(8)
D = Node(1)
E = Node(6)

A.next = B 
B.next = C
C.next = D 
D.next = E

question5subRoutine(A, 3, 0)

