# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        def dfs(node,st):
            if not node:
                return
            st.append(str(node.val))
            
            if not node.left and not node.right:
                self.ans.append("->".join(st))
                st.pop()
            dfs(node.left,st[:])
            dfs(node.right,st[:])
        dfs(root,[])
        return self.ans
            
        