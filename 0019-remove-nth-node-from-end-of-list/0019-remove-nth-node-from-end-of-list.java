/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getLength(ListNode node){
        int ans = 0;
        ListNode temp = node;
        while(temp!=null){
            ans+=1;
            temp = temp.next;
        }
        return ans;
    }
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        int l = getLength(head);
        int x = l-n-1;
        while(x>0){
            temp = temp.next;
            x-=1;
        }
        
        if(x<0){
            return head.next;
        }
        
        if(temp.next!=null){
             temp.next=temp.next.next;
        }
        return head;
    }
}