class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i <= j:
            
            if nums[j] == val:
                j -= 1
            else:
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    i += 1
        return i 
        
