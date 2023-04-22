class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def cs(arr,s,i):
            if s==target:
                ans.append(arr[:])
                return
            if s>target:
                return
            for j in range(i,len(candidates)):
                arr.append(candidates[j])
                cs(arr,s+candidates[j],j)
                arr.pop()
        cs([],0,0)
        return ans
                
        