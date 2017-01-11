class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        count = 0
        i,j = 0, 0
        while(i < len(g) and j < len(s)):
            if g[i] <= s[j]:
                count += 1
                i+=1
                j+=1
            else:
                j+=1
        return count

c = Solution()
print c.findContentChildren([10,9,8,7],[5,6,7,8])

