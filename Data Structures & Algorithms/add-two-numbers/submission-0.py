# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        '''
        set carry=0 
        while list1 and list2 exist
        set total to add value at list1 and value at list2
        carry = total//10

        and add it to the newnode list im going to retirn
        move list1 and list2
        '''
        
        carry=0
        dummy=curr=tbr=ListNode()

        while l1 or l2 or carry:
            if not l1:
                val1=0
            else:
                val1=l1.val
            if not l2:
                val2=0
            else:
                val2=l2.val
            
            total= val1+val2+carry
            carry= total//10

            curr.next=ListNode(total%10)
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        
        return dummy.next
