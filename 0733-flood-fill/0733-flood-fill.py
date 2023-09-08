class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s = set()
        def dfs(i,j,c):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return
            if image[i][j]!=c or (i,j) in s:
                return
            s.add((i,j))
            image[i][j] = color
            dfs(i+1,j,c)
            dfs(i,j+1,c)
            dfs(i-1,j,c)
            dfs(i,j-1,c)
        dfs(sr,sc,image[sr][sc])
        return image
        