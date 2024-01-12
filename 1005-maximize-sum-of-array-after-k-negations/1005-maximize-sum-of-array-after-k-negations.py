class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        s=sum(nums)
        while k>0:
            x = heapq.heappop(nums)
            heapq.heappush(nums,-1*x)
            s-=x
            s+=-1*x
            k-=1
        return s
            
        