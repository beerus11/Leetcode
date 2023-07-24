class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        ls = 1
        ns = set(nums)
        for k,v in enumerate(nums):
            t = 0
            if v-1 not in ns:
                j = v
                while j in ns:
                    j+=1
                    t+=1
            ls = max(ls,t)
        return ls
            
        