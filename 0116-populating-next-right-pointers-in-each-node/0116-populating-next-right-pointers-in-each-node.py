"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        m = defaultdict(list)
        q = [(0,root)]
        while q:
            l,node = q.pop(0)
            m[l].append(node)
            if node.left:
                q.append((l+1,node.left))
            if node.right:
                q.append((l+1,node.right))
        for k,v in m.items():
            i = 0
            while i <len(v)-1:
                v[i].next =v[i+1]
                i+=1
        return root
                