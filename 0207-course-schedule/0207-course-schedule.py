class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
            
        q = [k for k,v in indegree.items() if v==0]
        seen = set()
        while q:
            n = q.pop(0)
            seen.add(n)
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(seen)==numCourses
            
        
        