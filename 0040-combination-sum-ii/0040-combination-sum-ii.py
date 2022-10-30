class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = set()
        self.dp = {}
        def cs(candidates,i,s,arr):
            k = tuple(arr)
            if (i,s,k) in self.dp:
                return
            if s==0:
                self.ans.add(tuple(arr[:]))
                self.dp[(i,s,k)]=True
                return
            if i == len(candidates):
                self.dp[(i,s,k)]=True
                return
            if candidates[i]>s:
                cs(candidates,i+1,s,arr)
                self.dp[(i,s,k)]=True
                return 
            
            arr.append(candidates[i])
            cs(candidates,i+1,s-candidates[i],arr)
            arr.pop()
            
            cs(candidates,i+1,s,arr)
            self.dp[(i,s,k)]=True
            
        cs(candidates,0,target,[])
        return self.ans