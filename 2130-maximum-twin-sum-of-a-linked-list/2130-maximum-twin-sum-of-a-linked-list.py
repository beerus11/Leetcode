# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        mx = float('-inf')
        for i in range(len(arr)):
            a,b = arr[i],arr[len(arr)-1-i]
            mx = max(mx,a+b)
        return mx
        