class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d = {'0':0, '1':1,
            '2':2, '3':3, '4':4, '5':5,
            '6':6, '7':7,'8':8,'9':9}
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        z = []
        icarry = 0
        i = 0
        while (i < len(num2)) or (i>=len(num2) and icarry == 1):
            sum_ = 0
            if i < len(num2):
                sum_ = d[num1[i]] + d[num2[i]] + icarry
            elif i < len(num1):
                sum_ = d[num1[i]] + icarry
            else:
                sum_ = icarry
                icarry = 0

            if sum_ >= 10:
                icarry = 1
            if sum_ < 10:
                icarry = 0

            z.append(str(sum_%10))
            i += 1
        
        if i < len(num1): 
            for j in range(i, len(num1)):
                z.append(num1[j])
        
        return ''.join(z)[::-1]

c = Solution()
print c.addStrings('99', '9')

