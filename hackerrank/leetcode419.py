class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0:
            return 0
        m = len(board)
        n = len(board[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X' and (c == 0 or board[r][c-1]!='X') and (r == 0 or board[r-1][c]!='X'):
                    count += 1
        return count
