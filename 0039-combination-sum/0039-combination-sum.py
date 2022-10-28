class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def cs(candidates,i,s,arr):
            #print(i,s,arr)
            if s == 0:
                self.ans.append(tuple(arr[:]))
                return
            if i == len(candidates) or s<0:
                return
            if candidates[i]>target:
                return cs(candidates,i+1,s,arr)
            
            arr.append(candidates[i])
            cs(candidates,i+1,s-candidates[i],arr)
            arr.pop()
            
            arr.append(candidates[i])
            cs(candidates,i,s-candidates[i],arr)
            arr.pop()
            
            cs(candidates,i+1,s,arr)
        cs(candidates,0,target,[])
        return set(self.ans)
        