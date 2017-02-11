class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        res = []
        for i, x in enumerate(nums):
            for elem in self.permute(nums[:i]+nums[i+1:]):
                res.append([x]+elem)
        return res
