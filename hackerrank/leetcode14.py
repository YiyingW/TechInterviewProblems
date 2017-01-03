"""
Longest common prefix
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        candidate = strs[0]
        current = 0
        for i in range(1, len(strs)):
            current = min(len(candidate), len(strs[i]))
            candidate = candidate[:current]
            for j in range(0, current):
                if candidate[j] != strs[i][j]:
                    current = j
                    candidate = candidate[:current]
                    break
        return candidate[:current]

c = Solution()
print c.longestCommonPrefix(["a"])