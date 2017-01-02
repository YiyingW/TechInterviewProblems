class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret 

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return self.DFS(candidates, target-candidates[i], i, valuelist+[candidates[i]])

c = Solution()
print c.combinationSum([2,3,6,7], 7)
