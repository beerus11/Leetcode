class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hm = Counter(nums)
        ans = 0
        for k,v in hm.items():
            if v==1:
                return -1
            elif v%3==0:
                ans+=v//3
            elif v%3==2:
                ans+= v//3 +1
            elif v%3==1:
                ans+=  (v - 4)//3 + 2
        return ans
        