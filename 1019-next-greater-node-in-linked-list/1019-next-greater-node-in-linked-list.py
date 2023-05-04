# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []
        q = []
        temp = head
        while temp:
            q.append(temp.val)
            temp = temp.next
        for i in range(len(q)-1,-1,-1):
            while len(st)>0 and st[-1]<=q[i]:
                st.pop()
            if len(st)==0:
                ans.append(0)
            else:
                ans.append(st[-1])
            st.append(q[i])
        return ans[::-1]
            
            
        
        