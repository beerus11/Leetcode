class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        g = defaultdict(set)
        
        for road in roads:
            g[road[0]].add(road[1])
            g[road[1]].add(road[0])
            
        for n1 in range(n):
            for n2 in range(n1+1,n):
                cr = len(g[n1])+len(g[n2])
                if n2 in g[n1]:
                    cr -=1
                maxRank = max(maxRank,cr)
        return maxRank
        