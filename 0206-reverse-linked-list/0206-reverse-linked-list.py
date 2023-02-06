# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            if not head:
                return head
            if not head.next:
                return head
            nextNode = head.next
            head.next = None
            newhead = rev(nextNode)
            nextNode.next=head
            return newhead
        return rev(head)
        