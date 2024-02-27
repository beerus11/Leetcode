class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1,n+1))
        self.ans = []
        def gen(i,nums):
            if len(nums)==k:
                self.ans.append(nums[:])
                return
            if i==len(arr):
                return
            nums.append(arr[i])
            gen(i+1,nums)
            nums.pop()
            gen(i+1,nums)
        gen(0,[])
        return self.ans
        
        