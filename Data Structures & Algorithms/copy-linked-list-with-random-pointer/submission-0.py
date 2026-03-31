"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        '''
        Plan:
        make a hasmap to store the copies i make
        in the first iteration make copies of each node and store them in hashmap old to copy
        in the second iteration:
            assign .next and .random pointers using the hashmap
        '''

        OldtoCopy= {None:None}

        curr=head
        while curr:
            copy= Node(curr.val)
            OldtoCopy[curr]=copy
            curr=curr.next
        
        curr=head
        while curr:
            copy=OldtoCopy[curr]
            copy.next=OldtoCopy[curr.next]
            copy.random=OldtoCopy[curr.random]
            curr=curr.next

        return OldtoCopy[head]