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
    public int pairSum(ListNode head) {
        

        
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null&&fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode prev=null;
        ListNode next1;
        while(slow!=null){
            next1=slow.next;
            slow.next=prev;
            prev=slow;
            slow=next1;
        }
        ListNode first=head;
        ListNode second=prev;
        int sum=0;
        int max=0;
        while(second!=null){
            sum=first.val+second.val;
            if (sum>=max){
                max=sum;
            }
            first=first.next;
            second=second.next;
        }
        return max;
        
            
        }
        
    }