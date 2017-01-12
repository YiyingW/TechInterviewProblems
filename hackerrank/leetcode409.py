import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        print count 

        length = 0
        odds = False

        for k, v in count.items():
            if v%2 == 0:
                length += v
            else:
                length += v-1
                odds = True
        return length + odds

c = Solution()
print c.longestPalindrome('abccAbB')