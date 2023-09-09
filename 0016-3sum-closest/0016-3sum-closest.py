class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff,closest = float('inf'),None
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                x = nums[j]+nums[k]+nums[i]
                if abs(target-x)<diff:
                    closest = x
                    diff = abs(target-x)
                if target-x>0:
                    j+=1
                else:
                    k-=1
        return closest
                
            
        