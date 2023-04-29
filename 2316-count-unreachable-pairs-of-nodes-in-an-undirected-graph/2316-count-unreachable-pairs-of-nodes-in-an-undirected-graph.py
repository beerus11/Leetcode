class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        visited = set()   
        def dfs(node):
            count = 1
            visited.add(node)
            for nei in g[node]:
                if nei not in visited:
                    count+=dfs(nei)
            return count
        remain = n
        ans = 0
        for i in range(n):
            if i not in visited:
                s = dfs(i)
                ans+=s*(remain-s)
                remain -=s
        return ans
                
            