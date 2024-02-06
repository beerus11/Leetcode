class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        min_arr = []
        for i in range(len(nums)):
            if len(min_arr)==0:
                min_arr.append(nums[i])
            else:
                min_arr.append(min(min_arr[-1],nums[i]))
                
        st =[]
        for i in range(len(nums)-1,-1,-1):
            if min_arr[i-1]>=nums[i]:
                continue
            while st and min_arr[i]>=st[-1]:
                st.pop()
            if st and st[-1]<nums[i]:
                return True
            st.append(nums[i])
        return False
                
        
        