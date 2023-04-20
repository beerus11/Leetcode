from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx_arr = deque([])
        ans = []
        for i in range(len(nums)):
            while len(mx_arr)!=0 and nums[i]>=mx_arr[-1][1]:
                mx_arr.pop()
            mx_arr.append((i,nums[i]))
            while len(mx_arr)>k or mx_arr[0][0]<=i-k:
                mx_arr.popleft()
            if i>=k-1:
                ans.append(mx_arr[0][1])
        return ans
        