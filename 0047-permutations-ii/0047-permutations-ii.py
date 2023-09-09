class Solution:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        self.ans = set()
        def permute(j):
            if j== len(arr):
                self.ans.add(tuple(arr[:]))
                return
            for i in range(j,len(arr)):
                arr[i],arr[j]=arr[j],arr[i]
                permute(j+1)
                arr[i],arr[j]=arr[j],arr[i]
        permute(0)
        return self.ans
        