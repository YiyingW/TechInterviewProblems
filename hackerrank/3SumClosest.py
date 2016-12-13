'''
Given an array S of n integers, find three integers in S such that the sum is 
closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

'''

class Solution(object):
    def threeSumClosest(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numbers.sort()
        ans = None
        for i, num in enumerate(numbers):
            l, r = i + 1, len(numbers) - 1
            while (l < r):
                sum3 = numbers[i] + numbers[l] + numbers[r]
                if ans is None or abs(sum3 - target) < abs(ans - target):
                    ans = sum3
                # the current sum is larger than current best
                if sum3 <= target:  
                    l = l + 1
                else:
                    r = r - 1
        return ans


