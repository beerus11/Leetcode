from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s, d, c in flights:
            graph[s].append((d, c))
 
        pq = [(0, src, 0)] 
        seen = {}
 
        while pq:
            curr_cost, curr_node, curr_stops = heapq.heappop(pq)
            if curr_node == dst:
                return curr_cost
            if curr_node not in seen or curr_stops<seen[curr_node]:
                seen[curr_node]=curr_stops
                if curr_stops <= k:
                    for dest, cost in graph[curr_node]:
                        if dest not in seen or curr_stops+1<seen[dest]:
                            heapq.heappush(pq, (curr_cost + cost, dest, curr_stops+1))
        return -1