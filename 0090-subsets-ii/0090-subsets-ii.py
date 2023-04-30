class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums = sorted(nums)
        def subsets(nums,arr,i):
            if i== len(nums):
                self.ans.append(tuple(arr))
                return
            arr.append(nums[i])
            subsets(nums,arr[:],i+1)
            arr.pop()
            subsets(nums,arr[:],i+1)
        subsets(nums,[],0)
        return set(self.ans)
                
        