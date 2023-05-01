# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hm = {}
        temp = ListNode(-1)
        temp.next = head
        ans = temp
        i =0
        while temp:
            hm[i]=temp
            temp = temp.next
            i+=1
        if n==1:
            x = i-n
            hm[x-1].next = None
        else:
            j = i-n
            p = hm[j-1]
            n = hm[j+1] if j+1<i else None
            p.next = n
        return ans.next
            
            
        