# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)
        def dfs(node,v,l):
            if not node:
                return
            hm[v].append((l,node.val))
            dfs(node.left,v-1,l+1)
            dfs(node.right,v+1,l+1)
        dfs(root,0,0)
        #print(hm)
        ans = []
        for k,v in sorted(hm.items(),key=lambda x:x[0]):
            ans.append([b for a,b in sorted(v,key=lambda x:x[0])])
        return ans
            