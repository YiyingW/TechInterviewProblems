class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="": return []
        result = []
        def adddigits(output, digits, i):
            if i == len(digits):
                result.append(output)
            else:
                if digits[i] == "2":
                    adddigits(output+"a", digits, i+1)
                    adddigits(output+"b", digits, i+1)
                    adddigits(output+"c", digits, i+1)
                if digits[i] == "3":
                    adddigits(output+"d", digits, i+1)
                    adddigits(output+"e", digits, i+1)
                    adddigits(output+"f", digits, i+1)
                if digits[i] == "4":
                    adddigits(output+"g", digits, i+1)
                    adddigits(output+"h", digits, i+1)
                    adddigits(output+"i", digits, i+1)
                if digits[i] == "5":
                    adddigits(output+"j", digits, i+1)
                    adddigits(output+"k", digits, i+1)
                    adddigits(output+"l", digits, i+1)
                if digits[i] == "6":
                    adddigits(output+"m", digits, i+1)
                    adddigits(output+"n", digits, i+1)
                    adddigits(output+"o", digits, i+1)
                if digits[i] == "7":
                    adddigits(output+"p", digits, i+1)
                    adddigits(output+"q", digits, i+1)
                    adddigits(output+"r", digits, i+1)
                    adddigits(output+"s", digits, i+1)
                if digits[i] == "8":
                    adddigits(output+"t", digits, i+1)
                    adddigits(output+"u", digits, i+1)
                    adddigits(output+"v", digits, i+1)
                if digits[i] == "9":
                    adddigits(output+"w", digits, i+1)
                    adddigits(output+"x", digits, i+1)
                    adddigits(output+"y", digits, i+1)
                    adddigits(output+"z", digits, i+1)
        adddigits("",digits, 0)
        return result

c = Solution()
print c.letterCombinations("23")