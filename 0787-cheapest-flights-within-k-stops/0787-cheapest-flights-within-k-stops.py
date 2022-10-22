from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        memo = collections.defaultdict(list)
        for i,j,c in flights:
            memo[i].append((j,c))
        q = [(0,0,src)]
        seen = {}
        while q:
            cost, stop, cur = heapq.heappop(q)
            if cur == dst:
                return cost
            if cur not in seen or stop < seen[cur]:
                seen[cur] = stop
                if stop <= k:
                    for other, price in memo[cur]:
                        if other not in seen or stop + 1 < seen[other]:
                            heapq.heappush(q, (price + cost, stop + 1, other))
        return -1