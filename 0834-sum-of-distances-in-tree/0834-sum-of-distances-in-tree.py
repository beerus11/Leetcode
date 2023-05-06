class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        
        count = [1]*n
        ans = [0]*n
        
        def dfs(node=0,parent=None):
            for child in g[node]:
                if child!=parent:
                    dfs(child,node)
                    count[node]+=count[child]
                    ans[node]+= ans[child]+count[child]
        def dfs2(node=0,parent=None):
            for child in g[node]:
                if child!=parent:
                    ans[child]= ans[node]-count[child]+(n-count[child])
                    dfs2(child,node)
        dfs()
        dfs2()
        
        return ans
        