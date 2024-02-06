class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        max_length = 0
        st = []
        for i in range(len(nums)-1,-1,-1):
            if len(st)==0:
                st.append((nums[i],i))
            elif nums[i]<st[-1][0]:
                st.append((nums[i],i))
        #st = st[::-1]
        print(st[::-1])
        for i in range(len(nums)):
            while st and st[-1][0]<nums[i]:
                max_length = max(max_length,st.pop()[1]-i+1)
        return max_length
                
                
        