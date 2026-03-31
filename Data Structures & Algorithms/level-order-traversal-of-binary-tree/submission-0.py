# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        '''
        create a list to bee returned

        def dfs(root)
            if node is empty
                return
            
            if level doesnt exist
                append to list
            
            append the nodes on the level to list

            pass dfs(root.left, level+1)
            pass dfs(root.right, level+1)
        
        dfs(root,0)
        return res
        '''

        res= []

        def dfs(node,level):
            if not node:
                return
            
            if level == len(res):
                res.append([])
            
            res[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root,0)
        return res