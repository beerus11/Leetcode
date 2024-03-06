"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.hm = {}
        def clone(n):
            if not n:
                return None
            if n in self.hm:
                return self.hm[n]
            node = Node(n.val)
            self.hm[n]=node
            for nei in n.neighbors:
                node.neighbors.append(clone(nei))
            return node
                
        return clone(node)
        