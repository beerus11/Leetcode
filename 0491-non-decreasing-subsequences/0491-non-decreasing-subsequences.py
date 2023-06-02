class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def subs(arr,i):
            if i==len(nums):
                if len(arr)>=2:
                    ans.add(tuple(arr[:]))
                return
            if len(arr)==0 or arr[-1]<=nums[i]:
                arr.append(nums[i])
                subs(arr,i+1)
                arr.pop()
            subs(arr,i+1)
        subs([],0)
        return ans
            
            
            
            
        