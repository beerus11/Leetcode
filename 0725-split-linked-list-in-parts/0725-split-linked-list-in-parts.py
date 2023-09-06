# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        w, r = divmod(N, k)

        
        ans = []
        cur = root
        
        for i in range(k):
            head = cur
            for j in range(w+(i<r)-1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next,cur = None,cur.next
            ans.append(head)
            
        return ans