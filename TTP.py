'''
Coding up for binary tree traversal practice quiz. Traverse the tree in four different orders.

		A
      /   \
	B		C
   /   \
D 		E
          \
			F
BFS: A, B, C, D, E, F
In-order: D, B, E, F, A, C
Pre-order: A, B, D, E, F, C
Post-order: D, F, E, B, C, A
'''




class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def postOrderTraversal(node, output):
	if node != None:
		postOrderTraversal(node.left, output)
		postOrderTraversal(node.right, output)
		output.append(node.value)
	return output

def preOrderTraversal(node, output):
	if node != None:
		output.append(node.value)
		preOrderTraversal(node.left, output)
		preOrderTraversal(node.right, output)
	return output

def inOrderTraversal(node, output):
	if node != None:
		inOrderTraversal(node.left, output)
		output.append(node.value)
		inOrderTraversal(node.right, output)		
	return output


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.left = B
A.right = C 
B.left = D 
B.right = E 
E.right = F 

output = []
output = postOrderTraversal(A, output)
print 'post-Order: ',
for item in output:
	print item,
print '\n'

output = []
output = preOrderTraversal(A, output)
print 'pre-Order: ',
for item in output:
	print item,
print '\n'

output = []
output = inOrderTraversal(A, output)
print 'in-Order: ',
for item in output:
	print item,
print '\n'





