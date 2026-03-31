# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        '''
        current = root
        while current node exist
            if p.val and q.val> root.val:
                search the righ tree
            elif its in the left tree:
                search the left tree
            else
                it split and that is the node we need so return curr
        return none if tree is emptty
        '''

        curr=root
        while curr!=None:
            if p.val > curr.val and q.val > curr.val:
                curr=curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr=curr.left
            else:
                return curr
        return None