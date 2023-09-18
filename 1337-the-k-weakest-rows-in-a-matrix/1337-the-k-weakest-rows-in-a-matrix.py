class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            sc = 0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    sc+=1
            arr.append((sc,i))
        arr.sort()
        return [b for a,b in arr[:k]]
            
        