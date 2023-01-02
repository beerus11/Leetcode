class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_till_now,max_so_far = 0,0
        sp = 0
        mp = {}
        for k,v in enumerate(s):
            if v in mp and mp[v]>=sp:
                sp = min(k,mp[v]+1)
            mp[v]=k
            max_till_now = k-sp+1
            max_so_far = max(max_so_far,max_till_now)
        return max_so_far
            
            
            
        