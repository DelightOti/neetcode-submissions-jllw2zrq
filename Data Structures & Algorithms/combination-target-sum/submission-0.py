class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        create a list res to return result

        create a list subset to return subset

        create recursive dunction dfs(i,sum):
            # base case
            if sum==target:
                res.append(subset.copy())
                return
            if sum>target:
                discard subset or do nothing with subset
                return
            
            for each number since we can add it an unlimited number of times
            so to include it 
            append it to subset
            call dfs(i, sum + candidates[i])
            pop last subset so we can go down a different branch

            # to skip it and go to next
            dfs(i+1,sum)
        dfs(0,0)
        return res
        '''

        res=[]
        subset=[]

        def dfs(i,sum):
            if sum==target:
                res.append(subset.copy())
                return
            if sum>target or i==len(nums):
                return
            
            # inclusion
            subset.append(nums[i])
            dfs(i,sum+nums[i])
            subset.pop()

            # skip
            dfs(i+1,sum)
        dfs(0,0)
        return res