"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isLeaf(g,a,b,l):
            x = g[a][b]
            for i in range(a,a+l):
                for j in range(b,b+l):
                    if g[i][j]!=x:
                        return False
            return True
                    
        def constructTree(g,a,b,l):
            node = Node(0)
            n = len(g)
            if isLeaf(g,a,b,l):
                node.isLeaf = True
                node.val = g[a][b]
                return node
            x = int(l/2)
            node.topLeft = constructTree(g,a,b,x)
            node.topRight = constructTree(g,a,b+x,x)
            node.bottomLeft = constructTree(g,a+x,b,x)
            node.bottomRight = constructTree(g,a+x,b+x,x)
            return node
        return constructTree(grid,0,0,len(grid))
        