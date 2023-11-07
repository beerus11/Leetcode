import heapq
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            heap.append(dist[i]/speed[i])
        heapq.heapify(heap)
        
        t = 0
        while heap:
            at = heapq.heappop(heap)
            if at<=t:
                break
            t+=1
        return t
            
            
        