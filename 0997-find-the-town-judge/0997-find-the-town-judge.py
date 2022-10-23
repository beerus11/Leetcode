class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return n
        if len(trust)==0 and n>1:
            return -1
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)
        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1
        print(indegree)
        print(outdegree)
        ans = []
        for k,i in enumerate(indegree):
            if i == (n-1) and outdegree[k]==0:
                ans.append(k)    
        print(ans)
        return ans[0] if len(ans)==1 else -1
            
            
        