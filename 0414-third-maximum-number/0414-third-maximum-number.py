import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums)<3:
            return max(nums)
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>3:
                heapq.heappop(heap)
        print(heap)
        return heapq.heappop(heap)
                
            
        