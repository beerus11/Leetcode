# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sp,fp = head,head.next
        while sp!=fp:
            if not fp or not fp.next:
                return False
            sp = sp.next
            fp = fp.next.next
        return True