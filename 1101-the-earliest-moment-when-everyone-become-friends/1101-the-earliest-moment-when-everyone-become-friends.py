class DSU:
    def __init__(self,n):
        self.par = list(range(n+1))
        
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
            
    def union(self,a,b):
        xr,yr = self.find(a),self.find(b)
        if xr==yr:
            return False
        self.par[xr] = yr
        return True
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key= lambda x:x[0])
        ds = DSU(n)
        count = n
        for t,a,b in logs:
            if ds.union(a,b):
                count -=1
            if count == 1:
                return t
        return -1
            
            
        