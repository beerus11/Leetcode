"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.mx = 0
        def dfs(node):
            if not node:
                return 0
            paths = [0]
            for child in node.children:
                x = 1+dfs(child)
                heapq.heappush(paths,x)
                if len(paths)>2:
                    heapq.heappop(paths)
            if len(paths)==2:
                self.mx = max(self.mx,paths[0]+paths[1])
            if len(paths)==1:
                self.mx = max(self.mx,paths[0])
            return max(paths)
            
        dfs(root)
        return self.mx