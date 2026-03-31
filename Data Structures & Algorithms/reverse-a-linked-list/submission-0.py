# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        understanding: reverse a linked list and return the new beginning of said list

        plan:
        set curr pointer to be head
        set prev pointer to be None
        iterate over the linkedlist using a while loop (while curr!=null)
            set variable next_node equal to curr.next
            curr.next=prev
            move curr to next_node
            move prev to curr
        return prev
        '''

        curr=head
        prev=None

        while curr!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev