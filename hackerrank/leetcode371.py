class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        for _ in xrange(32):
            a, b = a^b, (a&b)<<1
        if a & 0x80000000:
            return a 
        else:
            return a & 0xffffffff