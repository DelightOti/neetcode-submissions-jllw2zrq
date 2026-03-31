# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Understanding: return the depth of a binary tree
        depth=longest path from node to farthest leaf node on either left or right side

        Plan: recursively

        left_depth=0
        right_depth=0
        count=1 for the root
        
        Check if root is empty
            else return 0

        Start at the root
            left_depth= count+ compute the left side recusively
            right_depth= right+ compute the right side recursively
        
        return max betweem left_depth and right_depth
        '''

        left_depth=0
        right_depth=0
        count=1

        if not root:
            return 0
        
        left_depth=count+self.maxDepth(root.left)
        right_depth=count+self.maxDepth(root.right)

        return max(left_depth,right_depth)

        