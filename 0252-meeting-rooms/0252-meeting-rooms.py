class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<=1:
            return True
        intervals.sort(key=lambda x: x[0])
        last = intervals[0][1]
        
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            if last>start:
                return False
            last = intervals[i][1]
        return True
        