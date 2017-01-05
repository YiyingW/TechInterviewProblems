class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def bracket(output, open_n, close_n, n):
            if (open_n ==  n & close_n == n):
                result.append(output)
            else:
            # number of close should never be larger than the open
                if open_n < n:
                    bracket(output+"(", open_n+1, close_n, n)
                if close_n < open_n:
                    bracket(output+")", open_n, close_n+1, n)
        bracket("", 0, 0, n)
        return result 


c = Solution()
print c.generateParenthesis(3)

