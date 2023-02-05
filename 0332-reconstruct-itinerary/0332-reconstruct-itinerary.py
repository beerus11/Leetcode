from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for a,b in tickets:
            insort(g[a],b)
        path = []
        def dfs(n):
            while g[n]:
                dfs(g[n].pop(0))  
            path.append(n)
        dfs("JFK")
        return path[::-1]

            