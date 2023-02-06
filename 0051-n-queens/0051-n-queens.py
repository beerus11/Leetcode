class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board,r,c):
            for i in range(len(board)):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
        ans = []
        def solve(board,i):
            if i ==len(board):
                ans.append(["".join(b) for b in board])
                return
            for j in range(n):
                if isSafe(board,i,j):
                    board[i][j]='Q'
                    solve(board,i+1)
                    board[i][j]='.'
                     
        board = [['.']*n for i in range(n)]
        solve(board,0)
        
        return ans
        