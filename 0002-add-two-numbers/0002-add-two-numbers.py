# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(-1)
        carry  = 0
        ans = output
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            s = a+b+carry
            output.next = ListNode(s%10)
            carry = s//10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            output = output.next
        if carry>0:
            output.next = ListNode(carry)
            output = output.next
        return ans.next
        