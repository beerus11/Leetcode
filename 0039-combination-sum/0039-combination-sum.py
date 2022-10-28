class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.dp = {}
        def cs(candidates,i,s,arr):
            if (i,s,tuple(arr)) in self.dp:
                return
            if s == 0:
                self.ans.append(tuple(arr[:]))
                self.dp[(i,s,tuple(arr))]=True
                return
            if i == len(candidates) or s<0:
                self.dp[(i,s,tuple(arr))]=True
                return
            if candidates[i]>target:
                self.dp[(i,s,tuple(arr))]=True
                return cs(candidates,i+1,s,arr)
            
            arr.append(candidates[i])
            cs(candidates,i+1,s-candidates[i],arr)
            arr.pop()
            
            arr.append(candidates[i])
            cs(candidates,i,s-candidates[i],arr)
            arr.pop()
            
            cs(candidates,i+1,s,arr)
            
            self.dp[(i,s,tuple(arr))]=True
        cs(candidates,0,target,[])
        return set(self.ans)
        