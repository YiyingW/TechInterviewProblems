"""
Since sumRange could be called many times on the same argument, we could
cache the result!
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.result = []
        if self.nums != []:
            self.result.append(self.nums[0])
        for i in range(1, len(self.nums)):
            self.result.append(self.result[i-1] + self.nums[i])
        print self.result


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == j:
            return self.nums[i]
        if i == 0:
            return self.result[j]
        else:
            return self.result[j] - self.result[i-1]