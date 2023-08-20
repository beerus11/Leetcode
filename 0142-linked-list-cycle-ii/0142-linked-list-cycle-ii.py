# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp,fp = head,head
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            
            if sp == fp:
                break
                
        if not fp or not fp.next:
            return None
        
        fp = head
        
        while sp!=fp:
            fp = fp.next
            sp = sp.next
        return sp
        