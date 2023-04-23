class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
            
        q = []
        for k,v in indegree.items():
            if v==0:
                q.append(k)
        count = 0
        while q:
            n = q.pop()
            count+=1
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return count==numCourses
                
        