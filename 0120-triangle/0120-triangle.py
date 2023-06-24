class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def mnp(i,j):
            if i == len(triangle)-1 and j <=len( triangle[i])-1:
                return triangle[i][j]
            if i == len(triangle)-1 and j >len( triangle[i])-1:
                return float('inf')
            a = mnp(i+1,j)
            b = mnp(i+1,j+1)
            return triangle[i][j]+min(a,b)
        return mnp(0,0)
        
            
        