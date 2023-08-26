from itertools import product
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(b,r,c):
            if r<0 or c<0 or r>=len(b) or c>=len(b[0]):
                return
            if b[r][c]!="O":
                return
            b[r][c]="E"
            for ro,co in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(b,r+ro,c+co)
        if not board or not board[0]:
            return
        borders = list(product(range(len(board)), [0, len(board[0])-1])) \
                + list(product([0, len(board)-1], range(len(board[0]))))
        
        for r,c in borders:
            dfs(board,r,c)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
                    
                    
                    
        