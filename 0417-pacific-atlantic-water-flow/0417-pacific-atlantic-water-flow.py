class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        if not height or not height[0]:
            return []
        at = set()
        po = set()
        
        def dfs(i,j,st):
            st.add((i,j))
            for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                x,y =a+i,b+j
                if x<0 or y<0 or x>=len(height) or y>=len(height[0]):
                    continue
                if (x,y) in st:
                    continue
                if height[x][y]<height[i][j]:
                    continue
                dfs(x,y,st)
        for i in range(len(height)):
            dfs(i,0,po)
            dfs(i,len(height[0])-1,at)
            
        for i in range(len(height[0])):
            dfs(0,i,po)
            dfs(len(height)-1,i,at)
        return list(at.intersection(po))
        
            
        