class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mx = max(arrays[0])
        mn = min(arrays[0])
        ans = float('-inf')
        for i in range(1,len(arrays)):
            curr_min = min(arrays[i])
            curr_max = max(arrays[i])
            a = abs(curr_max-mn)
            b = abs(mx-curr_min)
            ans = max([ans,a,b])
            mx = max(mx,curr_max)
            mn = min(mn,curr_min)
        return ans
            
        