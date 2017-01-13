class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type str: str
        :rtype: bool
        """
        n = len(s)
        if n == 1: 
            return False
        d = 1
        while d  <= n/2:
            if n % d == 0:
                print d
                if d >= 1 and n/d*s[:d] == s:
                    return True
            d += 1
        return False