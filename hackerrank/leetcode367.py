'''
https://leetcode.com/problems/valid-perfect-square/
valid perfect square
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        current = num
        while (current/2)**2 > num:
            current /= 2
        for i in range(current/2, current):
            if i**2 == num: return True
        return False

c = Solution()
print c.isPerfectSquare(49)