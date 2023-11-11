class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        self.n = n
        for a,b,c in edges:
            self.g[a].append((b,c))

    def addEdge(self, edge: List[int]) -> None:
        a,b,c = edge
        self.g[a].append((b,c))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0,node1)]
        costs = [inf]*(self.n)
        costs[node1]= 0
        while q:
            d,node = heapq.heappop(q)
            if d > costs[node]:
                continue
            if node==node2:
                return d
            for nei,cost in self.g[node]:
                new_cost = d+cost
                if d < costs[nei]:
                    costs[nei]=new_cost
                    heapq.heappush(q,(new_cost,nei))
                    
        return -1
                
                
            


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)