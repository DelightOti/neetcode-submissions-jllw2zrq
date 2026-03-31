# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        understanding: merging two sorted lists into one

        Plan:
        iterate over list1 and add it to list 2

        create an empty node

        while list1 and list2 exist:
            if list1.val<list2.val:
                node.next=list1
                increment list1
            else list2.val<list1.val:
                node.next=list2
                increment list2
            node=node.next
        
        return node.next

        '''

        dummy= node = ListNode()

        while list1 and list2:
            if list1.val<list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        
        # attach leftovers
        node.next=list1 or list2

        return dummy.next
