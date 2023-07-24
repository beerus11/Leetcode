class DSU(object):
    def __init__(self):
        self.par = list(range(1001))
    
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        xr,yr = self.find(x),self.find(y)
        if xr == yr:
            return False
        self.par[self.find(x)] = self.find(y)
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
        