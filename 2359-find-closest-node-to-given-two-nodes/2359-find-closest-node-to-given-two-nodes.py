class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node):
            d = {node:0}
            while node != -1:
                next_node = edges[node]
                if next_node in d:
                    return d
                d[next_node] = d[node] + 1
                node = next_node
            return d
        x = dfs(node1)
        y = dfs(node2)
        
        dc = ((max(x[node], y[node]), node) for node in x.keys() & y.keys())
        return min(dc, default=(0, -1))[1]
            
            
        