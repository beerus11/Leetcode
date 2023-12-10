class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix[0]),len(matrix)
        ans = [[None]*c for i in range(r)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i]=matrix[i][j]
        return ans
        