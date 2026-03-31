# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        start at the root
        list to be returned

        go down only the right subtree
            append each node to the list

        move only to the right(increment depth)
        call dfs
        return list
        '''

        res=[]
        def dfs(node,depth):

            if not node:
                return
            
            if depth==len(res):
                res.append(node.val)
            
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)

        dfs(root,0)
        return res