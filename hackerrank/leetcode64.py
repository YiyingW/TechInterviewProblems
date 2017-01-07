class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ncol = len(grid[0])
        nrow = len(grid)

        result = {}
        result[(0,0)] = grid[0][0]
        for i in range(1, nrow):
            result[(i, 0)] = grid[i][0] + result[(i-1, 0)]

        for j in range(1, ncol):
            result[(0,j)] = grid[0][j] + result[(0, j-1)]



        for i in range(1, nrow):
            for j in range(1, ncol):
                result[(i, j)] = min(result[(i-1, j)]+grid[i][j], result[(i, j-1)]+grid[i][j])
        return result[(nrow-1, ncol-1)]


c = Solution()
grid = [[2,3,1],[4,6,2],[1,2,3]]
print c. minPathSum(grid)