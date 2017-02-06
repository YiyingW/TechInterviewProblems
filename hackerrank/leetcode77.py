class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        sol = []
        allsol = []
        self.findComb(n, 1, k, sol, allsol)
        return allsol
        
    def findComb(self, n, start, k, sol, allsol):
        if k == 0:
            allsol.append([x for x in sol])
            return
        for i in range(start, n-k+2):
            sol.append(i)
            self.findComb(n, i+1, k-1, sol, allsol)
            sol.pop()
