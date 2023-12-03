# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bef,aft = ListNode(0),ListNode(0)
        bh,ah = bef,aft
        while head:
            if head.val<x:
                bef.next = head
                bef = bef.next
            else:
                aft.next = head
                aft = aft.next
            head = head.next
        aft.next = None
        bef.next = ah.next
        return bh.next
        