class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
                
        st =[]
        min_curr = nums[0]
        for i in nums[1:]:
            while st and st[-1][0]<=i:
                st.pop()
            if st and st[-1][1]<i:
                return True
            st.append((i,min_curr))
            min_curr =min(min_curr,i)
        return False
                
        
        