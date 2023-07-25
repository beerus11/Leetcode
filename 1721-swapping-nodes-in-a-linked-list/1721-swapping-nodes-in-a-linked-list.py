# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fn,sn= None,None
        
        temp = head
        l = 1
        while temp:
            if l== k:
                fn=temp
            temp = temp.next
            l+=1
        temp = head
        l = l-k-1
        while temp and l>0:
            temp = temp.next
            l-=1
        sn = temp
        fn.val,sn.val = sn.val,fn.val
        
        return head
        