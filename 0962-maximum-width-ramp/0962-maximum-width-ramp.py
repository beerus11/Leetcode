class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        st = []
        for i, n in enumerate(nums):
            if not st or n < nums[st[-1]]: st.append(i)
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            while st and nums[i] >= nums[st[-1]]:
                ans = max(ans, i - st.pop())
        return ans
        """
        st = []
        for k,v in enumerate(nums):
            if not st or v<nums[st[-1]]:
                st.append(k)
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                ans = max(ans,i-st.pop())
        return ans
        