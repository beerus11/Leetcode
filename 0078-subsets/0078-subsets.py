class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        def generate(nums,i,arr):
            if i==len(nums):
                self.ans.add(tuple(arr[:]))
                return
            for j in range(i,len(nums)):
                arr.append(nums[j])
                generate(nums,j+1,arr)
                arr.pop()
                
                generate(nums,j+1,arr)
        generate(nums,0,[])
        return [list(i) for i in self.ans]
                