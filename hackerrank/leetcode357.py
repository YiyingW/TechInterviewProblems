class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def cal_combination(n):
            result = 1
            while (n>=1):
                result *= n
                n -= 1
            return result
        
        def uniqueDigit(n): # output n digits cases only
            num = 0
            subresult = []
            def search(start, current, cnt):
                if cnt == n:
                    subresult.append(current)
                    return
                for i in range(start, 10):
                    search(i+1, current+str(i), cnt+1)  
            search(0, "", 0)
            print subresult
            
            for case in subresult:
                if '0' in case:
                    num += cal_combination(n) - cal_combination(n-1)
                else:
                    num += cal_combination(n)
            
            return num

        result = 0
        for i in range(0, n+1):
            result += uniqueDigit(i)
            print result
        return result

c = Solution()
print c.countNumbersWithUniqueDigits(4)        


