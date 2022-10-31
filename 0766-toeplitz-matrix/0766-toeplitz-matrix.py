class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if not (r==0 or c==0 or matrix[r-1][c-1]==val):
                    return False
        return True
        
        