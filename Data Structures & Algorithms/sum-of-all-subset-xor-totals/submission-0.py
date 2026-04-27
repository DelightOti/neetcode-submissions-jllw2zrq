class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def subset(i, total):

            if i == len(nums):
                return total            

            # inlude i
            include = subset(i+1, total ^ nums[i])
            
            not_include = subset(i+1, total)

            return include + not_include

        return subset(0,0)
            


