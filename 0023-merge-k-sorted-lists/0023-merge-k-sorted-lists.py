# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        i = 0
        for l in lists:
            if l :
                heapq.heappush(heap,(l.val,i,l))
            i+=1
        head = ListNode(0)
        temp = head
        while heap:
            val,ind,node = heapq.heappop(heap)
            temp.next = ListNode(val)
            if node.next:
                heapq.heappush(heap,(node.next.val,ind,node.next))
            temp = temp.next
        return head.next
                
            