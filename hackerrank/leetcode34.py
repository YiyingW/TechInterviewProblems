class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []: return [-1, -1]
        left = self.helper(nums, target)

        if left < len(nums) and nums[left] == target:
            right = self.helper(nums, target + 1) - 1
            return [left, right]

        else:
            return [-1, -1]


    def helper(self, nums, target): 
        # find the first location from left that is >= target
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l)/2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l 