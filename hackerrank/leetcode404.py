# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = [0]
        def Traversal(result, node):

            if (node != None):
       
                if node.left != None and node.left.left == None and node.left.right == None:
                    #print l
                    result = l[-1]
                    result += node.left.val
                    l.append(result)
                    Traversal(result, node.left)
                    Traversal(result, node.right)
                else:
                    result = l[-1]
                    Traversal(result, node.left)
                    result = l[-1]
                    Traversal(result, node.right)
        
        Traversal(0, root)
        return l[-1]