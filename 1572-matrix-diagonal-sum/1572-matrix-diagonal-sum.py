class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        l = len(mat)
        for i in range(len(mat)):
            s+=mat[i][i]
            s+=mat[i][l-i-1]
            if i == l-i-1:
                s-=mat[i][i]
            #print(i,l-i-1)
        return s