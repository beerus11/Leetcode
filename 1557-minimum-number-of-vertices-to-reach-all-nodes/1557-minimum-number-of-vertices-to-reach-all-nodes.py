class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = {i:0 for i in range(n)}
        for a,b in edges:
            g[a].append(b)
            indegree[b]+=1
        nodes = []
        for k,v in indegree.items():
            if v==0:
                nodes.append(k)
        return nodes

        