# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        create a prev variable that is gonna hold the list
        set curr to head

        iterate over curr
            next_node=curr.next
            set curr.next to prev
            set prev to curr to make it new prev
            set curr to next_node
        return prev.next where the reverse starts
        '''

        prev=None
        curr=head

        while curr!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev