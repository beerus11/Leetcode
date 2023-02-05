from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        indegree = {i:0 for i in range(1,n+1)}
        for a,b in relations:
            g[a].append(b)
            indegree[b]+=1
        q = []
        for k,v in indegree.items():
            if v==0:
                q.append(k)
        count = 0
        steps = 0
        while q:
            steps+=1
            nq = []
            for node in q:
                count+=1
                for nei in g[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        nq.append(nei)
            q  = nq

        return steps if count == n else -1
                
        