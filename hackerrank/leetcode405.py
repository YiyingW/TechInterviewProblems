class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return '0'
        ans = ""
        for i in range(8):
            n = num & 15
            if n > 9 :
                n = chr(87 + n)
            else :
                n = str(n)
            ans = n + ans
            num = num >> 4
        return ans.lstrip('0')