# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        understanding: given root of a binary tree invert it

        plan:
        go through each node
        swap the left and right
        do it recursively
        '''

        if not root:
            return root
        
        temp=root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root