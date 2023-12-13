class Solution:
    def minDays(self, n: int) -> int:
        q = [(0,n)]
        seen = set()
        while q:
            s,o = heapq.heappop(q)
            if o<0 or (o,s) in seen:
                continue
            seen.add((o,s))
            if o==0:
                return s
            if o%3==0:
                x = (o-2*(o//3))
                heapq.heappush(q,(s+1,x))
            if o%2==0:
                x = o//2
                heapq.heappush(q,(s+1,o-x))
            heapq.heappush(q,(s+1,o-1))
        
        return -1
        