# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        temp = head
        prev,nxt = head,head
        while prev and nxt:
            if prev == nxt:
                nxt = nxt.next
            elif prev.val == nxt.val:
                prev.next = nxt.next
                nxt = nxt.next
            else:
                prev = prev.next
                nxt = nxt.next
        return temp
            
        