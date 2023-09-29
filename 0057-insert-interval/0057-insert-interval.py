class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        
        if newInterval[1]<intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals
        elif newInterval[0]>intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        ans = []
        insert= False
        x,y = newInterval
        if newInterval[0]<intervals[0][0]:
            ans.append([min(x,intervals[0][0]),max(y,intervals[0][1])])
            insert = True
        for a,b in intervals:
            if not insert and (a<= x <=b or a<= y <=b):
                ans.append([min(a,x),max(b,y)])
                insert = True
            elif not insert and y<b:
                ans.append([x,y])
                ans.append([a,b])
                insert = True
            elif not insert and a>x:
                ans.append([min(a,x),max(b,y)])
                insert = True
            else:
                if len(ans)==0 or ans[-1][1]<a:
                    ans.append([a,b])
                else:
                    m,n = ans.pop()
                    ans.append([min(a,m),max(b,n)])
        if not insert and ans[-1][1]>=newInterval[0]:
            m,n = ans.pop()
            ans.append([min(x,m),max(y,n)])
            
            
        return ans
        