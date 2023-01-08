class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def cs(candidates,t,path):
            if t < 0:
                return 
            if t ==0 :
                self.ans.append(path)
                return
            for i in range(len(candidates)):
                cs(candidates[i:],t-candidates[i],path+[candidates[i]])
           
        cs(candidates,target,[])
        return self.ans
        