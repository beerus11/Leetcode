import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-1*i)
            
        while len(heap)>1:
            a = -1*heapq.heappop(heap)
            b = -1*heapq.heappop(heap)
            if a!=b:
                heapq.heappush(heap,b-a)
            print(heap)
        return 0 if len(heap)==0 else -1*heap[0]
            
        
        