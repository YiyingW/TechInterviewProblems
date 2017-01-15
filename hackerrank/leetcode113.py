class Solution:
# @param {TreeNode} root
# @param {integer} sum
# @return {integer[][]}
    def pathSum(self, root, sum):
        ans = []
        self.dfs(root, sum, [],ans)
        return ans

    def dfs(self, root, sum, tmp, ans):
        if not root:
            return
    
        if root.left == None and root.right == None and sum == root.val:
            ans.append(tmp+[root.val])
            return
    
        self.dfs(root.left, sum-root.val, tmp+[root.val], ans)
        self.dfs(root.right, sum-root.val, tmp+[root.val], ans)