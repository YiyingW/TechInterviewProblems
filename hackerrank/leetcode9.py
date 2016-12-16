'''
https://leetcode.com/problems/palindrome-number/

Palindrome Number
'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        length = 1
        while x >= length:
            length *= 10
        length /= 10
        while x:
            if x % 10 != x / length:
                return False
            x = (x % length) / 10
            length /= 100 # this is important 
        return True

num = Solution()
print num.isPalindrome(10000021)

