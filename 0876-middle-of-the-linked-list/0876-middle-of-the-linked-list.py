# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None :
            return head
        def get_len(node):
            if not node:
                return 0
            return 1+get_len(node.next)
        l = get_len(head)//2
        temp = head
        while l>0:
            temp = temp.next
            l-=1
        return temp
        