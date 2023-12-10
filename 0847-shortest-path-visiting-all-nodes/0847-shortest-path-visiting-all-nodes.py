class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        ending_mask = (1 << n) - 1
        q = [(node, 1 << node) for node in range(n)]
        seen = set(q)
        steps  = 0
        while q:
            nq = []
            for i in range(len(q)):
                nd,mask = q[i]
                for nei in graph[nd]:
                    next_mask = mask|(1<<nei)
                    if next_mask == ending_mask:
                        return 1+steps
                    
                    if (nei,next_mask) not in seen:
                        seen.add((nei,next_mask))
                        nq.append((nei,next_mask))
            steps+=1
            q = nq