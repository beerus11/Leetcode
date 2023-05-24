class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        fn,sn = nums[0],float('inf')
        count = 0
        for i in range(len(nums)):
            if nums[i]<=fn:
                fn=nums[i]
            elif nums[i]<=sn:
                sn = nums[i]
            else:
                return True
        return False
            
        