# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        temp = head
        while temp:
            st.append(temp)
            temp = temp.next
        c = 0
        while st:
            x = st.pop()
            v = c+(x.val*2)
            c,x.val = v//10,v%10
        if c==0:
            return head
        else:
            node = ListNode(c)
            node.next = head
            return node
            
            
            
        