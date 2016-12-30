# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        if root.left == None and root.right == None:
            return root.val == sum_
        else:
            return self.hasPathSum(root.left, sum_ - root.val) || self.hasPathSum(root.right, sum_ - root.val)