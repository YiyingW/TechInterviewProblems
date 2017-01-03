class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        result = [""]*numRows
        step = -1
        n = 0
        for i in range(0, len(s)):
            if n == 0 or n == numRows-1:
                step *= -1
            result[n] = result[n] + s[i]
            n += step
        return "".join(result)

c = Solution()
print c.convert("PAYPALISHIRING", 3)