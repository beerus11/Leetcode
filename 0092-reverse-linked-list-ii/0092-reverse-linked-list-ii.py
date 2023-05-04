# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        st =[]
        temp = head
        add = False
        leftNode = None
        i =1
        while temp:
            if not add and i==left:
                add=True
                leftNode = temp
            if add and i>right:
                break
            if add:
                st.append(temp.val)
            temp = temp.next
            i+=1
        st = st[::-1]
        print(st)
        temp = leftNode
        while temp and len(st)>0:
            temp.val = st.pop(0)
            temp = temp.next
        return head
        