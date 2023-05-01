# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2 = list1,list2
        ans = ListNode(0)
        head = ans
        while temp1 or temp2:
            if not temp1:
                head.next = temp2
                temp2 = temp2.next
            elif not temp2:
                head.next = temp1
                temp1 = temp1.next
            elif temp1.val<temp2.val:
                head.next = temp1
                temp1 = temp1.next
            else:
                head.next = temp2
                temp2 = temp2.next
            head = head.next
        return ans.next
        