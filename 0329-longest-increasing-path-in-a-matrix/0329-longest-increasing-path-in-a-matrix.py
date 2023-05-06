class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dp = {}
        rows = len(matrix)
        cols = len(matrix[0])
        def lip(x,y):
            if (x,y) in self.dp:
                return self.dp[(x,y)]
            l = 0
            for i, j in [(0,1),(0,-1),(1,0),(-1,0)]:
                newX, newY = x+i, y+j
                if newX >= 0 and newX < rows and newY >= 0 and newY < cols and matrix[newX][newY] > matrix[x][y]:
                    l = max(l, lip(newX, newY))
            self.dp[(x,y)] =  l+1
            return self.dp[(x,y)]
        
        ml = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ml = max(ml,lip(i,j))
        return ml
        