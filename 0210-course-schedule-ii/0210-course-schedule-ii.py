class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
        q = []
        for k,v in enumerate(indegree):
            if v==0:
                q.append(k)
        visited = set()
        ans = []
        while q:
            n = q.pop(0)
            ans.append(n)
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(ans)!=numCourses:
            return []
        return ans
        
            
        
            
        
        