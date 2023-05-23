# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        temp = head
        l = 0
        while temp:
            l+=1
            temp = temp.next
        l = (l//2)-1
        temp = head
        while l>0:
            temp = temp.next
            l-=1
        print(temp.val)
        temp.next = temp.next.next
        return head