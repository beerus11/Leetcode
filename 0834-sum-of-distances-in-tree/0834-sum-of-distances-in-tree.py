from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
           
        dist = {}
        count = [1] *n
        ans = [0] * n
        def dfs(node=0,parent=None):
            for nei in g[node]:
                if nei != parent:
                    dfs(nei,node)
                    count[node] += count[nei]
                    ans[node] += ans[nei]+count[nei]
        def dfs2(node=0,parent=None):
            for nei in g[node]:
                if nei != parent:
                    ans[nei]= ans[node]-count[nei]+n-count[nei]
                    dfs2(nei,node)
        dfs()
        dfs2()
        return ans