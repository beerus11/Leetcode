"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getp(node,parents):
            if not node.parent:
                parents.append(node)
                return
            parents.append(node)
            getp(node.parent,parents)
        p1,p2 = [],[]
        getp(p,p1)
        getp(q,p2)
        for i in p1:
            for j in p2:
                if i==j:
                    return i