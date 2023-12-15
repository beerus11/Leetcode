class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        st = set(nums)
        mx = 1
        for i in nums:
            t = 0
            j = i
            if j-1 not in st:
                while j in st:
                    j+=1
                    t+=1
            mx = max(t,mx)
                
        return mx
            
        
            
        