'''
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is 
the farthest node from the root that is an ancestor of both nodes. For example, the root is a common 
ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, 
and the tree itself adheres to all BST properties. The function definition should look like 
question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is 
equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer 
representing the root, and n1 and n2 are non-negative integers representing the two nodes in no 
particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''
import numpy as np 

def Question4(T, r, n1, n2):

	class Node():
		def __init__(self, value):
			self.value = value
			self.left = None
			self.right = None


	# helper methods ******
	def MatrixToNodes(T):
		# converts a matrix represented tree into node-based-tree
		# input: Matrix 
		# output: root node
		newT = [Node(i) for i in range(0, len(T))]
		for i in range(0, len(T)):
			newT[i] = Node(i)
			sub = []
			for j in range(0, len(T[0])):
				if T[i][j] == 1:
					sub.append(j)
			if len(sub) == 1:
				newT[i].left = newT[sub[0]]
			if len(sub) == 2:
				newT[i].left = newT[sub[0]]
				newT[i].right = newT[sub[1]]	
		# which node is the root? The columns in the matrix that are all 0 are root candidates

		return newT

	def PreOrderTraversalSearch(node, target): # node is the node to start with, target is the value
		if node:
			if node.value == target:
				return True
			else:
				return (PreOrderTraversalSearch(node.left, target) or PreOrderTraversalSearch(node.right, target))
		return False


	def FCA(node, p, q):  # node is the node n to start with, p, q are the values 
		
		if node:
			if (node.value == p) or (node.value == q):
				return node.value

			if (node.left != None) & (node.right != None): # when node has both left subtree and right subtree
				leftsub = node.left
				rightsub = node.right
				if (PreOrderTraversalSearch(leftsub, p) and PreOrderTraversalSearch(rightsub, q)) or (PreOrderTraversalSearch(leftsub, q) and PreOrderTraversalSearch(rightsub, p)):
					return node.value
				elif PreOrderTraversalSearch(leftsub, p): # p and q both on the left subtree
					return FCA(leftsub, p, q)
				else:
					return FCA(rightsub, p, q)
			elif node.left == None:
				rightsub = node.right
				return FCA(rightsub, p, q)
			elif node.right == None:
				leftsub = node.left
				return FCA(leftsub, p, q)


	newT = MatrixToNodes(T)
	root = newT[r]



	return FCA(root, n1, n2)


T = [[0, 1, 0],
	 [0, 0, 1],
	 [0, 0, 0]
    ]

print Question4(T, 0, 1, 2)


