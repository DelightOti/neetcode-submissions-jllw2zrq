# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
        understandi
        height-balancng:ed tree is a tree which the left and right nodes differ in length
        by no more than 1

        plan:
        go down the left subtree recursively and compute the length
        go down the right subtree recursively and compute the length
        if right - left >=1
            return false
        or 
        left-right>=1
         return false
        return true
        '''

        def max_depth(root):
            if not root:
                return 0
            left_depth=max_depth(root.left)
            right_depth=max_depth(root.right)
            return 1+max(left_depth,right_depth)
            
        if not root:
            return True

        left_depth=max_depth(root.left)
        right_depth=max_depth(root.right)

        if left_depth-right_depth>1:
            return False
        elif right_depth-left_depth>1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        