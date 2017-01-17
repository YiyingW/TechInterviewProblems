'''
[1,2,3,1] => 3 is the peak and return index 2
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)/2

            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                # larger than the left one                larger than the right one
                return mid 
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
            else:
                l = mid + 1
        return -1 


