# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        '''
        Understanding: Reorder the linked list to appear in this format
                        [0, n-1, 1, n-2, 2, n-3, ...]
        Plan:
        
        find the middle of the linked list using fast and slow pointer technique
        reverse the second half of the linked list 
        merge the second list into the fist list

        # set slow pointer to zero
        # set fast pointer to index1
        # set m to none

        # while fast and fast.next exist
            # if slow=fast:
                m=slow
        
        set curr= m.next
        m.next=none
        prev=m.next

        left=curr
        prev=none

        while left (left is curr) exists:
            next_node=left.next
            left.next=prev
            prev=left
            left=next_node
        # return prev

        # merge the second linked list into the first linked list
        
        ptr1= m
        ptr2= prev

        while prev exists:
            ptr3=m.next
            ptr4=prev.next
            m.next=prev
            prev.next=ptr3
            m=ptr3
            prev=ptr4
        '''
        if not head or not head.next:
            return
        # set slow pointer to zero
        slow=head
        # set fast pointer to index1
        fast=head.next
        # set m to none
        m=None

        # while fast and fast.next exist
        while fast and fast.next:
            # if slow=fast:
            slow=slow.next
            fast=fast.next.next
        
        m=slow
        curr= m.next
        m.next=None

        left=curr
        prev=None

        while left:
            next_node=left.next
            left.next=prev
            prev=left
            left=next_node
        # return prev

        first=head
        second=prev
        # merge the second linked list into the first linked list
        while second:
            ptr3=first.next
            ptr4=second.next
            first.next=second
            second.next=ptr3
            first=ptr3
            second=ptr4