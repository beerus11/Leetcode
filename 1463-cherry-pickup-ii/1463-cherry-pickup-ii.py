class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(r,c1,c2):
            if c1<0 or c2<0 or c1>=len(grid[0]) or c2>=len(grid[0]):
                return float('-inf')
            res = grid[r][c1]
            if c1!=c2:
                res+=grid[r][c2]
            mx = 0
            if r !=len(grid)-1:
                for i in [c1-1,c1,c1+1]:
                    for j in [c2-1,c2,c2+1]:
                        mx = max(mx,dfs(r+1,i,j))
            return mx+res
        return dfs(0,0,len(grid[0])-1)
        
            
        