# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        st = []
        while temp:
            st.append(temp.val)
            temp = temp.next
        st = st[::-1]
        temp = head
        while len(st)>0 and temp:
            if st.pop(0)!=temp.val:
                return False
            temp = temp.next
        return True