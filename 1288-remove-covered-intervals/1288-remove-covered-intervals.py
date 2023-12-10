class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0],-x[1]))
        x = intervals[0][1]
        count = 1
        for i in range(1,len(intervals)):
            a = x>=intervals[i][0]
            b = x>=intervals[i][1]
            if a and b :
                continue
            else:
                count+=1
                a,b = intervals[i][0],intervals[i][1]
            x = intervals[i][1]
        
        return count