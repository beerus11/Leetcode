class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        
        def dfs(i,j,k=0):
            if k == len(word):
                return True
            if i > m-1 or j > n-1 or i <0 or j <0 :
                return False
            if board[i][j] == "#":
                return False
            if word[k]!=board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            if dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1):
                return True
            board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    return True
        return False
                
                
            