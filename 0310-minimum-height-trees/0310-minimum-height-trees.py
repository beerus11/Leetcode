from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # if no of nodes less than or equal to 2
        if n <=2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = []
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)
                
        reamining_leaves = n    
        while reamining_leaves>2:
            reamining_leaves -= len(leaves)
            new_leaves = []
            while leaves:
                leave = leaves.pop()
                
                nei = graph[leave].pop()
                graph[nei].remove(leave)
                
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
                
            leaves = new_leaves
                
        return leaves
        