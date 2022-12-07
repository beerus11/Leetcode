# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        hm = {}
        i = 1
        temp = head
        while temp:
            hm[i]=temp
            temp = temp.next
            i+=1
        x = i-n
        print(x)
        if x-1 not in hm:
            return head.next
        prev = hm[x-1]
        print(prev.val)
        prev.next = hm[x+1] if x+1 in hm else None
        
        return head
        