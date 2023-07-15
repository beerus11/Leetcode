# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self,node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self,node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
    
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        if key > node.val:
            node.right = self.deleteNode(node.right,key)
        elif key < node.val:
            node.left = self.deleteNode(node.left,key)
        else:
            if not node.left and not node.right:
                node= None
            elif node.right:
                node.val = self.successor(node)
                node.right = self.deleteNode(node.right,node.val)
            else:
                node.val = self.predecessor(node)
                node.left = self.deleteNode(node.left,node.val)       
        return node