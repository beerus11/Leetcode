class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def fn(arr):
            arr.sort()
            diff = arr[1]-arr[0]
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1]!=diff:
                    return False
            return True
        ans = []
        for i in range(len(r)):
            x = nums[l[i]:r[i]+1]
            ans.append(fn(x))
        return ans