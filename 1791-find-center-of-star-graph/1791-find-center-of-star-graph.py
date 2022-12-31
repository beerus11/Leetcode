class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count_map = collections.Counter([i for e in edges for i in e])
        mx = -1*float('inf')
        ans = None
        for k,v in count_map.items():
            mx = max(mx,v)
            if mx == v:
                ans = k
        return ans
        