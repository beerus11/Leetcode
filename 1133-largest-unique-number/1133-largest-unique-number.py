class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hm = Counter(nums)
        heap = []
        for k,v in hm.items():
            if v==1:
                heapq.heappush(heap,k)
                if len(heap)>1:
                    heapq.heappop(heap)
        if len(heap)==1:
            return heap[0]
        return -1
        