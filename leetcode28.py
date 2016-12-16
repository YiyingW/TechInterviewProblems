'''
https://leetcode.com/problems/implement-strstr/

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =="": return 0
        length = len(needle)
        for i in range(0, len(haystack)-length+1):
            sub = haystack[i:i+length]
            if sub == needle: return i
        return -1

test = Solution()
print test.strStr("aaa", "aa")



