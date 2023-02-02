from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        
        for i in range(len(values)):
            a,b = equations[i]
            g[a][b]= values[i]
            g[b][a]= 1/values[i]
        visited = set()
        def dfs(src,dest,no):
            if src ==dest:
                return no
            visited.add(src)
            for n,v in g[src].items():
                if n not in visited:
                    x=dfs(n,dest,no*v)
                    if x!=-1.0:
                        return x
            return -1.0
        ans = []
        for a,b in queries:
            if a not in g or b not in g:
                ans.append(-1.0)
            else:
                visited = set()
                ans.append(dfs(a,b,1))
        return ans
            
        
        