class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return 1
        if len(trust)==0 and n>-1:
            return -1
        
        
        g = defaultdict(list)
        
        indegree = {i:0 for i in range(1,n+1)}
        outdegree = {i:0 for i in range(1,n+1)}
        
        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1
        
        arr = []
        for k,v in outdegree.items():
            if v==0 and indegree[k]==n-1:
                arr.append(k)
        
        return arr[0] if len(arr)==1 else -1
            
                
        