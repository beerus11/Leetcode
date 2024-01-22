class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges)+1))
        def find(x):
            if x!=parents[x]:
                return find(parents[x])
            return x
        def union(x,y):
            a = find(x)
            b = find(y)
            if a==b:
                return False
            parents[a]=b
            return True
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []
                
            
        