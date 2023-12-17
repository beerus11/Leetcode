class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = []
        seen = set()
        ans = [[float('inf')]*len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    seen.add((i,j))
        while q:
            x,y,d = q.pop(0)
            ans[x][y]=d
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                a,b=x+i,y+j
                if a>=0 and b>=0 and a<len(mat) and b<len(mat[0]) and (a,b) not in seen:
                    q.append((a,b,d+1))
                    seen.add((a,b))
        return ans
