class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        lds = [1]*len(nums)
        longest_len = 1
        longest_subset_index = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    lds[i] = max(lds[i],lds[j]+1)
                    
        longest_len = max(lds)
        for i in range(len(lds)):
            if lds[i] == longest_len:
                longest_subset_index = i
                break
        ans = []
        last = nums[longest_subset_index]
        curr_size = longest_len
        for i in range(longest_subset_index,-1,-1):
            if curr_size == lds[i] and last%nums[i]==0:
                ans.append(nums[i])
                curr_size-=1
                last = nums[i]
                
        return ans[::-1]
        
        