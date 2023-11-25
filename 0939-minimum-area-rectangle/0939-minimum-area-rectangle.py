class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set(map(tuple,points))
        ans = float('inf')
        for a,b in s:
            for x,y in s:
                if a!=x and b!=y and (x,b) in s and (a,y) in s:
                    ans = min(ans,abs(x-a)*abs(y-b))
        return ans if ans<float('inf') else 0
        
        
        