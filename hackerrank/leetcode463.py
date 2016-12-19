'''
https://leetcode.com/problems/island-perimeter/

'''

class Solution(object):
    
    def perimeterOneWay(self, grid):

        perimeter = 0
        nrow = len(grid)
        ncol = len(grid[0])

        for i in range(nrow):
            for j in range(ncol):

                if j == 0 and grid[i][j] == 1: 
                    perimeter += 1 
                if j<ncol-1 and grid[i][j] != grid[i][j+1]:
                    perimeter += 1
                if j == ncol-1 and grid[i][j] == 1: 
                    perimeter += 1

        return perimeter




    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = self.perimeterOneWay(grid)+ self.perimeterOneWay(zip(*grid))
        print perimeter



s = Solution()
test = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

s.islandPerimeter(test)