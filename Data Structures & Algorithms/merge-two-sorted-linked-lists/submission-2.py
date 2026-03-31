# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        create an empty node

        while list1 and list2 exist:
            if list1.val<list2.val:
                node.next=list1.val
                move list1 up
            elif list2.val<list1.val:
                node.next=list2.val
                move list2 up
        
        if 1 or the other runs out
            add the remaining to the node

        return node.next
        '''

        n=dummy=ListNode()

        while list1 and list2:
            if list1.val<list2.val:
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        
        dummy.next= list1 or list2

        return n.next


       