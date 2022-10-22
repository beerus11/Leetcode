# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_sum  =0
        h1,h2 = l1,l2
        ans = ListNode(0)
        h3 = ans
        while h1 or h2:
            s=prev_sum
            if h1:
                s+=h1.val
                h1 = h1.next
            if h2:
                s+=h2.val
                h2 = h2.next
            if s>=10:
                node = ListNode(s%10)
                prev_sum =  s//10
            else:
                node = ListNode(s)
                prev_sum = 0
            h3.next = node
            h3 = h3.next
        if prev_sum!=0:
            node = ListNode(prev_sum)
            h3.next = node
        return ans.next
            