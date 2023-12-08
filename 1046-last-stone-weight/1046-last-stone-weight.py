import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x:-1*x,stones))
        heapq.heapify(heap)
        while len(heap)>1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-1*abs(x-y))
        return -1*heap[0] if len(heap)>0 else 0
            
        
        