class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m,n = len(board),len(board[0])
        def dfs(board, i, j):
            m, n = len(board), len(board[0])
            if i<0 or j<0 or i>=m or j>=n or board[i][j] != 'E':
                return

            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            adj_mines = 0

            for d in directions:
                di, dj = i + d[0], j + d[1]
                if 0 <= di < m and 0 <= dj < n and board[di][dj] == 'M':        
                    adj_mines += 1

            if adj_mines == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(adj_mines)
                return

            for d in directions:
                di, dj = i + d[0], j + d[1]
                dfs(board, di, dj)
                    
        if not board:
            return []
        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        dfs(board, i, j)
        return board
                
        