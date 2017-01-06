class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        initiate = {1:1, 2:2}
        for i in range(3, n+1):
            initiate[i] = initiate[i-1] + initiate[i-2]

        return initiate[n]