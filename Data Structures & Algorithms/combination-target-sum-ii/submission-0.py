class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        create a list res to return
        create a list subset to store pairs as i go

        create dfs recusive function
            Base case
            if sum>target:
                return
            if sum==target:
                append a copy of subset to result
            
            # build the decision tree for backtracking
            # for each one i can decide whether to add it or add the next one
            # whenver i hit a base case i should pop the last recent cus that made it greater
            # and try another one the next one
        call dfs function
        return res
        '''
        candidates.sort()
        res = []

        def dfs(start, total, subset):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                subset.append(candidates[i])
                dfs(i + 1, total + candidates[i], subset)
                subset.pop()

        dfs(0, 0, [])
        return res

            

