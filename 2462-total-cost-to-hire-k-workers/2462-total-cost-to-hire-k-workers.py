class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        fh = []
        eh = []
        l,r = 0,len(costs)-1
        for _ in range(k):
            while len(fh)<candidates and l<=r:
                heapq.heappush(fh,costs[l])
                l+=1
            while len(eh)<candidates and l<=r:
                heapq.heappush(eh,costs[r])
                r-=1
            a = fh[0] if fh else float('inf')
            b = eh[0] if eh else float('inf')
            
            if a<=b:
                total_cost+=a
                heapq.heappop(fh)
            else:
                total_cost+=b
                heapq.heappop(eh)
        
        
        return total_cost
        