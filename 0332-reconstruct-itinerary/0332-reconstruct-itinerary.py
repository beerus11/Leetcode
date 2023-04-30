class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        
        for a,b in tickets:
            insort(g[a],b)
        path = []
        def dfs(node):
            while g[node]:
                dfs(g[node].pop(0))
            path.append(node)
        dfs("JFK")
        return path[::-1]
        