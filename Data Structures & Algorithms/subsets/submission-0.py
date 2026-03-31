class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        create a list res to return subset

        create a subset list to store subsets
        create dfs function to do decision tree
            if i>=len(nums):
                append a copy of subset to res
                return

                # decision to append
                subst.append(nums[i])
                dfs(i+1)
                # decision to remove it
                subset.pop()
                dfs(i+1)
        '''

        res=[]
        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
