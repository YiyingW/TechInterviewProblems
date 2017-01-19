'''
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r-l)/2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid 
        return r
        