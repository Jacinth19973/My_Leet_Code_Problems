class Solution:
    def totalNQueens(self, n: int) -> int:
        from typing import List
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def isSafe(row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False
            
            # Check upper-right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == "Q":
                    return False
            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."  

        backtrack(0)
        return len(res)
