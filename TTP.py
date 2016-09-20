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
print output





