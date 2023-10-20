class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for i in range(n)]
        
        def is_safe(i,j):
            for r in range(i):
                if board[r][j]=="Q":
                    return False
            a,b=i,j
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            while a>=0 and b<n:
                if board[a][b]=="Q":
                    return False
                a-=1
                b+=1
            return True
        self.count = 0
        def solve(r):
            if r==n:
                self.count+=1
                return True
            for c in range(n):
                if is_safe(r,c):
                    board[r][c]='Q'
                    solve(r+1)
                    board[r][c]='.'
            return False
        solve(0)
        return self.count
                    
                
            
        