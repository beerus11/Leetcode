class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if grid2[i][j]==0:
                return
            if grid1[i][j]==0:
                self.si = False
            grid2[i][j] = 0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            
        self.si = True 
        ans = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                self.si = True
                if grid2[i][j]==1:
                    dfs(i,j)
                    if self.si == True:
                        ans+=1
        return ans
                        
                
        