class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [nums[0]]
        for i in nums[1:]:
            l.append(l[-1]*i)
        r = [nums[-1]]
        for j in range(len(nums)-2,-1,-1):
            r.append(r[-1]*nums[j])
        r = r[::-1]
        ans = []
        
        for k,v in enumerate(nums):
            if k==0:
                ans.append(r[k+1])
            elif k== len(nums)-1:
                ans.append(l[k-1])
            else:
                ans.append(r[k+1]*l[k-1])
        return ans
            
            
        
        