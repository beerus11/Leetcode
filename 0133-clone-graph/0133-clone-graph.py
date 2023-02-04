"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        def clone(o):
            if not o:
                return None
            if o in self.visited:
                return self.visited[o]
            
            clone_node = Node(o.val)
            self.visited[o]=clone_node
            
            if o.neighbors:
                clone_node.neighbors = [clone(n) for n in o.neighbors]
                
                
            return clone_node
        return clone(node)
        
        