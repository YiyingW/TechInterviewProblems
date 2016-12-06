'''
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. 
NOTE: This is not necessarily a BST.
Thoughts:
1. the first common ancestor is the deepest node such that p and q are both descendants. How you might
	identify this node. 
	p is in the left subtree of this node and q is in the right subtree of this node. 
2. How would you figure out if p is a descendent of a node n?
	start from n, do a serach, if i can find p, then p is a descendent of node n. 
3. start with the root. Can you identify if root is the first common ancestor? If it is not, can
	you identify which side of root the first common ancestor is on?
	I can check the left child of root and right child of root seperately to see if I reach p and q
	both in left subtree or both in right subtree. If so, the root is not first common ancestor and
	the FCA is on whichever side I can find p and q. If I reach p and q on a different subtree of root,
	then root is the FCA. 

=> recursive approach:
	check if p and q are descendants of the left subtree and the right subtree. If they are descendants
	of different subtrees, then the current node is the first common ancestor. If they are descendants 
	of the same subtree, then that subtree holds the first common ancestor.
	* how to check if p is descendant of n? tree traversal. 

'''
class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def PreOrderTraversalSearch(node, target): # node is the node to start with, target is the value
	if node:
		if node.value == target:
			return True
		else:
			return (PreOrderTraversalSearch(node.left, target) or PreOrderTraversalSearch(node.right, target))
	return False


def FCA(node, p, q):  # node is the node n to start with, p, q are the values 
	leftsub = node.left
	rightsub = node.right
	if (PreOrderTraversalSearch(leftsub, p) and PreOrderTraversalSearch(rightsub, q)) or (PreOrderTraversalSearch(leftsub, q) and PreOrderTraversalSearch(rightsub, p)):
		return node.value
	elif PreOrderTraversalSearch(leftsub, p): # p and q both on the left subtree
		return FCA(leftsub, p, q)
	else:
		return FCA(rightsub, p, q)



A = Node(3)
B = Node(0)
C = Node(1)
D = Node(4)
E = Node(2)
A.left = B
B.left = C
B.right = E
A.right = D

print FCA(A, 1, 4)




