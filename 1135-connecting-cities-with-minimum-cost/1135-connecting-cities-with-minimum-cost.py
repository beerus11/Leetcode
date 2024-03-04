class DSU:
    def __init__(self,n):
        self.parents = list(range(n+1))
        self.ranks = [1]*(n+1)
        
    def union(self,a,b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a ==par_b:
            return False
        
        if self.ranks[par_a]>self.ranks[par_b]:
            self.parents[par_b]=par_a
            self.ranks[par_a]+=self.ranks[par_b]
        else:
            self.parents[par_a]=par_b
            self.ranks[par_b]+=self.ranks[par_a]
        return True
    
    def find(self,a):
        if a!=self.parents[a]:
            return self.find(self.parents[a])
        return a
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])
        dsu = DSU(n)
        
        total_cost = 0
        joins = 0
        for a,b,c in connections:
            if dsu.union(a,b):
                total_cost+=c
                joins+=1
        if joins!=n-1:
            return -1
                
        return total_cost
            
        
        
        