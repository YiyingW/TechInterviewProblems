'''
Implement a BST 
You can assume that two nodes with the same value won't be inserted into the tree
'''

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start != None:
            traversal.append(start.value)
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)
        return traversal

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        traversal = self.preorder_print(self.root, traversal)
        return '-'.join(str(e) for e in traversal)

    def insert(self, new_val):
        current_node = self.root
        LorR = None
        while current_node != None:
        	previous_node = current_node
        	if new_val < current_node:        		
        		current_node = current_node.left
        		LorR = 'L'
        	elif new_val > current_node:
        		current_node = current_node.right
        		LorR = 'R'
        if LorR == 'L': previous_node.left = Node(new_val)		
        if LorR == 'R': previous_node.right = Node(new_val)


    def search(self, find_val):
    	return self.search_helper(self.root, find_val)




    def search_helper(self, start, find_val):
    	if start != None:
    		if start.value == find_val:
    			return True
    		elif find_val > start.value:
    			return self.search_helper(start.right, find_val)
    		else:
    			return self.search_helper(start.left, find_val)

        return False

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

