class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(l,r,s):
            #print(l,r,s)
            res = []
            while l<r:
                if nums[l]+nums[r]==s:
                    res.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<s:
                    l+=1
                else:
                    r-=1
            return res
        
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                v = nums[i]+nums[j]
                x = two_sum(j+1,len(nums)-1,target-v)
                for e in x:
                    arr = e
                    arr.append(nums[i])
                    arr.append(nums[j])
                    ans.add(tuple(arr))
        return ans
            
        
        