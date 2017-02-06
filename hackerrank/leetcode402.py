class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        A = num
        if not A or len(A) < k:
            return ""
        n = len(A)
        count = 0
        while count < k:
            for i in range(n):
                if i < n-1 and A[i] > A[i+1] or i == n-1:
                    break # i+1 is the position that drops and i needs to be delete
            A = A[:i]+A[i+1:]
            count += 1
            n -= 1                
        res = A.lstrip('0')
        if res == '':
            return '0'
        else:
            return res
