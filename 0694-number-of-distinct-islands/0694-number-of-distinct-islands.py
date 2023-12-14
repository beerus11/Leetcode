class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        uis = set()
        def dfs(i,j,st,sc):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return
            if (i,j) in seen or not grid[i][j]:
                return
            seen.add((i,j))
            current_island.add((i-st,j-sc))
            dfs(i+1,j,st,sc)
            dfs(i-1,j,st,sc)
            dfs(i,j+1,st,sc)
            dfs(i,j-1,st,sc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_island = set()
                dfs(i,j,i,j,)
                if current_island:
                    uis.add(frozenset(current_island))
                    
        
        return len(uis)