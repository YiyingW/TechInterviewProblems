class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def subCountNumbers(n):
            """
            :type n: int
            :rtype: int
            """
            if n == 0: return 1
            result = []
            def adddigit(output, num, n):
                if num == n:
                    result.append(output)
                else:
                    if len(output)>=1:
                        if output[0] != "0" and "0" not in output:
                            adddigit(output+"0", num+1, n)
                    if "1" not in output:
                        adddigit(output+"1", num+1, n)                    
                    if "2" not in output:
                        adddigit(output+"2", num+1, n)
                    if "3" not in output:
                        adddigit(output+"3", num+1, n)
                    if "4" not in output:
                        adddigit(output+"4", num+1, n)
                    if "5" not in output:
                        adddigit(output+"5", num+1, n)
                    if "6" not in output:
                        adddigit(output+"6", num+1, n)
                    if "7" not in output:
                        adddigit(output+"7", num+1, n)  
                    if "8" not in output:
                        adddigit(output+"8", num+1, n)
                    if "9" not in output:
                        adddigit(output+"9", num+1, n) 


            adddigit("", 0, n)
            return len(result)

        
        if n == 0: return subCountNumbers(n)
        else:
            final_result = subCountNumbers(n)
            while (n>=1):
                final_result += subCountNumbers(n-1)
                n -= 1
        return final_result


c = Solution()
print c.countNumbersWithUniqueDigits(8)        


