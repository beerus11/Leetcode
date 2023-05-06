class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1,n+1))
        self.ans =[]
        def comb(i,path):
            if len(path)==k:
                self.ans.append(path[:])
                return
            if i==len(arr):
                return
            path.append(arr[i])
            comb(i+1,path)
            path.pop()
            comb(i+1,path)
        comb(0,[])
        return self.ans
                
        