import heapq
class Solution:
    def topKFrequent(self, nums: List[int], l: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i]+=1
        heap = []
        for k,v in hm.items():
            heapq.heappush(heap,(v,k))
            if len(heap)>l:
                heapq.heappop(heap)
        return [v for k,v in heap]
            
        