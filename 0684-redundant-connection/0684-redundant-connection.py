class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parents = list(range(n))
        
        def union(a,b):
            par_a = find(a)
            par_b = find(b)
            
            if par_a==par_b:
                return False
            
            parents[par_a]=par_b
            
            return True
        
        def find(a):
            if parents[a]!=a:
                return find(parents[a])
            return a
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []
                
            
        