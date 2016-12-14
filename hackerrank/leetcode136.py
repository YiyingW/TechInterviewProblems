'''
https://leetcode.com/problems/single-number/
'''
from collections import defaultdict
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k, v in d.items():
            if v == 1:
                return k

class Solution:
    """
   @param A : an integer array
   @return : a integer
   """
    def singleNumber(self, A):
        # write your code here
        ans = 0;
        for x in A:
            ans = ans ^ x
        return ans