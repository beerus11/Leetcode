class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        for a,b in intervals:
            if len(rooms)==0 or rooms[0]>a:
                heapq.heappush(rooms,b)
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms,b)
        return len(rooms)
                