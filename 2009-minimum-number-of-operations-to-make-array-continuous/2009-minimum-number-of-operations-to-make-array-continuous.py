class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = float("inf")
        
        for i, start in enumerate(nums):
            search = start + n - 1
            start, end = 0, len(nums)-1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= search:
                    idx = mid
                    start = mid + 1
                else:
                    end = mid - 1

            count = idx - i + 1
            ans = min(ans, n - count)
        return ans
            
        