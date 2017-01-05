class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1')+bin(m).count('1')) == num:
                    res.append('{0}:{1:0>2}'.format(h,m))
        return res 
c = Solution()
print c.readBinaryWatch(1)
