'''
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

start from the top right corner, 
    if target is smaller than current, go left
    if target is larger than current, go down
O(m+n) time, O(1) space
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) # row
        if m == 0: return False
        n = len(matrix[0]) # column
        if n == 0: return False

        i, j = 0, n-1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


c = Solution()
print c.searchMatrix([[1,4,7,11,15],
                    [2,5,8,12,19],
                    [3,6,9,16,22],
                    [10,13,14,17,24],
                    [18,21,23,26,30]], 5)




