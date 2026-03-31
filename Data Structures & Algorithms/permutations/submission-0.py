class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
        if there's nothing in the stack
            return empty list
        
        perms= get the rest of the list minus the first 1
        iterate over the permutation list:
            iterate ove a range of len(p)+1
                copy the permutation
                insert into the copy
                insert into the list
        return the result list
        '''

        if not nums:
            return [[]]
        

        perms= self.permute(nums[1:])
        res=[]
        
        for p in perms:
            for i in range(len(p)+1):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res


        