'''
Coding up for tree traversal practice quiz. Traverse the tree in four different orders.

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
		self.children = None

class Tree:
	def __init__(self, root=None):
		self.root = root

