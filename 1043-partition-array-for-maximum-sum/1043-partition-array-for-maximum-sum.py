class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def maxSum(start):
            if start>=len(arr):
                return 0
            curr_sum = 0
            curr_max = 0
            end = min(len(arr),start+k)
            for i in range(start,end):
                curr_max = max(curr_max,arr[i])
                curr_sum = max(curr_sum,curr_max*(i-start+1)+maxSum(i+1))
            return curr_sum
        return maxSum(0)
                
        