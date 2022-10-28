# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        st = []
        temp = head
        startNode,endNode = None,None
        i = 1
        while temp:
            if i==left:
                startNode=temp   
            if i==right:
                endNode=temp
                st.append(temp.val)
                break
            if startNode:
                st.append(temp.val)
            temp = temp.next
            i+=1
        if not endNode:
            return head
        temp = startNode
        while temp!=endNode.next:
            temp.val = st.pop()
            temp = temp.next
        return head