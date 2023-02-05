from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
            
        q,order = [],[]
        
        for k,v in indegree.items():
            if v==0:
                q.append(k)
        #print(indegree,g)
        visited = set()        
        while q:
            n = q.pop(0)
            order.append(n)
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        count = 0
        for k,v in indegree.items():
            if v >0:
                count+=1
        if count>0:
            return []
        return order