class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        '''
        sort the array

        index to be returned is
            len(array)-k so
        return sortedarray[index]
        '''

        nums.sort()

        index=len(nums)-k
        return nums[index]
