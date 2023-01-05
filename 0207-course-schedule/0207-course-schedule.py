from collections import defaultdict
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
        visited = set()
        while q:
            n = q.pop()
            visited.add(n)
            for i in g[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return len(visited)==numCourses
                    
        