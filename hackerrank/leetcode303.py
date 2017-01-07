class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums






    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == j:
            return self.nums[i]
        return self.nums[i] + self.sumRange(i+1, j)

        


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4,5]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)