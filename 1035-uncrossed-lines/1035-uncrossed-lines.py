class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        @lru_cache(None)
        def solve(i,j):
            if i<=0 or j<=0:
                return 0
            if nums1[i-1]==nums2[j-1]:
                return 1+solve(i-1,j-1)
            return max(solve(i-1,j),solve(i,j-1))
        return solve(m,n)
            
        