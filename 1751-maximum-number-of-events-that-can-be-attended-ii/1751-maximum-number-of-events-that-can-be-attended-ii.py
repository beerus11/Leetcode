class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[0])
        print(events)
        dp = {}
        def mv(prev_end_time,i,k):
            if i>len(events)-1 or k==0:
                return 0
            if (prev_end_time,i,k) in dp:
                return dp[(prev_end_time,i,k)]
            if prev_end_time>=events[i][0]:
                dp[(prev_end_time,i,k)]= mv(prev_end_time,i+1,k)
            else:
                a = events[i][2]+ mv(events[i][1],i+1,k-1)
                b = mv(prev_end_time,i+1,k)
                dp[(prev_end_time,i,k)] = max(a,b)
            return dp[(prev_end_time,i,k)]
        return mv(0,0,k)
                
        