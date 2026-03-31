# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        '''
        iterate over the linked list to get the count
        index to be removed is N(count) - n(node from back)
        iterate over linked list again
            if cur.next is equal to index
                set cur.next to cur.next.next
        '''

        N=0
        curr=head
        while curr!=None:
            N+=1
            curr=curr.next
        
        # index to be removed
        index=N-n
        
        if index==0:
            return head.next

        curr=head
        i=0
        while curr.next!=None:
            if i+1==index:
                curr.next=curr.next.next
                break
            curr=curr.next
            i+=1
        return head

        

