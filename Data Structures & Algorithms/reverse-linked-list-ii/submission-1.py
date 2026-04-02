# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        '''
        iterate over list to start of sublist

        store node before start reversing
        store right.next

        flip sublist up until u get to right

        connect the ends
        '''

        dummy = ListNode(None)
        dummy.next = head

        prev = dummy

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for i in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next