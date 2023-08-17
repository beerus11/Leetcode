class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def comb(n,j,arr):
            if n==0 and len(arr)==k:
                ans.append(arr[:])
                return
            if len(arr)>k or n<0:
                return
            for i in range(j,10):
                arr.append(i)
                comb(n-i,i+1,arr)
                arr.pop()
        comb(n,1,[])
        return ans
            
        