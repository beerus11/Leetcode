class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        heap = []
        
        for a,b in intervals:
            if len(heap)>0 and heap[0]<= a:
                heapq.heappop(heap)
            heapq.heappush(heap,b)
        return len(heap)
        