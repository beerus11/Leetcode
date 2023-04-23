"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def clone(n):
            if not n:
                return
            if n in visited:
                return visited[n]
            
            nd = Node(n.val)
            visited[n]=nd
            if not n.neighbors:
                return nd
            for nei in n.neighbors:
                nd.neighbors.append(clone(nei))
            return nd
        return clone(node)
        