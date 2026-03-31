# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        '''
        understanding: count the number of nodes from the longest path of the root to leaf node

        plan:
        implement recursively 

        left_depth=0
        right_depth=0
        count=1

        if not root:
            return 0

        if root.left
            left_depth=count+self.maxDepth(root.left)
        
        if root.right
            right_depth=count+self.maxDepth(root.right)

        return count+max(left_depth,right_depth)

        '''
        left_depth=0
        right_depth=0
        count=1

        if not root:
            return 0

        if root.left:
            left_depth=self.maxDepth(root.left)
        
        if root.right:
            right_depth=self.maxDepth(root.right)

        count= count+max(left_depth,right_depth)

        return count