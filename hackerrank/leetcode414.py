class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        cmax = max(nums)
        cmin = min(nums)
        for n in nums:
            if n < cmax and n > cmin:
                cmid = n
                break

        for n in nums:
            if n < cmax and n > cmid:
                cmin = cmid
                cmid = n
            if n < cmid and n > cmin:
                cmin = n 
        return cmin


c = Solution()
print c.thirdMax([2, 2, 3, 1])