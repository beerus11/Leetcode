# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = ListNode(0)
        head = ans
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap,(l.val,l))
        while len(heap)>0:
            value,n = heapq.heappop(heap)
            node = ListNode(n.val)
            head.next = node
            head = head.next
            if n.next:
                heapq.heappush(heap,(n.next.val,n.next))
        return ans.next
                
            
        