class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        left=0
        right=len(array)-1

        iterate over the array left<right
            sum=nums[left]+nums[right]
            if sum==target
                return a list of left,right
            if sum>target:
                right-=1
            if sum<target:
                left+=1
        '''
        seen = {}  # value -> index

        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i