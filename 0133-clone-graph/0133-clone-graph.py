"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = {}
        def dfs(n):
            if not n:
                return None
            if n in hm:
                return hm[n]
            x = Node(n.val)
            hm[n]=x
            if not n.neighbors:
                return x
            for nei in n.neighbors:
                x.neighbors.append(dfs(nei))   
            return x
        return dfs(node)
        