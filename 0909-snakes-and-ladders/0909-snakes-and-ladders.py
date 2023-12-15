class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        n = len(board)
        cells = [None] * (n**2+1)
        
        index = 1
        for row in range(n):
            if row%2==0:
                for column in range(n):
                    cells[index] = board[row][column]
                    index+=1
            else:
                for column in range(n-1,-1,-1):
                    cells[index] = board[row][column]
                    index+=1
        q = [(1,0)]
        s = set()
        while q:
            node,steps = q.pop(0)
            if cells[node]!=-1:
                node = cells[node]
            if node == n**2:
                return steps
            for i in range(node+1,node+7):
                if i not in s:
                    s.add(i)
                    q.append((i,steps+1))
        return -1
        
        