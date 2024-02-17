class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
        
    def union(self,a,b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a==par_b:
            return False
        
        rank_a = self.parent[a]
        rank_b = self.parent[b]
        
        if rank_a>rank_b:
            self.parent[par_b]=par_a
            self.rank[par_a]+=1
        else:
            self.parent[par_a]=par_b
            self.rank[par_b]+=1
        
        return True
    
    def find(self,a):
        if self.parent[a]!=a:
            return self.find(self.parent[a])
        return a
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        dsu = DSU(n) 
        count = n
        
        for t,a,b in logs:
            if dsu.union(a,b):
                count-=1
            
            if count ==1:
                return t
                
        return -1
            
                
                
            
        