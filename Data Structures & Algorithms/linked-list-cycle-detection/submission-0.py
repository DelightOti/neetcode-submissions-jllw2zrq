# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        use fast and slow pointer method
        basically increment slow by 1
        and increment fast by 2 and eventually if there is a cycle they will meet
        if not return false
        '''

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False