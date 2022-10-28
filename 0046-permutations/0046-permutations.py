class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def p(arr,i):
            if i == len(arr)-1:
                self.ans.append(arr[:])
                return
            for j in range(i,len(arr)):
                arr[i],arr[j] = arr[j],arr[i]
                p(arr,i+1)
                arr[i],arr[j] = arr[j],arr[i]
                
        p(nums,0)
        return self.ans