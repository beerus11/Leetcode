class DSU:
    def __init__(self,n):
        self.par = list(range(n+1))
        self.rank = [1]*(n+1)
        
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        par1 = self.find(x)
        par2 = self.find(y)      
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1]+=self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2]+=self.rank[par1]
            
    def is_same(self,a,b):
        return self.find(a)==self.find(b)
            
            
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key= lambda x: x[2])
        cost = 0
        ds = DSU(n)
        total = 0
        for i in range(len(connections)):
            a,b,c = connections[i]
            if ds.is_same(a,b):
                continue
            ds.union(a,b)
            cost += c
            total+=1
        
        if total == n-1:
            return cost
        return -1
        