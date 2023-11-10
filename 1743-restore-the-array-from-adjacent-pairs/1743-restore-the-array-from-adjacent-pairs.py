class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        self.ans = []
        for a,b in adjacentPairs:
            g[a].append(b)
            g[b].append(a)
            
        root = None
        for n in g:
            if len(g[n])==1:
                root = n
                break
                
        def dfs(node, prev):
            self.ans.append(node)
            for nei in g[node]:
                if nei!=prev:
                    dfs(nei,node)
        
        dfs(root,None)
        return self.ans