class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = (2**31)-1
        
        flag = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            flag = -1
        
        a = abs(dividend) 
        b = abs(divisor)
        
        mul = 1
        res = 0
        while a > 0:
            if a >= b:
                a = a - b
                res += mul
                b = b << 1
                mul = mul << 1
            else:
                b = b >> 1
                mul = mul >> 1

        if flag == 1:
            return min(MAX_INT, res)
        else:
            return max(-1*(MAX_INT+1), -1*res)
            
