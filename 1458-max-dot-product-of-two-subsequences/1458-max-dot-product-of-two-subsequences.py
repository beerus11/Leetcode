class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def mxdp(i,j):
            if i== len(nums1) or j== len(nums2):
                return 0
            a = (nums1[i]*nums2[j])+mxdp(i+1,j+1)
            b = mxdp(i+1,j)
            c = mxdp(i,j+1)
            return max([a,b,c])
        ans = mxdp(0,0)
        if ans !=0:
            return ans
        return max(min(nums1)*max(nums2),max(nums1)*min(nums2))
        