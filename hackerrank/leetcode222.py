# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0

        treeDepth = 0

        temp = root
        while temp:
            temp = temp.left
            treeDepth += 1

        n = 2**(treeDepth - 1)

        l, r = 0, n 

        while l < r:
            mid = l + (r - l)/2

            if self.nodeDepth(mid, n/2, root) == treeDepth:
                l = mid + 1
            else:
                r = mid 
        return l + n - 1

    def nodeDepth(self, index, half, root):

        depth = 0
        while root != None:
            if index < half:
                root = root.left
            else:
                root = root.right
                index = index - half
            depth += 1
            half /= 2
        return depth


