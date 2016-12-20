'''
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''

from collections import defaultdict 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = defaultdict(str)
        for i in range(len(s)):
            if s[i] in mapping and t[i] != mapping[s[i]]:
                return False
            else:
                mapping[s[i]] = t[i]
        if len(mapping.values()) != len(set(mapping.values())):
            return False
        return True 

c = Solution()
print c.isIsomorphic("paper", "titlt")

