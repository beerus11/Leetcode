# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp,tail = head.next,head
        while temp:
            while temp and tail.val == temp.val:
                temp = temp.next
            tail.next = temp
            tail = tail.next
            if temp:
                temp = temp.next
        return head
        
        