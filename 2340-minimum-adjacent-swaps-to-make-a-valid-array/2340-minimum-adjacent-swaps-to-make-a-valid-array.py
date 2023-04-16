class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l = len(nums)
        s_i,mx_i=len(nums),0
        s_no,mx_no = float('inf'),float('-inf')
        
        for i in range(len(nums)):
            if nums[i]<s_no:
                s_no,s_i= nums[i],i
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>mx_no:
                mx_no,mx_i= nums[i],i

        mx_swap = (l-1-mx_i)
        mn_swap = (s_i)
        
        #print(mx_swap,mn_swap)
        
        if mx_i < s_i:
            return mx_swap+mn_swap-1
        else:
            return mx_swap+mn_swap