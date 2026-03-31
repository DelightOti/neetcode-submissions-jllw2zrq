# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        left_depth=0
        right_depth=0
        coit

        if root is empty:
            return 0
        
        recursively go down the left subtree to find left_depth
        left_depth=count+self.maxDepth(root.left)
        recursiverly go down the right subtree to find right_depth



        return the greater between the two
        '''

        left_depth=0
        right_depth=0

        if not root:
            return 0
        
        left_depth=1+self.maxDepth(root.left)
        right_depth=1+self.maxDepth(root.right)

        return max(left_depth,right_depth)

        