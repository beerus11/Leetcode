class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.rank = {i:None for i in range(n)}
        self.g = defaultdict(list)
        self.conn_dict = {}
        
        for a,b in connections:
            self.g[a].append(b)
            self.g[b].append(a)
            self.conn_dict[(min(a,b),max(a,b))] = 1
        
        def dfs(node,discovery_rank):
            if self.rank[node]:
                return self.rank[node]
            self.rank[node] = discovery_rank
            
            min_rank = discovery_rank+1
            for nei in self.g[node]:
                if self.rank[nei] and self.rank[nei]==discovery_rank-1:
                    continue
                rec_rank = dfs(nei,discovery_rank+1)
                
                if rec_rank <= discovery_rank:
                    del self.conn_dict[(min(node,nei),max(node,nei))]
                
                min_rank  = min(min_rank,rec_rank)
                
            return min_rank
        dfs(0,0)
        result = []
        for u,v in self.conn_dict:
            result.append([u,v])
            
        return result