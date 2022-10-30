class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        self.count = 0
        def dfs(g,i,j):
            if i<0 or j<0 or i>len(g)-1 or j >len(g[0])-1:
                return
            if g[i][j]=="0":
                return
            g[i][j]="0"
            dfs(g,i+1,j)
            dfs(g,i,j+1)
            dfs(g,i-1,j)
            dfs(g,i,j-1)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]=="1":
                    dfs(g,i,j)
                    self.count+=1
        return self.count