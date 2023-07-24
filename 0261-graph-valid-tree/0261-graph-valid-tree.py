class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        
        self.count =0
        visited = set()
        def dfs(node,parent):
            if node==None:
                return
            self.count+=1
            visited.add(node)
            for nei in g[node]:
                if nei==parent:
                    continue
                if nei in visited:
                    return False
                result = dfs(nei,node)
                if not result:
                    return False
            return True
        
        return dfs(0,-1) and self.count==n
                
        