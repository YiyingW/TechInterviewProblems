# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, 0, res)
        return res
        
    def helper(self, root, level, res):
        if root:
            if len(res) == level:
                res.append(root.val)
        
            level += 1
            self.helper(root.right, level, res)
            self.helper(root.left, level, res)
