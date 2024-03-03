class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(defaultdict)
        for i in range(len(equations)):
            a,b = equations[i]
            g[a][b]=values[i]
            g[b][a]=1/values[i]
        v = set()
        def dfs(src,dest,no):
            if src==dest:
                return no
            v.add(src)
            ans = 1
            for nei,value in g[src].items():
                if nei not in v:
                    x = dfs(nei,dest,no*value)
                    if x!=-1.0:
                        return x
            return -1.0
        
        ans = []
        for q in queries:
            a,b = q
            v = set()
            if a not in g or b not in g:
                ans.append(-1.0)
            else:
                ans.append(dfs(a,b,1))
        return ans
        