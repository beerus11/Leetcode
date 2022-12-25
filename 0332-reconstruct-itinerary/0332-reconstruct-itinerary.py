from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path, d = [], defaultdict(list)
        for a,b in tickets:
            insort(d[a], b)
        
        def dfs(loc):
            while d[loc]:
                dfs(d[loc].pop(0))
            path.append(loc)
            
        dfs("JFK")
        return path[::-1]