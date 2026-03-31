# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        '''
        do this recursively
        if root is none:
            return False
        if Subroot is None:
            return True
        check if isSametree(root, subroot):
            return True
        
        return self.isSubtree(root.left, subroot) and self.isSubtree(root.right, subroot)
        '''
        def isSametree(root,subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            if root.val!=subroot.val:
                return False
            return isSametree(root.left, subroot.left) and isSametree(root.right, subroot.right)


        if root is None:
            return False
        if subRoot is None:
            return True
        if isSametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)