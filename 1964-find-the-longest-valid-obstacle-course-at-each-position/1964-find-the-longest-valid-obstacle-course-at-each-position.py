
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1]*n
        lis = []
        for i,h in enumerate(obstacles):
            idx = bisect.bisect_right(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx]=h
            ans[i] = idx+1
        return ans
        
        