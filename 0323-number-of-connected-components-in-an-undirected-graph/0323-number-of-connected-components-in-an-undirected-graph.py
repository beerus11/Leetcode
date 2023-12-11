class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.seen = set()
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(node,par=None):
            if node==None or node in self.seen:
                return
            self.seen.add(node)
            for nei in g[node]:
                if nei!=par:
                    dfs(nei,node)
        count =0        
        for node in range(n):
            if node not in self.seen:
                dfs(node)
                count+=1
        return count
            
            
        
        